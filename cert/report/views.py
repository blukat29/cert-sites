from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from report.models import Report
from report.forms import ReportForm

@login_required
def index(request):
    return render(request, "report/index.html")

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = "report/create.html"

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = User.objects.get(username=self.request.user.username)
        report.save()
        return redirect("/report/")

