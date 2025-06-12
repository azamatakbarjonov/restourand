from django.shortcuts import render, redirect
from .forms import SignupForm

def contact_view(request):
    forms = SignupForm()  # Faol forma
    if request.method == 'POST':
        forml = SignupForm(request.POST)
        if forml.is_valid():
            forml.save()
            return redirect('home')  # Formani saqlab, home sahifasiga qaytish


    context = {
        'forms': forms,  
    }
    return render(request, 'contact.html', context)



