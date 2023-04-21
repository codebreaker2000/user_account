from users import views
from django.urls import path

urlpatterns = [
   path("",views.index,name="index"),
   path("register/",views.Register,name="register"),
   path("login/",views.Login,name='login'),
   
]
