from rest_framework import serializers
from .models import Employee, Salary, Task


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
