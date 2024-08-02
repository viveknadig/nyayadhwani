from django.db import models
from datetime import datetime,timedelta
from tabnanny import verbose
# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import Group, User, Permission
from users.models import Clients,Lawyers

case_choice=(
    ("won","won"),
    ("lost","lost"),
    ("ongoing","ongoing"),
)
court_choice={
    ("high-court","high-court"),
    ("district-court","district-court"),
    ("supreme-court","supreme-court"),

}
active_choice=(
    ("Yes","Yes"),
    ("No","No"),
)

type_of_cases=(
    ("Criminal","Criminal"),
    ("Family","Family"),
    ("Corporate","Corporate"),
    ("Civil","Civil"),
    ("Intellectual property","Intellectual property"),
    ("Cyber","Cyber"),
    ("Contract","Contract"),
)
# Create your models here.
class lawyer_type(models.Model):
    lawyer=models.ForeignKey(Lawyers,on_delete=models.CASCADE)
    type_of_lawyer=models.CharField(max_length=100,choices=type_of_cases)


    def __str__ (self):
        return f"{self.type_of_lawyer}"



class register_case(models.Model):
    type_of_case=models.CharField(max_length=100,choices=type_of_cases,default="Criminal")
    proofs=models.ImageField(default='evid.png', upload_to='evidence_images/')
    Descriptions=models.TextField(null=True)

    def __str__ (self):
        return f"({self.type_of_case}) ({self.proofs}) ({self.Descriptions})"

class case(models.Model):
    case_id=models.AutoField(primary_key=True)
    client_id=models.ForeignKey(Clients,on_delete=models.CASCADE,db_constraint=False)
    lawyer=models.ForeignKey(Lawyers,on_delete=models.CASCADE,db_constraint=False)
    Description=models.CharField(max_length=250)
    image= models.ImageField(default='evid.png', upload_to='evidence_images')
    Active=models.CharField(max_length=100,choices=active_choice,default="Yes")
    court_name=models.CharField(max_length=100,choices=court_choice,default="district-court")
    Date_of_hearing=models.DateField(default=datetime.now()+timedelta(days=1))
    status=models.CharField(max_length=20,choices=case_choice,default="ongoing")

    def __str__ (self):
        return f"{self.Active} ({self.court_name}) ({self.Date_of_hearing}) ({self.status})"
