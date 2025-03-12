from django import forms
from .models import Salary, Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'designation', 'department', 'bank_name', 'account_no']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
