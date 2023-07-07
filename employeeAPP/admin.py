from django.contrib import admin
from .models import Employee, Salary, Task

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)
    search_fields = ('name',)


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount')
    list_filter = ('employee',)
    search_fields = ('employee__name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'employee__name')


# Customize the admin site header and title
admin.site.site_header = 'Employee Management'
admin.site.site_title = 'Employee Management'

