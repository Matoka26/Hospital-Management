from django.urls import path
from .views import (
    UserDetail, UserInfo,
    TreatmentDetail, TreatmentInfo,
    PatientDetail, PatientInfo,
    AssistantInfo, AssistantDetail,
    DoctorInfo, DoctorDetail,
    GeneralManagerInfo, GeneralManagerDetail,
    RecommendsInfo, RecommendsDetail,
)

urlpatterns = [
    path("user/", UserDetail.as_view(), name="user"),
    path("user/<uuid:id>/", UserInfo.as_view()),

    path("treatment/", TreatmentDetail.as_view(), name="treatment"),
    path("treatment/<uuid:id>/", TreatmentInfo.as_view()),

    path("patient/", PatientDetail.as_view(), name="patient"),
    path("patient/<uuid:id>/", PatientInfo.as_view()),

    path("assistant/", AssistantDetail.as_view(), name="assistant"),
    path("assistant/<uuid:id>/", AssistantInfo.as_view()),

    path("doctor/", DoctorDetail.as_view(), name="doctor"),
    path("doctor/<uuid:id>/", DoctorInfo.as_view()),

    path("general-manager/", GeneralManagerDetail.as_view(), name="general-manager"),
    path("general-manager/<uuid:id>/", GeneralManagerInfo.as_view()),

    path("recommends/", RecommendsDetail.as_view(), name="recommendation"),
    path("recommends/<uuid:id>/", RecommendsInfo.as_view()),
]