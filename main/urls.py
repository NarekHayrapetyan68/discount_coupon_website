from django.urls import path
from .views import HomePage, CompaniesList

app_name = "main"
urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("companies/", CompaniesList.as_view(), name="company")
]
