from django.shortcuts import render
from about.models import Chef

def chef_ma(request):
    chef = Chef.objects.all()

    context = {
        'chef': chef
    }
    return render(request, 'uzz.html', context)
