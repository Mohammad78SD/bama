from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('deal_system.urls'), name=('cars')),
]
