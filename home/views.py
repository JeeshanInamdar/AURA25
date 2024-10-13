from django.shortcuts import render,HttpResponse
from home import check_qr, login

def home(request):
    return render(request,'home.html')

def host(request):
    return HttpResponse('<h1>This home page is for Host</h1>')

def participant(request):
    return HttpResponse('<h1> This is Participants Home Page</h1>')

def qr_validation(request):
    return render(request,'qr_validation.html')

def check_qr_code(request):
    if request.method == 'POST':
        code=request.POST['qr']

        result = check_qr.check(code)

        return HttpResponse(result)
    return HttpResponse('Something went wrong...')


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