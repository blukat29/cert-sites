from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from datetime import datetime

from report.models import Report

class ReportForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(initial=datetime.now)
    class Meta:
        model = Report
        fields = ["url", "text", "date"]
