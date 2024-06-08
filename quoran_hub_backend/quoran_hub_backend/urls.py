
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('course/', include('courseApp.urls')),
    path('exam/', include('examApp.urls')),
    path('blog/', include('blogApp.urls')),
]
