from django.urls import path
from .views import register,login_view

app_name = 'users'
urlpatterns = [
    path('users/',register,name="register"),
    path('login/',login_view,name='login')

]