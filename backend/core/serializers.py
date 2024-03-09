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
	email = EmailField(required=True)
	first_name = CharField(required=True)
	last_name = CharField(required=True)
	address = CharField(required=True)
	is_deleted = BooleanField(required=True)
	salary = IntegerField(required=True)

	class Meta:
		model = models.User
		fields = (
			'email',
			'first_name',
			'last_name',
			'address',
			'is_deleted',
			'salary',
		)

class GeneralManagerSerializer(UserSerializer):
	class Meta:
		abstract = False

class DoctorSerializer(UserSerializer):
	class Meta:
		abstract = False

class AssistantSerializer(UserSerializer):
	class Meta:
		abstract = False


class PatientSerializer(serializers.ModelSerializer):
	email = EmailField(required=True)
	first_name = CharField(required=True)
	last_name = CharField(required=True)

	class Meta:
		model = models.Patient
		fields = (
			'first_name',
			'last_name',
			'email',
		)

class TreatmentSerializer(serializers.ModelSerializer):
	name = CharField(required=True)
	description = CharField(required=True)

	class Meta:
		model = models.Treatment
		fields = (
			'name',
			'description'
		)

class RecommendsSerializer(serializers.ModelSerializer):
	doctor_id = UUIDField(required=True)
	patient_id = UUIDField(required=True)
	treatment_id = UUIDField(required=True)
	days = IntegerField(required=False) 