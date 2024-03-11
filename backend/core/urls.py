from django.urls import path
from .views import UserDetail, UserInfo

urlpatterns = [
    path("user/", UserDetail.as_view(), name="user"),
    path("user/<uuid:id>/", UserInfo.as_view())
]