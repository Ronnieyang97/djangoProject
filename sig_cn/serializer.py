from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Employee, News, Enterprise


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class EnterpriseSerializer(ModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"
