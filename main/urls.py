from django.urls import path
from main import views



urlpatterns = [
    path('get/homepage/', views.getHomePageDetails, name="homepage"),
    path('create/homepage/', views.createHomePage, name="create-homepage"),
]
