from django.urls import path

from projects.views import ProjectCreatePage, ProjectDetailPage

urlpatterns = [
    path("create", ProjectCreatePage.as_view(), name="projects-create"),
    path("<pk>", ProjectDetailPage.as_view(), name="projects-detail"),
]
