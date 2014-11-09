from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

from datetime import datetime

from report.models import Report

class ReportForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(initial=datetime.now)
    image1 = forms.FileField(required=False)
    image2 = forms.FileField(required=False)
    image3 = forms.FileField(required=False)
    image4 = forms.FileField(required=False)
    class Meta:
        model = Report
        fields = ["url", "text", "date", "tags", "image1", "image2", "image3", "image4"]
