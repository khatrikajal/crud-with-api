from django.shortcuts import render,redirect

from .forms import EmployeeForm


# Create your views here.



def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request,'registration.html')





def addemployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            # Save the form data to the database
            employee.save()
            # Redirect to a success page or another view
            return redirect('home')
    else:
        form = EmployeeForm()

    return render(request, 'addemployee.html', {'form': form})
