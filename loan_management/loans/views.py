from rest_framework import generics, status
from rest_framework.response import Response
from .models import LoanProvider, Customer, Employee, LoanRequest
from .serializers import (
    LoanProviderSerializer, 
    CustomerSerializer, 
    EmployeeSerializer, 
    LoanRequestSerializer
)

# LoanProvider Views
class LoanProviderList(generics.ListCreateAPIView):
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer

class LoanProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanProvider.objects.all()
    serializer_class = LoanProviderSerializer

# Customer Views
class CustomerViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Employee Views
class EmployeeViewSet(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Loan Views
class LoanViewSet(generics.ListCreateAPIView):
    queryset = LoanRequest.objects.filter(isApproved=True)
    serializer_class = LoanRequestSerializer

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.filter(isApproved=True)
    serializer_class = LoanRequestSerializer

# LoanRequest Views
class LoanRequestViewSet(generics.ListCreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class LoanRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

class ApproveLoanRequest(generics.UpdateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'approved':
            instance.status = 'approved'
            instance.save()
            return Response({'status': 'Loan request approved'}, status=status.HTTP_200_OK)
        return Response({'status': 'Loan request was already approved'}, status=status.HTTP_400_BAD_REQUEST)
