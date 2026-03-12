from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import Dog
from Dog.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('donate/', Dog.views.donate_view, name='donate'),
    path('dog/', include('Dog.urls')),
    path('user/', include('User.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)