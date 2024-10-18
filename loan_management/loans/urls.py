from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

# Define schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Loan Management API",
        default_version='v1',
        description="API documentation for the Loan Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@loanmanagement.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('providers/', views.LoanProviderList.as_view(), name='provider-list'),
    path('customers/', views.CustomerViewSet.as_view(), name='customer-list'),
    path('employees/', views.EmployeeViewSet.as_view(), name='employee-list'),
    path('loans/', views.LoanViewSet.as_view(), name='loan-list'),
    path('loan-requests/', views.LoanRequestViewSet.as_view(), name='loan-request-list'),
    path('loan-requests/<int:pk>/approve/', views.ApproveLoanRequest.as_view(), name='approve-loan-request'),
    path('providers/<int:pk>/', views.LoanProviderDetail.as_view(), name='provider-detail'),
    path('loans/<int:pk>/', views.LoanDetail.as_view(), name='loan-detail'),
    path('loan-requests/<int:pk>/', views.LoanRequestDetail.as_view(), name='loan-request-detail'),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-json'),
]
