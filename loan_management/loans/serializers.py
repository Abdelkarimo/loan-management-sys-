from rest_framework import serializers
from .models import LoanProvider, Customer, Employee, LoanRequest

class LoanProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProvider
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
""" 
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'
 """
class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'
