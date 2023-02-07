from django.urls import path
from adminapp import views
urlpatterns=[
  path('adminlogin/',views.adminlogin),
  path('ALogAction/',views.ALogAction),
  path('AdminHome/',views.adminhome),
  path('postrequirement/',views.postrequirement),
  path('PostAction/',views.PostAction),
  path('viewBooked/',views.ViewApplication),
  path('ConfirmApply/',views.ConfirmApply),
  ]
