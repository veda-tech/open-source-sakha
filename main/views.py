from django.views.generic import ListView, TemplateView

from projects.models import Project


class IndexPage(ListView):
    template_name = "main/index.html"
    queryset = Project.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        if search := self.request.GET.get("search", None):
            qs = qs.filter(name__icontains=search)
        return qs


class AboutPage(TemplateView):
    template_name = "main/about.html"


class FAQPage(TemplateView):
    template_name = "main/faq.html"


class CompanyPage(TemplateView):
    template_name = "main/company.html"
