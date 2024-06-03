from offer_app.models import OffersModel
from main.models import MyUser
from django.db.models import Count


def technology_statistics():
    # Получаем все предложения, которые имеют назначенного студента
    offers_with_students = OffersModel.objects.filter(user_student__isnull=False)
    
    # Считаем количество предложений для каждой квалификации
    qualification_counts = offers_with_students.values('user_student__qualification__name').annotate(count=Count('id')).order_by('-count')

    # Подготавливаем данные для графика
    qualifications = [item['user_student__qualification__name'] for item in qualification_counts]
    counts = [item['count'] for item in qualification_counts]

    context = {
        'qualifications': qualifications,
        'counts': counts
    }
    return context