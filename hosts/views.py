from django.shortcuts import render,HttpResponse
from hosts import check_qr

# Create your views here.

def home(request):
    return HttpResponse('<h1>This home page is for Host</h1>')

def qr_validation(request):
    return render(request,'qr_validation.html')

def check_qr_code(request):
    if request.method == 'POST':
        code=request.POST['qr']

        result = check_qr.check(code)

        return HttpResponse(result)
    return HttpResponse('Something went wrong...')
