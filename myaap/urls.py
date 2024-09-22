from django.urls import path
from .import views 
urlpatterns =[
    path('home',views.home, name='home'),
    path('signup',views.signup, name='signup'),
    path('staff',views.getStaff, name='staff'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),

]