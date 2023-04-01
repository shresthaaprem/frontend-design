from django.urls import path,include
from .import views
urlpatterns = [
   path('', views.Home, name='index'),
   path('about/', views.About, name='about'),
   path('frontend/',views.FrontEnd, name="front"),

]
