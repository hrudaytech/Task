from django.urls import path
from .views import EmployeeList, EmployeeDetail, SalaryList, SalaryDetail, TaskList, TaskDetail


urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    # Salary URLs
    path('salaries/', SalaryList.as_view(), name='salary-list'),
    path('salaries/<int:pk>/', SalaryDetail.as_view(), name='salary-detail'),

    # Task URLs
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    
    
]
