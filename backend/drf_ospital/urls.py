from django.urls import path, include
from django.contrib import admin
from core import views as core_views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('core/', include("core.urls")),
]