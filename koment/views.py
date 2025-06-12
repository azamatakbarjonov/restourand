from django.shortcuts import render
from service.models import Service

def test_koment(request):
    service =  Service.objects.all()

    contxt = {
        'services': service
    }
    return render(request, 'koment.html', contxt)
