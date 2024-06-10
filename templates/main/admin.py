from django.contrib import admin
from .models import MyUser, NotificationsModel
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from client.models import OfferJobModel

from student.models import EducationStudentModel, LanguageStudentModel, PortfolioStudentModel, StudentCalendarModel
from offer_app.models import OffersModel


class EducationStudentInline(admin.TabularInline):
    model = EducationStudentModel
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

class LanguageStudentInline(admin.TabularInline):
    model = LanguageStudentModel
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
class PortfolioStudentInline(admin.StackedInline):
    model = PortfolioStudentModel
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
class StudentCalendarInline(admin.TabularInline):
    model = StudentCalendarModel
    extra = 0
    ordering = ['date']
    show_max = 20
    paginate_by = 10

    def has_change_permission(self, request, obj=None):
        return False

class OfferClientInline(admin.StackedInline):
    model = OffersModel
    extra = 0
    filter_vertical = ('tags',)
    fk_name = 'user_client' 

class NotificationsInline(admin.StackedInline):
    model = NotificationsModel
    extra = 0
    readonly_fields = ('message', 'link',)

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_fields(self, request, obj=None):
        return ['message', 'link']

class OfferJobClientInline(admin.StackedInline):
    model = OfferJobModel
    extra = 0
    fk_name = 'user_client' 

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

class OfferStudentInline(admin.StackedInline):
    model = OffersModel
    extra = 0
    filter_vertical = ('tags',)
    fk_name = 'user_student'

    def has_change_permission(self, request, obj=None):
        return False

class RoleFilter(SimpleListFilter):
    title = 'Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('client', 'Client'),
            ('student', 'Student'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'student':
            return queryset.filter(role='student')
        elif self.value() == 'client':
            return queryset.filter(role='client')

class MyUserAdmin(UserAdmin):
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'role', 'email_verified', 'is_staff', 'is_active')
    list_filter = (RoleFilter, 'is_staff', 'is_active', 'email_verified')
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    filter_horizontal = ('skils',)
    date_hierarchy = 'date_joined'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if 'role' in request.GET and request.GET['role'] == 'student':
            queryset |= self.model.objects.filter(qualification__name__icontains=search_term)

        return queryset, use_distinct

    def get_list_filter(self, request):
        filters = list(self.list_filter)
        if 'role' in request.GET and request.GET['role'] == 'student':
            filters.append('qualification')
        return filters
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            return fieldsets
        if obj.role == 'client':
            return(
                (None, {'fields': ('username', 'password', 'user_id_key')}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'image','email', 'phone_number', 'role', 'email_verified', 'address', 'time_zone')}),
                #('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        elif obj.role == 'student':
            return(
                (None, {'fields': ('username', 'password', 'user_id_key')}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'image', 'email', 'phone_number', 'role', 'email_verified', 'address', 'time_zone')}),
                ('Student info', {'fields': ('about', 'price_hour', 'hours_per_week', 'skils', 'qualification', 'balance')}),
                #('Tags', {'fields': ['name'], 'classes': ['collapse']}),  # Добавление filter_horizontal здесь
                #('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        else:
            return(
                (None, {'fields': ('username', 'password', 'user_id_key')}),
                ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'role',)}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.role == 'student':
            return ('user_id_key', 'about', 'time_zone', 'price_hour', 'hours_per_week', 'balance', 'address', 'last_login', 'date_joined', 'role', 'email', 'phone_number',) #email_verified, qualification
        if obj and obj.role == 'client':
            return ('user_id_key', )
        else:
            return ('user_id_key',)

    def get_inline_instances(self, request, obj=None):
        if obj and obj.role == 'client':
            inlines = [OfferClientInline, OfferJobClientInline, NotificationsInline]
            return [inline(self.model, self.admin_site) for inline in inlines]
        elif obj and obj.role == 'student':
            inlines = [OfferStudentInline, EducationStudentInline, PortfolioStudentInline, LanguageStudentInline, NotificationsInline, StudentCalendarInline]
            return [inline(self.model, self.admin_site) for inline in inlines]
        return []



admin.site.register(MyUser, MyUserAdmin)