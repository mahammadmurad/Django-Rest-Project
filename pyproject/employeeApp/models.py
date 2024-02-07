from django.db import models


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.DepartmentName


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=300)
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    DateOfJoining = models.DateTimeField(auto_now_add=True)
    PhotoFileName = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.EmployeeName


# Create your models here.
