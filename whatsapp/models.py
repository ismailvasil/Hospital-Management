from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=255)
    dep_description=models.TextField(max_length=255)
    
    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    
    def __str__(self):
       return "DR" +self.doc_name+' -('+self.doc_spec+')'

class Booking(models.Model):
    Patient_Name=models.CharField(max_length=255)
    Patient_Phone=models.CharField(max_length=10) 
    Patient_Email=models.EmailField()
    Doctor_Name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booking_Date=models.DateField()
    Booked_On=models.DateField(auto_now=True)