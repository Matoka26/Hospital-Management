from django.urls import path
from django.contrib import admin
from core import views as core_views
from rest_framework import routers

app = 'core'

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    #path('user/', core_views.UserAPIView.as_view()),
]