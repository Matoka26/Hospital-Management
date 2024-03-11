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
        #abstract = True

    username = models.CharField(verbose_name="Username", max_length=31)
    password = models.CharField(verbose_name="Password",max_length=255)
    email = models.EmailField(verbose_name="Email")
    first_name = models.CharField(verbose_name="FirstName", max_length=255)
    last_name = models.CharField(verbose_name="LastName", max_length=255)
    address = models.CharField(verbose_name="Address",max_length=255)   # 511 might work better
                                                                        # .TextField() for longer
    is_deleted = models.BooleanField(verbose_name="Deleted", default=False)   # if a user is no longer working at the hospital
    salary = models.IntegerField(verbose_name="Salary", default=3000)  # minimum wage idk

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

	
    