from django.urls import path
from .views import hompepageview


urlpatterns = [
    path('' , hompepageview ,  name='home')
]