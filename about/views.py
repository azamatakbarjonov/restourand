from django.shortcuts import render
from .models import About, Section, Aboutmain, Chef

def about_view(request):
    about = About.objects.all()
    section = Section.objects.all()
    chef = Chef.objects.all()
    aboutmain = Aboutmain.objects.first()


    context = {
        'about' : about,
        'section' : section,
        'aboutm' : aboutmain,
        'chef' : chef,
    }
    return render(request, 'about.html', context)
