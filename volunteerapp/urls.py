from django.urls import path
from volunteerapp import views
urlpatterns=[
  path('',views.index),
  path('login/',views.login),
  path('Register/',views.Register),
  path('VRegAction/',views.VRegAction),
  path('VLogAction/',views.VLogAction),
  path('viewPrograms/',views.ViewPrograms),
  path('Apply/',views.Apply),
  path('ApplyAction/',views.ApplyAction),
  path('applystatus/',views.applystatus),
 
  
  ]
