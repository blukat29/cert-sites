from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

from report.models import Report
from report.forms import ReportForm

@login_required
def index(request):
    reports = Report.objects.all()
    for report in reports:
        report.tags_names = report.tags.names()
    return render(request, "report/index.html", {"reports":reports})

@login_required
def read(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        report.tags_names = report.tags.names()
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

        # Automatically set the author of this report to the
        # current logged in user.
        report.user = User.objects.get(username=self.request.user.username)
        report.save()

        # This saves the tags
        form.save_m2m()
        return redirect("/report/")

    def get_context_data(self, **kwargs):
        context = super(ReportCreateView, self).get_context_data(**kwargs)

        # "user" is for displaying currend logged in user on
        # the top of the page. This is assumed in all pages.
        context["user"] = self.request.user

        # "reporter" is for displaying the author of a report.
        # reporter's info is filled on the report form.
        context["reporter"] = self.request.user

        # True means template is safe to display report form.
        # So though there is no report object, we still pass
        # this context variable.
        context["valid_report"] = True
        return context

class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = "report/create.html"

    def get_object(self):
        try:
            report = Report.objects.get(id=self.kwargs["report_id"])
        except Report.DoesNotExist:
            report = None
        return report

    def get_context_data(self, **kwargs):
        context = super(ReportUpdateView, self).get_context_data(**kwargs)

        # "user" is the current logged in user.
        context["user"] = self.request.user

        if self.object:
            # "reporter" is the user who submitted this report.
            context["reporter"] = self.object.user
            context["valid_report"] = True
        else:
            context["valid_report"] = False
        return context

    def get_success_url(self):
        return "/report/read/" + str(self.kwargs["report_id"])

