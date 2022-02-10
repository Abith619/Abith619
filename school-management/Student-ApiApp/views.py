from django.shortcuts import render
from django.http import JsonResponse
from itsdangerous import Serializer
from rest_framework.views import api_view
from rest_framework.response import Response
from .serializers import Taskserializer
from .models import Task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import employees
from .serializers import employeeSerializer

# Create your views here

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import School, Student
from .serializers import SchoolListSerializer, StudentListSerializer, StudentDetailSerializer, \
AddStudentSerializer, AddSchoolSerializer


class SchoolView(APIView):
    def get(self, request):
        schools = School.objects.all()
        school_serializer = SchoolListSerializer(schools, many=True)
        return Response(school_serializer.data)

    def post(self, request):
        data = request.data
        serializer = AddSchoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status': 'failure', 'error': serializer.errors})


class SchoolDetailView(APIView):
    def delete(self, request, school_id):
        try:
            school = School.objects.get(pk=school_id)
            school.delete()
            return Response({'status': 'success', 'message': 'school data deleted successfully!'})
        except School.DoesNotExist:
            return Response({'status': 'failure', 'message': 'school data not available!'})

    def get(self, request, school_id):
        school = School.objects.get(pk=school_id)
        school_serializer = SchoolListSerializer(school)
        return Response(school_serializer.data)


class StudentView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        students = Student.objects.all()

        # case insensitive query param filter
        if name is not None:
            students = students.filter(name__icontains=name)
        student_serializer = StudentListSerializer(students, many=True)
        return Response(student_serializer.data)

    def post(self, request):
        try:
            data = request.data  # receive body data
            serializer = AddStudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status': 'failure', 'error': serializer.errors})
        except Exception as e:
            return Response({'status': 'failure', 'error': 'server could not process the request'})


class StudentDetailView(APIView):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        return Response(StudentDetailSerializer(student).data)

    def delete(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            student.delete()
            return Response({'status': 'success', 'message': 'student deleted successfully!'})
        except Student.DoesNotExist:
            return Response({'status': 'failure', 'message': 'student data not available!'})

    def put(self, request, student_id):
        data = request.data
        student = Student.objects.get(pk=student_id)
        serializer = AddStudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status': 'failure', 'error': serializer.errors})


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>//',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.Objects.all()
    Serializer = Taskserializer(tasks, many=True)
    return Response(Serializer.data)

@api_view(['GET'])
def tasklist(request, pk):
    tasks = Task.Objects.get(id=pk)
    Serializer = Taskserializer(tasks, many=False)
    return Response(Serializer.data)

@api_view(['POST'])
def tasklist(request):
    Serializer = Taskserializer(data=request.data)
    if Serializer.is_valid():
        Serializer.save()
    return Response(Serializer.data)