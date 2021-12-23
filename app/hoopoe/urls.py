from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include(('core.urls', 'core'), namespace='core-v1')),
    path('api/v1/', include(('users.urls', 'users'), namespace='users-v1')),
]
