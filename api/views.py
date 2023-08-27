from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):

        Company=company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        pass

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer