from django import forms

class DateForm(forms.Form):
    start = forms.IntegerField(label='Start Year', min_value=2012, max_value=2024)
    end = forms.IntegerField(label='End Year', min_value=2012, max_value=2024)