# Generated by Django 5.1.7 on 2025-03-12 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('da', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conveyance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical', models.DecimalField(decimal_places=2, max_digits=10)),
                ('special_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provident_fund', models.DecimalField(decimal_places=2, max_digits=10)),
                ('professional_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='salary.employee')),
            ],
        ),
    ]
