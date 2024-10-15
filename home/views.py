from django.shortcuts import render,HttpResponse
from home import check_qr, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from home.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def home(request):
    return HttpResponse('<h1>This is Home Page...</h1>')

def host(request):
    return HttpResponse('<h1>This home page is for Host</h1>')

def participant(request):
    return HttpResponse('<h1> This is Participants Home Page</h1>')

# def qr_validation(request):
#     return render(request,'qr_validation.html')

# def check_qr_code(request):
#     if request.method == 'POST':
#         code=request.POST['qr']

#         result = check_qr.check(code)

#         return HttpResponse(result)
#     return HttpResponse('Something went wrong...')


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile = Profile(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        profile.save()
        login.login(name,email,number)
        messages.success(request, 'Submitted successfully!')
        
    return render(request,'form.html')

def scan(request):
    return render(request,'scan.html')
@csrf_exempt
def qr_code_scan(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request body
            data = json.loads(request.body)
            scanned_data = data.get('scanned_data')

            # Log or process the scanned data
            # print(f"Received QR Code data: {scanned_data}")

            # Here you can add logic to handle the scanned data, e.g., saving it to the database
            result = check_qr.check(code)

            return HttpResponse(result)

            # Respond with a success message
            # return JsonResponse({'status': 'success', 'scanned_data': scanned_data})

        except json.JSONDecodeError:
            # Handle JSON decode error if the request body is not properly formatted
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
    else:
        # Return an error if the request method is not POST
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)