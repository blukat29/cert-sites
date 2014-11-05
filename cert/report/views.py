from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from report.models import Report
from report.forms import ReportForm

@login_required
def index(request):
    reports = Report.objects.all()
    return render(request, "report/index.html", {"reports":reports})

@login_required
def read(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        report = None
    user = request.user
    return render(request, "report/read.html", {"report":report, "user":user})

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = "report/create.html"

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = User.objects.get(username=self.request.user.username)
        report.save()
        return redirect("/report/")

    def get_context_data(self, **kwargs):
        context = super(ReportCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context["username"] = user.username
        context["real_name"] = user.first_name
        context["phone"] = user.last_name
        context["email"] = user.email
        return context

