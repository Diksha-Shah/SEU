from rest_framework import serializers
from SEUAPI.models import Account,Meter,Bill,Maintenance,Power

class MeterSerializer(serializers.ModelSerializer):
    '''
        serializer class for the meter model
    '''
    class Meta:
        model = Meter
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    '''
        serializer class for the account model
    '''
    class Meta:
        model = Account
        fields = ("id","first_name","middle_name","last_name","phone_number","email","password","ward","gender","address","meter")
    #for foreign key meter
    def to_representation(self, instance):
        self.fields["meter"] = MeterSerializer(read_only=True)
        return super().to_representation(instance)

class PowerSerializer(serializers.ModelSerializer):
    '''
        serializer class for the power model
    '''
    class Meta:
        model = Power
        fields = ("id","power","voltage","current","energy","timestamp","meter")
    #for foreign key meter
    def to_representation(self, instance):
        self.fields["meter"] = MeterSerializer(read_only=True)
        return super().to_representation(instance)

class BillSerializer(serializers.ModelSerializer):
    '''
        serializer class for the bill model
    '''
    class Meta:
        model = Bill
        fields = ("id","amount","units","timestamp","status","account")
    #for foreign key account
    def to_representation(self,instance):
        self.fields["account"] = AccountSerializer(read_only=True)
        return super().to_representation(instance)

class MaintenanceSerializer(serializers.ModelSerializer):
    '''
        serializer class for the maintenance model
    '''
    class Meta:
        model = Maintenance
        fields = ("id","date","description","resolved","account")
    #for foreign key account
    def to_representation(self,instance):
        self.fields["account"] = AccountSerializer(read_only=True)
        return super().to_representation(instance)