from django.contrib import admin
from .models import Employee, Salary  # Import models

admin.site.register(Employee)  # Correct
admin.site.register(Salary)    # Register Salary model as well
