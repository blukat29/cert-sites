from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from report.models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ["url", "text", "date"]
