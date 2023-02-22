from django.urls import path

from main.views import IndexPage, AboutPage, FAQPage, CompanyPage

urlpatterns = [
    path('', IndexPage.as_view(), name='main-index'),
    path('about', AboutPage.as_view(), name='main-about'),
    path('faq', FAQPage.as_view(), name='main-faq'),
    path('company', CompanyPage.as_view(), name='main-company'),
]
