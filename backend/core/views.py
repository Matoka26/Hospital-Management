from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import (
    User,
    Treatment,
    Patient,
)
from .serializers import (
    UserSerializer,
    PatientSerializer,
    TreatmentSerializer,
    RecommendsSerializer,
)

# Ment to make a directory of Views and each class to
# have it's file but had issues importing them

class UserDetail(APIView):
    '''
    A simple Viewset for viewing all Users
    '''
    def get(self,request):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInfo(APIView):
    # get user by id
    def get(self,request,id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"user not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    # update user
    def put(self,request,id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"user not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(obj,data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # partial update user 
    def patch(self,request,id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"user not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(obj, data=request.data, partial=True)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete user
    def delete(self,request,id):
        try:
            obj = User.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"user not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"deleted user"}, status=status.HTTP_204_NO_CONTENT)
    


class TreatmentDetail(APIView):
    '''
    A simple Viewset for viewing all Treatments
    '''
    def get(self,request):
        obj = Treatment.objects.all()
        serializer = TreatmentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TreatmentInfo(APIView):

    # get treatment by id
    def get(self,request,id):
        try:
            obj = Treatment.objects.get(id=id)
        except User.DoesNotExist:
            msg = {"msg":"treatment not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TreatmentSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    # update treatment
    def put(self,request,id):
        try:
            obj = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            msg = {"msg":"treatment not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = TreatmentSerializer(obj,data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # partial update Treatment 
    def patch(self,request,id):
        try:
            obj = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            msg = {"msg":"treatment not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = TreatmentSerializer(obj, data=request.data, partial=True)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete Treatment
    def delete(self,request,id):
        try:
            obj = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            msg = {"msg":"treatment not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        obj.save()
        return Response({"msg":"deleted treatment"}, status=status.HTTP_204_NO_CONTENT)
    

class PatientDetail(APIView):
    '''
    A simple Viewset for viewing all Patient
    '''
    def get(self,request):
        obj = Patient.objects.all()
        serializer = PatientSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientInfo(APIView):
    # get patient by id
    def get(self,request,id):
        try:
            obj = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            msg = {"msg":"patient not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    # update patient
    def put(self,request,id):
        try:
            obj = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            msg = {"msg":"patient not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(obj,data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # partial update patient 
    def patch(self,request,id):
        try:
            obj = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            msg = {"msg":"patient not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(obj, data=request.data, partial=True)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete patient
    def delete(self,request,id):
        try:
            obj = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            msg = {"msg":"patient not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"deleted patient"}, status=status.HTTP_204_NO_CONTENT)
  