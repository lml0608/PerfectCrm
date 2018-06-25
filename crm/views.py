from django.shortcuts import render

# Create your views here.


def dashboard(request):

    return render(request,'crm/dashboard.html')
    #return render(request,'login.html')

def login(request):


    return render(request,'login.html')