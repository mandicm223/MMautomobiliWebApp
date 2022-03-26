from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        costumer_need = request.POST['costumer_need']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        state = request.POST['state']
        city = request.POST['city']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id , user_id=user_id)
            if has_contacted:
                messages.error(request , "You have already submited inquey for this car !")
                return redirect('/cars/single_car/'+car_id)

        contact = Contact( first_name=first_name , last_name=last_name , user_id=user_id , car_id=car_id , car_title=car_title , 
               costumer_need=costumer_need , email=email , phone=phone , message=message , state=state , city=city )
        

            
        send_mail(
            'Hey you have new inquiry !',
            'New inquiry for the car ' + car_title + ' Please check your admin page.',
            'mandicm223@gmail.com',
            ['cloudiumm@gmail.com'],
            fail_silently=False,
        )

        contact.save()
        messages.success(request , "You're request has been submited and we will reply to you soon .")
        return redirect('/cars/single_car/'+car_id)