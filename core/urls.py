from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('signup/', views.RegisterFormView.as_view(), name='signup'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('addprogram/', views.AddProgramView.as_view(), name='addprogram'),
]
