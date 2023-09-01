from django.shortcuts import render,redirect
from django.views import View
from Code_mantra_app.models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

class ContactUs(View):
    def get(self,request):
        return render(request,'index.html')
    
    def post(self,request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        about_yourself = request.POST['about_yourself']
        
        subject = 'Mail from Code Mantra Team'
        message = f'Hi ,{first_name} thank you for Contact Us. Our team will Contact you shortly with the solution to your query.'
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

        Contact_us.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,about_yourself=about_yourself)
        
        return redirect("home")
