from django.urls import path,include

from formapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('reg_form/',views.reg_form,name='reg_form'),
    path('add/',views.add_form,name='add_form'),
    path('submit/',views.submit,name='submit'),
    path('logout/',views.logout,name='logout'),



]