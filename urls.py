from django.urls import path

from studentapp import views

urlpatterns=[
    path('', views.log_fun, name='log'),
    path('logindata',views.logdata_fun),
    path('reg',views.register_fun,name='reg'),
    path('read',views.regdata_fun),
    path('home',views.home_fun,name='home'),
    path('add_students',views.add_student_fun,name='add'),
    path('adddata',views.adddata_fun),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')

]