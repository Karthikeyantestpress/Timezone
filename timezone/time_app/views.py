from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect, render
from timezone import settings

common_timezones = {
    "chennai": "Asia/Kolkata",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
}


def set_timezone(request):
    if request.method == "POST":
        request.session["django_timezone"] = request.POST["timezone"]
        request.session["django_timezone_city"] = get_city(
            request.POST["timezone"]
        )
        return redirect(reverse("time"))

    else:
        return render(
            request,
            "time/get_time.html",
            {"timezones": common_timezones.items()},
        )


def get_city(timezones):
    for city, zone in common_timezones.items():
        if zone == timezones:
            city
            return city


def get_time(request):
    time = timezone.now()
    return render(
        request, "time/time.html", {"time": time, "city": settings.city}
    )
