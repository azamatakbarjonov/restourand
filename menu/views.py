from django.shortcuts import render
from .models import Menu

def menu_view(request):
    menu = Menu.objects.all()
    context = {
        'menu': menu
    }
    return render(request, 'menu.html', context)



