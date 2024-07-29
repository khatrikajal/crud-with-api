from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name','photo','department','salary','email','gender','phone_number','address','join_date','position','employee_id')
        
admin.site.register(Employee, EmployeeAdmin)
    
    
    
    
   