from rest_framework import serializers
from Student.models import Departments, Students

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('StudentId','StudentName','Department','DateOfJoining','PhotoFileName')