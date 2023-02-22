from main.views import AboutPage, CompanyPage, FAQPage, IndexPage

from django.urls import path





urlpatterns = [
    path("", IndexPage.as_view(), name="main-index"),
    path("about", AboutPage.as_view(), name="main-about"),
    path("faq", FAQPage.as_view(), name="main-faq"),
    path("company", CompanyPage.as_view(), name="main-company"),
]
