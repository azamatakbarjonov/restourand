from django.shortcuts import render, redirect
# from .models import Booking
from .forms import BookingForm


def book_view(request):
    forms = BookingForm()  # Faol forma
    if request.method == 'POST':
        forml = BookingForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect('home')  # Formani saqlab, home sahifasiga qaytish
    context = {
        'forms': forms,  
    }
    return render(request, 'booking.html', context)

