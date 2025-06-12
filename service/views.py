from django.shortcuts import render
from .models import Service

def service_view(request):
    service = Service.objects.all()
    context = {
        'services': service
    }
    return render(request, 'service.html', context)



