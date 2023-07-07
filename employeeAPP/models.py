from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

# Employee
class Employee(models.Model):
    DEVELOPMENT = 'Development'
    QUALITY_ASSURANCE = 'Quality Assurance'
    PRODUCT_MANAGEMENT = 'Product Management'
    SALES_BUSINESS_DEVELOPMENT = 'Sales/Business Development'
    MARKETING = 'Marketing'
    CUSTOMER_SUPPORT = 'Customer Support'
    HUMAN_RESOURCES = 'Human Resources'

    DEPARTMENT_CHOICES = [
        (DEVELOPMENT, 'Development'),
        (QUALITY_ASSURANCE, 'Quality Assurance'),
        (PRODUCT_MANAGEMENT, 'Product Management'),
        (SALES_BUSINESS_DEVELOPMENT, 'Sales/Business Development'),
        (MARKETING, 'Marketing'),
        (CUSTOMER_SUPPORT, 'Customer Support'),
        (HUMAN_RESOURCES, 'Human Resources'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    document = models.FileField(upload_to='employee_documents/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name


# Salary
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.employee.name} - {self.amount}"
    
    
    
    
# Task
class Task(models.Model):
    PENDING = 'Pending'
    WORK_IN_PROGRESS = 'Work in Progress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (WORK_IN_PROGRESS, 'Work in Progress'),
        (DONE, 'Done'),
    ]

    name = models.CharField(max_length=100)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
