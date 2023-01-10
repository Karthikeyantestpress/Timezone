from django import forms


class ChangeTimeZone(forms.Form):

    city_list = [
        ("chennai", "Asia/Kolkata"),
        ("London", "Europe/London"),
        ("Paris", "Europe/Paris"),
        ("New York", "America/New_York"),
    ]
    city = forms.CharField(widget=forms.Select(choices=city_list))
