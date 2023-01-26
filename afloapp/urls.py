from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('formations/', views.formations, name="formations"),
    path('formations/update/<str:pk>/' , views.update_formation , name="update-formation"),
    path('formations/delete/<str:pk>/', views.delete_formation, name="delete-formation"),
    path('formations/create/', views.create_formation , name="create-formation"),
    path('formations/<str:pk>/', views.formation, name="formation"),
    path('about/<str:name>/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
]