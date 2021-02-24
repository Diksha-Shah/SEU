from django.db import models

# Create your models here.

class Meter(models.Model):
    '''
        A Model class that has all the features of the meter
        This is the table where meter is registered.
        Any includes to be made to the meter should be made here
    '''
    #primary id of the meter
    id = models.AutoField(primary_key=True)
    #model of the meter
    model = models.CharField(max_length=50,blank=False, null=False)
    #unique id of the meter (used only for registration)
    uid = models.CharField(max_length=50,blank=False, null=False,unique=True)
    #date when the meter was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+" "+str(self.model)+" "+str(self.uid)+" "+str(self.created)

class Account(models.Model):
    '''
        A Model class that has all the details of customer
        This is the table where customer is registered.
        Any includes to be made to the customer info should be made here
    '''
    #primary id of the customer
    id = models.AutoField(primary_key=True)
    #first name of the customer
    first_name = models.CharField(max_length=20,blank=False,null=False)
    #middle name of the customer
    middle_name = models.CharField(max_length=20)
    #last name of the customer
    last_name = models.CharField(max_length=20,blank=False,null=False)
    #phone number of the customer
    phone_number = models.CharField(max_length=10,blank=False,null=False)
    #email id of the customer
    email = models.EmailField(blank=False,null=False)
    #password of the customer
    password = models.CharField(max_length=15,blank=False,null=False)
    #ward of the customer
    ward = models.CharField(max_length=30,blank=False,null=False)
    #gender of the customer
    gender = models.CharField(max_length=20,blank=False,null=False)
    #address of the customer
    address = models.CharField(max_length=150,blank=False,null=False)
    #meter linked with the account
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE,related_name="meter_owned",blank=True, null=True)

    def __str__(self):
        return str(self.id)+" "+str(self.email)+" "+str(self.phone_number)+" "+str(self.meter)

class Power(models.Model):
    '''
        A Model class that has all the details of energy consumed
        This is the table where amount of energy consumed is stored.
        Any includes to be made to the energy info should be made here
    '''
    #primary id of the power consumed by a meter on a give time
    id = models.AutoField(primary_key=True)
    #power consumed by the meter on a given time 
    power = models.FloatField(blank=False,null=False)
    #voltage consumed by the meter on a given time
    voltage = models.FloatField(blank=False,null=False)
    #current consumed by the meter on a given time
    current = models.FloatField(blank=False,null=False)
    #energy consumed by the meter on a given time
    energy = models.FloatField(blank=False,null=False)
    #meter linked with the power
    meter = models.ForeignKey(Meter,on_delete=models.CASCADE,related_name="power_meter",blank=False, null=False)
    #time at which data was entered
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+" "+str(self.timestamp)+" "+str(self.power)+" "+str(self.meter)


class Bill(models.Model):
    '''
        A Model class that has all the the details of bill
        This is the table where bill is stored.
        Any includes to be made to the bill info should be made here
    '''
    #primary id of the bill
    id = models.AutoField(primary_key=True)
    #amount to be paid by the customer
    amount = models.FloatField(blank=False,null=False)
    #consumed units by the customer
    units = models.FloatField(blank=False,null=False)
    #date and time at which bill is generated
    timestamp = models.DateTimeField(auto_now_add=True)
    #status of the bill(amount paid or unpaid)
    status = models.BooleanField(default=False,blank=False,null=False)
    #account linked with the bill
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,related_name="bill_owner",blank=True,null=True)

class Maintenance(models.Model):
    '''
        A Model class that has all the details of maintenance of the meter
        This is the table where maintenance info is stored.
        Any includes to be made to the maintence info should be made here
    '''
    #primary id of the maintenance info
    id = models.AutoField(primary_key=True)
    #date at which maintenance done
    date = models.DateTimeField(auto_now_add=True)
    #description of what kind of maintenance is done/problem is solved
    description = models.CharField(max_length=150,blank=False,null=True)
    #whether the problem is resolved or not
    resolved = models.BooleanField(blank=False,null=True)
    #account linked with the maintenance
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,related_name="account_owner",blank=True,null=True)
