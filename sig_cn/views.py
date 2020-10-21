from __future__ import unicode_literals
from sig_cn.models import Employee, News, Enterprise
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from .serializer import EmployeeSerializer, NewsSerializer, EnterpriseSerializer


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeePartnerView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Investment partner', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeeGlobalView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Global management', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeeManagerView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Investment manager', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeeAdviserView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Investment adviser', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeePostView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Post-investment', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeeLegalView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Legal', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class EmployeeOperationView(APIView):
    def get(self, request):
        employees = Employee.objects.filter(department='Operation', available=1)
        employee_data = EmployeeSerializer(employees, many=True)
        return Response(employee_data.data)


class NewsView(APIView):
    def get(self, request):
        news = News.objects.all()
        news_data = NewsSerializer(news, many=True)
        return Response(news_data.data)


class EnterpriseView(APIView):
    def get(self, request):
        enterprise = Enterprise.objects.filter(available=1)
        enterprise_data = EnterpriseSerializer(enterprise, many=True)
        return Response(enterprise_data.data)


class IndexEnterpriseView(APIView):
    def get(self, request):
        index_enterprise = Enterprise.objects.filter(index=1, available=1)
        index_enterprise_data = EnterpriseSerializer(index_enterprise, many=True)
        return Response(index_enterprise_data.data)
