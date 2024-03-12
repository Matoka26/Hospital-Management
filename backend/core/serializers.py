from . import models
from rest_framework import serializers
from rest_framework.fields import (
    CharField, 
    EmailField,
    BooleanField,
    IntegerField,
	UUIDField,
)

# Ment to make a directory of Serializers and each class to
# have it's file but had issues importing them


class UserSerializer(serializers.ModelSerializer):
	username = CharField(required=True)
	password = CharField(required=True)
	email = EmailField(required=True)
	first_name = CharField(required=True)
	last_name = CharField(required=True)
	address = CharField(required=True)
	is_deleted = BooleanField(required=True)
	salary = IntegerField(required=True)

	class Meta:
		model = models.User
		fields = [
			'username',
			'password',
			'id',
			'created',
			'modified',
			'email',
			'first_name',
			'last_name',
			'address',
			'is_deleted',
			'salary',
		]

class GeneralManagerSerializer(UserSerializer):
	class Meta:
		model = models.GeneralManager
		abstract = False
		fields = '__all__'

class DoctorSerializer(UserSerializer):
	class Meta:
		model = models.Doctor
		abstract = False
		fields = '__all__'

class AssistantSerializer(UserSerializer):
	class Meta:
		model = models.Assistant
		abstract = False
		fields = '__all__'
		


class PatientSerializer(serializers.ModelSerializer):
	email = EmailField(required=True)
	first_name = CharField(required=True)
	last_name = CharField(required=True)

	class Meta:
		model = models.Patient
		fields = '__all__'
		depth = 1
	

class TreatmentSerializer(serializers.ModelSerializer):
	name = CharField(required=True)
	description = CharField(required=True)

	class Meta:
		model = models.Treatment
		fields = '__all__'

class RecommendsSerializer(serializers.ModelSerializer):
	#doctor_id = UUIDField(required=True)
	#patient_id = UUIDField(required=True)
	#treatment_id = UUIDField(required=True)
	days = IntegerField(required=False) 
	class Meta:
		model = models.Recommends
		fields = '__all__'