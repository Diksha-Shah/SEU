from django.shortcuts import render
from SEUAPI.models import Meter,Account,Power,Bill,Maintenance
from SEUAPI.serializers import MeterSerializer,AccountSerializer,PowerSerializer,BillSerializer,MaintenanceSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

#class to get all the meters and add one
class AllMeter(APIView):
    '''
        A class to get all meters
    '''
    def get(self,requests):
        meters = Meter.objects.all().order_by("id")
        #meter = Meter.objects.get(model="SM2020")
        serializer = MeterSerializer(meters,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        #mode  = request.POST['model']
        #meter = Meter.objects.get(model=mode)
        serializer = MeterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get all the accounts and add
class AllAccount(APIView):
    '''
        A class to get all accounts
    '''
    def get(self,requests):
        accounts = Account.objects.all().order_by("id")
        serializer = AccountSerializer(accounts,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get all the power and add
class AllPower(APIView):
    '''
        A class to get all power data
    '''
    def get(self,requests):
        power = Power.objects.all().order_by("id")
        serializer = PowerSerializer(power,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = PowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get all the bill and add
class AllBill(APIView):
    '''
        A class to get all bill detail
    '''
    def get(self,requests):
        bill = Bill.objects.all().order_by("id")
        serializer = BillSerializer(bill,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = BillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to get all the maintenance and add
class AllMaintenance(APIView):
    '''
        A class to get all accounts
    '''
    def get(self,requests):
        maintenance = Maintenance.objects.all().order_by("id")
        serializer = MaintenanceSerializer(maintenance,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = MaintenanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)