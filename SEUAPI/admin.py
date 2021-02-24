from django.contrib import admin
from SEUAPI.models import Account,Meter,Power,Bill,Maintenance

# Register your models here.
admin.site.register(Meter)
admin.site.register(Account)
admin.site.register(Power)
admin.site.register(Bill)
admin.site.register(Maintenance)
