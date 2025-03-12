from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    da = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    conveyance = models.DecimalField(max_digits=10, decimal_places=2)
    medical = models.DecimalField(max_digits=10, decimal_places=2)
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=10, decimal_places=2)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2)
    esi_hi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loan_recovery = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tds = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    
    
    @property
    def gross_salary(self):
        return (self.basic_salary + self.da + self.hra + self.conveyance + 
                self.medical + self.special_allowance)
    
    @property
    def net_salary(self):
        return self.gross_salary - (self.provident_fund + self.professional_tax + self.esi_hi + self.loan_recovery + self.other_deduction + self.tds)
    
    def __str__(self):
        return f"Salary of {self.employee.name}"
