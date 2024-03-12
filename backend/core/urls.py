from django.urls import path
from .views import (
    UserDetail, UserInfo,
    TreatmentDetail, TreatmentInfo,
    PatientDetail, PatientInfo
)

urlpatterns = [
    path("user/", UserDetail.as_view(), name="user"),
    path("user/<uuid:id>/", UserInfo.as_view()),

    path("treatment/", TreatmentDetail.as_view(), name="treatment"),
    path("treatment/<uuid:id>", TreatmentInfo.as_view()),

    path("patient/", PatientDetail.as_view(), name="patient"),
    path("patient/<uuid:id>", TreatmentInfo.as_view()),
]