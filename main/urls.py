from django.urls import path
from main import views



urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name="user-profile"),
    path('users/profile/update/', views.updateUserProfile, name="user-profile-update"),

    path('users/', views.getUsers, name="users"),

    path('get/homepage/', views.getHomePageDetails, name="homepage"),
    path('get/main/', views.getMainDetails, name="main"),
    path('update/main/<str:id>/', views.updateMain, name="update-main"),
    path('update/home/<str:id>/', views.updateHomePage, name="update-homepage"),
]
