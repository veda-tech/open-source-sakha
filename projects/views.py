from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from projects.forms import ProjectForm
from projects.models import Project


class ProjectCreatePage(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = "projects/project-create.html"

    def form_valid(self, form):
        if not self.request.user.is_staff:
            return HttpResponseRedirect("/")
        self.object: Project = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProjectDetailPage(DetailView):
    template_name = "projects/project-detail.html"
    queryset = Project.objects.all()
