from django.db import models
from django.db.models.enums import Choices
from django.db.models.expressions import F
#from django.db.models.fields import DurationField

# Create your models here.
class Carrer(models.Model):
    carrer_code=models.CharField(max_length=3,primary_key=True)
    name=models.CharField(max_length=50)
    duration=models.PositiveSmallIntegerField(default=5)

    def __str__(self) -> str:
        txt="{0} (Duration: {1} year(s))"
        return txt.format(self.name,self.duration)

class Student(models.Model):
    dni=models.CharField(max_length=8,primary_key=True)
    lastname1=models.CharField(max_length=35)
    lastname2=models.CharField(max_length=35)
    names=models.CharField(max_length=35)
    birthday=models.DateField()
    sexes=[
        ('F','Female'),
        ('M','Male')
    ]
    sex=models.CharField(max_length=1,choices=sexes,default='F')
    career=models.ForeignKey(Carrer,null=False,blank=False,on_delete=models.CASCADE)
    vigency=models.BooleanField(default=True)

    def fullName(self):
        txt="{0} {1}, {2}"
        return txt.format(self.lastname1,self.lastname2,self.names)
    
    def __str__(self) -> str:
        txt="{0} Career: {1}/{2}"
        if self.vigency:
            studentState="Vigent"
        else:
            studentState="Out"
        return txt.format(self.fullName(),self.career,studentState)


class Course(models.Model):
    code=models.CharField(max_length=6,primary_key=True)
    name=models.CharField(max_length=30)
    credits=models.PositiveSmallIntegerField()
    teacher=models.CharField(max_length=100)

    def __str__(self) -> str:
        txt="{0} ({1} / Teacher: {2})"
        return txt.format(self.name,self.code,self.teacher)

class identificationNumber(models.Model):
    id=models.AutoField(primary_key=True)#Se crea un id uno a uno, campo incremental numérico
    student=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)#Relación de llave foranea
    course=models.ForeignKey(Course,null=False,blank=False,on_delete=models.CASCADE)
    dateIN=models.DateTimeField(auto_now_add=True)#Se llena automaticamente la fecha de creación

    def __str__(self) -> str:
        txt="{0} matriculad{1} en el curso {2} / Date: {3}"
        if self.student.sex=="F":
            sexLetter="a"
        else:
            sexLetter="o"
        
        matriculeDate=self.dateIN.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.student.fullName(), sexLetter, self.course, matriculeDate)
