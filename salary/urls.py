from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee, name='add_employee'),
    path('add-salary/', views.add_salary, name='add_salary'),
    path('employee-salary/<str:emp_id>/', views.employee_salary, name='employee_salary'),
    path('employee-list/', views.employee_list, name='employee_list'),
    path('salary-list/', views.salary_list, name='salary_list'),
    path('generate-payslip/<str:emp_id>/', views.generate_pay_slip, name='generate_payslip'),

]
