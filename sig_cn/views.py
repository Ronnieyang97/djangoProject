from __future__ import unicode_literals
from sig_cn.models import Employee, News, Enterprise
from rest_framework.response import Response
from django.db.models import Q
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
        news = News.objects.filter(available=1)
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


class SearchView(APIView):
    def post(self, request):
        if request.data:
            value = request.data['value']
            model_enterprise = Q()
            model_enterprise.connector = 'OR'
            model_enterprise.children.append(('name__contains', value))
            model_enterprise.children.append(('owner__contains', value))
            model_enterprise.children.append(('introduction__contains', value))
            enterprise = Enterprise.objects.filter(model_enterprise, available=1)
            enterprise_data = EnterpriseSerializer(enterprise, many=True)
            model_news = Q()
            model_news.connector = 'OR'
            model_news.children.append(('title__contains', value))
            model_news.children.append(('summary__contains', value))
            model_news.children.append(('introduction__contains', value))
            news = News.objects.filter(model_news, available=1)
            news_data = NewsSerializer(news, many=True)
            return Response([enterprise_data.data, news_data.data])
        else:
            return Response(0)
