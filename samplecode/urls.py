from django.contrib import admin
from django.urls import path, include

from samples.views import top

urlpatterns = [
    path('', top, name='top'),
    path('samples/', include('samples.urls')),
    path('admin/', admin.site.urls),
]