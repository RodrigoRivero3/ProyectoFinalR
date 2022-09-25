from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', lambda req: redirect('AppGameInicio')),
    path('admin/', admin.site.urls),
    path('AppGame/', include('AppGame.urls')),
    path('User/', include('UserApp.urls')),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)