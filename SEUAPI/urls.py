from django.urls import path
from SEUAPI.views import AllAccount,AllBill,AllMaintenance,AllMeter,AllPower

urlpatterns = [
  # username, password, first_name, last_name, email, phone_number POST
  path('user/',AllAccount.as_view(),name="register_user"),
  path('meter/',AllMeter.as_view(),name="meter"),
  path('power/',AllPower.as_view(),name="power"),
  path('bill/',AllBill.as_view(),name="bill"),
  path('maintenance/',AllMaintenance.as_view(),name="maintenance"),
]