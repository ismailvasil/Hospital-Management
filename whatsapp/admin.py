from django.contrib import admin
from . models import Department,Doctors,Booking

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','Patient_Name','Patient_Phone','Doctor_Name','Booking_Date','Booked_On')
admin.site.register(Booking,BookingAdmin)