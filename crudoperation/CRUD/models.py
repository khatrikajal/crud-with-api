from django.db import models
import random

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='Profile-Image')
    department = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    join_date = models.DateField()
    position = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=6, unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_unique_employee_id()
        super(Employee, self).save(*args, **kwargs)

    def generate_unique_employee_id(self):
        while True:
            employee_id = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            if not Employee.objects.filter(employee_id=employee_id).exists():
                return employee_id

    def _str_(self):
        return self.name

class EMP_Details(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product_sale = models.IntegerField()
    product_purchase = models.IntegerField()
    total_sales = models.IntegerField()
    total_purchase = models.IntegerField()
    profit = models.IntegerField()
    emp_salary = models.IntegerField()    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.employee)
    
class Create_acc(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    
    def _str_(self):
        return str(self.employee.employee_id)
    
class EMP_login(models.Model):
    employee = models.CharField(max_length=6)
    password = models.CharField(max_length=50)

    def _str_(self):
        return str(self.employee.employee_id)

class Manager(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='Manager')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    manager_id = models.CharField(max_length=6, unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name
    

class Manager_log(models.Model):
    manager = models.CharField(max_length=6)
    password = models.CharField(max_length=50)

    def _str_(self):
        return str(self.manager)