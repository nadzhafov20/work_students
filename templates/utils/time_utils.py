import pytz
from django.utils import timezone


def current_time_user_tz(user_time_zone):
    current_time_utc = timezone.now()
    user_tz = pytz.timezone(user_time_zone)
    current_time_user_tz = current_time_utc.astimezone(user_tz)
    formatted_event_time = current_time_user_tz.strftime('%I:%M %p').lower()
    return formatted_event_time