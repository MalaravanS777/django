from django.urls import path
from . import views
urlpatterns=[path('',views.todo,name="todo"),
             path("signup",views.signupinfo,name="signup"),
             path("si",views.si,name="si"),
             path("li",views.li,name="li"),
             path("logindetails",views.logindetails,name="logindetails"),
             path("insert",views.insert,name='insert'),
             path("delete",views.delete,name='delete'),
             path('update',views.update,name='update'),
             path('update_con',views.update_con,name='update_con'),
             ]