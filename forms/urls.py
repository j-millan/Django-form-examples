from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "forms"

urlpatterns = [
	path('user_home/', views.user_home, name='user_home'),
	path('job_app/', views.job_application, name='job_app'),
	path('new_car/', views.new_car, name='new_car'),
	path('protect/', views.protector_registration, name='protect'),
	path('mstlogout/', views.logout_request, name='logout_request'),
	path('login/', LoginView.as_view(template_name='forms/auth/login.html'), name='login'),
	path('logout/', LoginView.as_view(template_name='forms/auth/logout.html'), name='logout'),
	path('signup/', views.sign_up, name='sign_up'),
]