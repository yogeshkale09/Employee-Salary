
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Salary
from .forms import SalaryForm, EmployeeForm
# Create your views here.nn



def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        
        form = EmployeeForm()
    return render(request, 'salary/employee_form.html', {'form': form})

def add_salary(request):
    if request.method == "POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm()
    return render(request, 'salary/salary_form.html', {'form': form})

def employee_salary(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    salary = get_object_or_404(Salary, employee=employee)
    return render(request, 'salary/employee_salary.html', {'employee': employee, 'salary': salary})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'salary/employee_list.html', {'employees': employees})

def salary_list(request):
    salaries = Salary.objects.select_related('employee')  # Fetch salary details with employee data
    return render(request, 'salary/salary_list.html', {'salaries': salaries})



def generate_pay_slip(request, emp_id):
    # Get employee and salary details
    print(type(emp_id))
    employee = get_object_or_404(Employee, emp_id=emp_id)
    salary = get_object_or_404(Salary, employee=employee)

    # Create HTTP response with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Pay_Slip_{employee.name}.pdf"'

    # Create PDF document
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "SOFTGRID INFO PVT. LTD.")
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Month: Oct-23")
    p.drawString(400, height - 80, f"UAN Number: 101476794975")

    # Employee Details
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, height - 110, "Employee Pay Slip")
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 140, f"EMP ID: {employee.emp_id}")
    p.drawString(300, height - 140, f"Name: {employee.name}")
    p.drawString(50, height - 160, f"Designation: {employee.designation}")
    p.drawString(300, height - 160, f"Department: {employee.department}")
    p.drawString(50, height - 180, f"Bank: {employee.bank_name}")
    p.drawString(300, height - 180, f"Account No: {employee.account_no}")

    # Salary Details
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 220, "Salary Components")
    p.setFont("Helvetica", 12)

    salary_data = [
        ("Basic Salary", salary.basic_salary),
        ("DA", salary.da),
        ("HRA", salary.hra),
        ("Conveyance Allowance", salary.conveyance),
        ("Medical Allowance", salary.medical),
        ("Special Allowance", salary.special_allowance),
        ("Gross Salary", salary.gross_salary),
        ("Provident Fund", salary.provident_fund),
        ("Professional Tax", salary.professional_tax),
        ("Net Salary", salary.net_salary)
    ]

    y_position = height - 250
    for item, amount in salary_data:
        p.drawString(50, y_position, f"{item}: ₹{amount}")
        y_position -= 20

    # Footer
    p.setFont("Helvetica", 10)
    p.drawString(50, y_position - 30, "Note: This is a computer-generated slip, signature is not required.")

    # Save the PDF document
    p.showPage()
    p.save()

    return response
