from django import forms
from .models import Employee,EMP_Details,Manager,Create_acc

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'photo', 'department', 'salary', 'email', 'gender', 'phone_number', 'address', 'join_date', 'position']
        
class EMP_DtailsForm(forms.ModelForm):
    class Meta:
        model = EMP_Details
        fields = '__all__'
        
class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        
class Create_acc(forms.ModelForm):
    class Meta:
        model = Create_acc
        fields = '__all__'
        