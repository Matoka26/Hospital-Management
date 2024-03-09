import uuid
from django.db import models
from django_extensions.db.models import TimeStampedModel


# Every model will inherit  this abstract class 
class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True

class User(
	TimeStampedModel, 
	Model
	):

    class Meta:
        app_label = 'core'

    email = models.EmailField(verbose_name="Email")
    first_name = models.CharField(verbose_name="FirstName", max_length=255)
    last_name = models.CharField(verbose_name="LastName", max_length=255)
    address = models.CharField(verbose_name="Address",max_length=255)   # 511 might work better
                                                                        # .TextField() for longer
    is_deleted = models.BooleanField(default=False)   # if a user is no longer working at the hospital
    salary = models.IntegerField(default=3000)  # minimum wage idk

	
    