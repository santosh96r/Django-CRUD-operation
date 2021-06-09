from django.contrib import admin
from django.urls import path
from register import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.add_show, name='addandshow'),
    path('retrive/', views.UsersListView.as_view(), name='retrive'),
    path('edit/<int:id>/', views.edit, name='update'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),

]
