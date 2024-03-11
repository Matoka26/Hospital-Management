from django.db import models
from utils.model_abstracts import Model, User

# Ment to make a directory of Serializers and each class to
# have it's file but had issues importing them

# Chose to make an inheritance instead of a simple role attribute
# so that you can have modularity, you can alter parts of those
# entities independently

class GeneralManager(Model):
    class Meta:
        verbose_name_plural = "GeneralManagers"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gemeral_managers')
    
class Doctor(Model):
    class Meta:
        verbose_name_plural = "Doctors"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    
class Assistant(Model):
    class Meta:
        verbose_name_plural = "Assistants"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistants')
    

class Patient(Model):
    class Meta:
        verbose_name_plural = "Patients"
    
    first_name = models.CharField(verbose_name="FirstName", max_length=255)
    last_name = models.CharField(verbose_name="LastName", max_length=255)
    email = models.EmailField(verbose_name="Email")

    assistants = models.ManyToManyField(Assistant)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

	
class Treatment(Model):
    class Meta:
        verbose_name_plural = "Treatments"

    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.CharField(verbose_name="Description", max_length=1023)

    def __str__(self):
        return f'{self.name}'


# Associative table between Doctor, Patient and Treatment
#
# Note that the primary_key is an artificial key so that
# the combination of foreign_keys is not necessary unique
# so that he can take the same treatment given by the same 
# doctor multiple times

class Recommends(Model):
    class Meta:
        verbose_name_plural = "Recommandations"

    doctor = models.ForeignKey(Doctor, verbose_name="Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name="Patient", on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, verbose_name="TreatmentID", on_delete=models.CASCADE)
    days = models.IntegerField(verbose_name="Days")
