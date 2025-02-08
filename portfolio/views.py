from django.shortcuts import render
from .models import Project, About, Skills_Value, Skills_About, Title

# Create your views here.

def home(request):
    projects = Project.objects.all()
    about = About.objects.all()
    skills_about = Skills_About.objects.all()
    skills_value = Skills_Value.objects.all().order_by('-value')
    titles=Title.objects.all()
    context = {
        "projects" : projects,
        "about" : about,
        "skill_about" : skills_about,
        "skill_value" : skills_value,
        "titles" : titles,
        }
    return render(request, 'portfolio/home.html', context)
def login(request):
    return render(request, 'portfolio/login.html')