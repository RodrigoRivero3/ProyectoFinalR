from django.urls import path
from django.contrib.auth.views import LogoutView
from UserApp.views import *
from django.conf import settings

urlpatterns = [
    path('login/', login_request, name='UserLogin' ),
    path('register/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='Usuarios/logout.html'), name= 'UserLogout'),
    path('editar/', editar_usuario, name='UserEditar'),
    path('avatar/', upload_avatar, name='UserAvatar')



]
