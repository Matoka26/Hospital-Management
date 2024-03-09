import uuid
from django.db import models
from utils.model_abstracts import Model, User

# Ment to make a directory of Serializers and each class to
# have it's file but had issues importing them

# Chose to make an inheritance instead of a simple role attribute
# so that you can have modularity, you can alter parts of those
# entities independently

class GeneralManager(User):
    class Meta:
        verbose_name_plural = "GeneralManagers"
    employee_id = models.UUIDField(foreign_key=True, default=uuid.uuid4)
    
    
class Doctor(User):
    class Meta:
        verbose_name_plural = "Doctors"
    employee_id = models.UUIDField(foreign_key=True, default=uuid.uuid4)
    
class Assistant(User):
    class Meta:
        verbose_name_plural = "Assistants"
    employee_id = models.UUIDField(foreign_key=True, default=uuid.uuid4)
    

class Patient(Model):
    class Meta:
        verbose_name_plural = "Patients"
    
    first_name = models.CharField(verbose_name="FirstName", max_length=255)
    last_name = models.CharField(verbose_name="LastName", max_length=255)
    email = models.EmailField(verbose_name="Email")
	
class Treatment(Model):
    class Meta:
        verbose_name_plural = "Treatments"

    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.CharField(verbose_name="Description", max_length=1023)


# Associative table between Assistant and Patient 

class AssistantPatient:
    class Meta:
        verbose_name_plural = "AssistantsPatients"
    
    assistant_id = models.UUIDField(foreign_key=True,verbose_name="AssistantID")
    patient_id = models.UUIDField(foreign_key=True,verbose_name="PatientID")

# Associative table between Doctor, Patient and Treatment
#
# Note that the primary_key is an artificial key so that
# the combination of foreign_keys is not necessary unique
# so that he can take the same treatment given by the same 
# doctor multiple times

class Recommends(Model):
    class Meta:
        verbose_name_plural = "Recommandations"

    doctor_id = models.UUIDField(foreign_key=True,verbose_name="DoctorID")
    patient_id = models.UUIDField(foreign_key=True,verbose_name="PatientID")
    treatment_id = models.UUIDField(foreign_key=True,verbose_name="TreatmentID")
    days = models.IntegerField(verbose_name="Days")
