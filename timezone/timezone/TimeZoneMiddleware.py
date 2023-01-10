import zoneinfo
from django.utils import timezone
from timezone import settings


class TimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
            settings.city = request.session.get("django_timezone_city")
        else:
            timezone.deactivate()
        return self.get_response(request)
