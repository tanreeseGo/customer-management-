from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='logins'),
    path('logout/', views.logoutUser, name='logout'),

    path('' , views.showHome, name='showHome'),
    path('user/', views.userPage, name='user_page'),
    path('customer/<str:pk_test>/' , views.showCustomer, name='showCustomer'),
    path('products/' , views.showProducts, name='showProducts'), 
    
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]
