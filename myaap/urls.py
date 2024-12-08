from django.urls import path
from . import views 
urlpatterns =[
    path('home',views.home, name='home'),
    path('signup',views.signup, name='signup'),
    path('staff',views.getStaff, name='staff'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('search', views.search, name="search"),
    path('product', views.product, name="product"),
    # path('product/edit/<int:pk>', views.editproduct, name="editproduct"),
    path('addproduct', views.product_create, name="product_create"),
    path('edit/<int:pk>', views.product_update, name='product_update'),
    path('viewproduct', views.product_view, name='product_view'),
    path('delete/<int:pk>', views.product_delete, name='product_delete'),

]