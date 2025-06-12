from django.shortcuts import render
from .models import Base_main
from about.models import Aboutmain


def base_view(request):
    main = Base_main.objects.first()
    about = Aboutmain.objects.first()


    cxt = {
        'main': main,
        'aboutm': about,
    }
    return render(request, 'base.html', cxt)
