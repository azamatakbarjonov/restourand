from django.shortcuts import render,redirect
from .models import Homehead, Secbut
from about.models import  About, Section, Aboutmain, Chef
from service.models import Service
from booking.forms import BookingForm

def home_view(request):
    home = Homehead.objects.first()  # Homehead modelidan ma'lumot olish
    about = About.objects.all()
    secbut = Secbut.objects.all()
    section = Section.objects.all()
    chef = Chef.objects.all()
    aboutmain = Aboutmain.objects.first()
    service = Service.objects.all()
    forms = BookingForm()  # Faol forma
    if request.method == 'POST':
        forml = BookingForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect('home')  # Formani saqlab, home sahifasiga qaytish

    context = {
        'home': home,
        'about' : about,
        'section' : section,
        'aboutm' : aboutmain,
        'chef' : chef,
        'services': service,
        'secbut': secbut,
        'forms': forms,
    }
    return render(request, 'index.html', context)  # home sahifasini qaytaradi


