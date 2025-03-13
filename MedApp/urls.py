
from django.contrib import admin
from django.urls import path
from MedApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
  path('index/', views.index, name='index'),
  path('starter/',views.starter, name='starter'),
  path('about/', views.about, name='about'),
  path('service/', views.service, name='service'),
  path('departments/', views.departments, name='departments'),
  path('doctors/', views.doctors, name='doctors'),
  path('appoint/', views.appoint, name='appoint'),
  path('home/', views.home, name='home'),
  path('contact/', views.contact, name='contact'),
  path('show/', views.show, name='show'),
  path('delete/<int:id>', views.delete, ),
  path('edit/<int:id>', views.edit, name='edit'),
  path('', views.register, name='register'),
  path('login/', views.login_view, name='login'),
  #Mpesa API
  path('pay/', views.pay, name='pay'),
  path('stk/', views.stk, name='stk'),
  path('token/', views.token, name='token'),
  path('transactions/', views.transactions_list, name='transactions'),


]
