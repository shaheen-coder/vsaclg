import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
class Student(models.Model):
    DEPARTMENTS = [
        ("B.E - COMPUTER SCIENCE AND ENGINEERING","B.E-CSE"),
        ("B.E-CIVIL ENGINEERING","B.E CIVIL"),
        ("B.E - ELECTRONICS AND COMMUNICATION ENGINEERING","B.E-ECE"),
        ("B.E - ELECTRICAL AND ELECTRONICS ENGINEERING","B.E-EEE"),
        ("B.TECH -ENGINEERING IN INFORMATION TECHNOLOGY ", "B.TECH-IT"),
        ("B.E - MECHANICAL", "B.E -MECH"),
    ]
    
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(blank=True,null=True)
    age = models.IntegerField()
    dob = models.DateField()
    dept = models.CharField(max_length=50,choices=DEPARTMENTS,default=DEPARTMENTS[0][0])
    year =  models.IntegerField()
    div = models.CharField(max_length=10)
    rollno = models.CharField(max_length=10)
    phone =  models.BigIntegerField()
    address = models.TextField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        try:
            self.email = self.user.email
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
        except Exception as e:
            print(f'error : {e}')
    def __str__(self):
        return f'name:{self.name} dept:{self.dept}'
    
class Teacher(models.Model):
    SUBJECT = [
        ("TAMIL","TAMIL"),
        ("ENGLISH","ENG"),
        ("MATHS","MATH"),
        ("PHYSICE","PHY"),
        ("CHEMISTRY ", "CHEMISTRY"),
        ("COMPUTER SCIENCE", "CS"),
        
    ]
    
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=50,choices=SUBJECT,default='')
    exp =  models.IntegerField()
    hod = models.BooleanField()
    phone =  models.IntegerField()
    slug = models.SlugField(unique=True)
    cls_incharge = models.CharField(max_length=10)
    def save(self, *args, **kwargs):
        try:
            self.email = self.user.email
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
        except Exception as e:
            print(f'error : {e}')
    def __str__(self):
        return f'name:{self.name} dept:{self.subject}'
class Result(models.Model):
    reg_id = models.IntegerField()
    student = models.OneToOneField(Student,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.JSONField()
    def __str__(self):
        return f'name:{self.student.name} RegID:{self.reg_id}'
    