from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.categoryview, name='categories'),
    path('unit/', views.unitview, name='units'),
    path('item/', views.itemview, name='items'),
    path('supplier/', views.supplierview, name='suppliers'),
    path('order/', views.orderview, name='orders'),
    path('employee/', views.employeeview, name='employees'),
    path("", views.home, name="home"),
]