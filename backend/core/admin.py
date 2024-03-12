from django.contrib import admin
from .models import (
    User,
    Treatment,
    Patient,
)

admin.site.register(User)
admin.site.register(Treatment)
admin.site.register(Patient) 