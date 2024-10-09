from django.shortcuts import render,HttpResponse
from participants import login

# Create your views here.

def home(request):
    return HttpResponse('<h1> This is Participants Home Page</h1>')

def form(request):
    return render(request,'index.html')

def submit_form(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['phone']

        login.login(name,email,number)

        return HttpResponse(f'Form has been submitted..........\nname: <h1>{name}</h1>')
    return HttpResponse('Something went wrong.....')