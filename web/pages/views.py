from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def home(request):
    all_cars = Car.objects.order_by('-created_date')
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    teams = Team.objects.all()
    model_search = Car.objects.values_list('model' , flat=True).distinct()
    city_search = Car.objects.values_list('city' , flat=True).distinct()
    year_search = Car.objects.values_list('year' , flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style' , flat=True).distinct()

    data = {
        'all_cars': all_cars,
        'featured_cars': featured_cars,
        'teams': teams,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request , "pages/home.html" , data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams
    }
    return render(request , "pages/about.html" , data)

def services(request):
    return render(request , "pages/services.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        subject_revorked = 'Hey you have new message regarding subject:' + subject
        body_revorked = "Hey my name is:" + name + ' My email:' + email + ' My phone' + phone + ' Message:' + message
        
        send_mail(
            subject_revorked,
            body_revorked,
            'mandicm223@gmail.com',
            ['cloudiumm@gmail.com'],
            fail_silently=False,
        )

        messages.success(request , "Vaša poruka je poslata. Odgovorićemo Vam uskoro. ")
        return redirect('contact')

    return render(request , "pages/contact.html")