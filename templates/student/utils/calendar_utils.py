import datetime
import calendar
from ..models import StudentCalendarModel


def update_calendar_entries(user, data):
    today = datetime.date.today()
    for entry in data:
        year = entry.get('year', today.year)
        date = datetime.date(year=year, month=int(entry['month']), day=int(entry['day']))
        status = entry['status']
        if status == 'B':
            StudentCalendarModel.objects.update_or_create(user=user, date=date, defaults={'status': 'red'})
        elif status == 'S':
            StudentCalendarModel.objects.update_or_create(user=user, date=date, defaults={'status': 'yellow'})
        elif status == 'N':
            StudentCalendarModel.objects.filter(user=user, date=date).delete()
        else:
            StudentCalendarModel.objects.update_or_create(user=user, date=date, defaults={'status': None})

def get_month_calendar_data(year):
    import calendar
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_data = []
    for month in range(1, 13):
        month_calendar = calendar.monthcalendar(year, month)
        month_data = {
            'month_name': month_names[month - 1],
            'month_number': month,
            'month_calendar': month_calendar,
        }
        months_data.append(month_data)
    return months_data

def get_user_events(user):
    events = StudentCalendarModel.objects.filter(user=user)
    busy_dates = [event.date for event in events if event.status == 'red']
    slightly_busy_dates = [event.date for event in events if event.status == 'yellow']
    return events, busy_dates, slightly_busy_dates

def format_dates(dates, year):
    return [{'year': year, 'month': date.month, 'day': date.day} for date in dates]

def annotate_calendar_with_status(months_data, busy_dates, slightly_busy_dates, current_year):
    for month_data in months_data:
        month = month_data['month_number']
        for week in month_data['month_calendar']:
            for day in week:
                if day != 0:
                    for busy_date in busy_dates:
                        if busy_date.year == current_year and busy_date.month == month and busy_date.day == day:
                            status = 'B'
                            break
                    else:
                        for sl_busy_date in slightly_busy_dates:
                            if sl_busy_date.year == current_year and sl_busy_date.month == month and sl_busy_date.day == day:
                                status = 'S'
                                break
                        else:
                            status = 'F'
                    day_index = month_data['month_calendar'].index(week)
                    month_data['month_calendar'][day_index][week.index(day)] = {'day': day, 'status': status}
    return months_data