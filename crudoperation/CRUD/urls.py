from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    
    path("addemployee/", views.addemployee, name='addemployee'),

]
 