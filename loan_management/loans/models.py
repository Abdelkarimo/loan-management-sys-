from django.db import models

class LoanProvider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name=models.CharField(max_length=20)
    totalFund = models.DecimalField(max_digits=15, decimal_places=2)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name =models.CharField(max_length=20)

class LoanRequest(models.Model):
    loan_id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    isApproved = models.BooleanField(default=False)
    items = models.CharField(max_length=250)
    approvalDate = models.DateField(null=True, blank=True)
    deadLine = models.DateField()
    interestRate = models.DecimalField(max_digits=5, decimal_places=2)
    payDay = models.DateField(null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    minimumPayment = models.DecimalField(max_digits=10, decimal_places=2)
    maximumPayment = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(LoanProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
""" 
class LoanRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    isApproved = models.BooleanField(default=False)
    items = models.CharField(max_length=250)
    provider = models.ForeignKey(LoanProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
 """