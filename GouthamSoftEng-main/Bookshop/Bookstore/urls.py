from django.contrib import admin
from django.urls import path, include
from . import views
 


urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    path('',views.home, name="home"),
    path('logout/',views.logout,name="logout"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]