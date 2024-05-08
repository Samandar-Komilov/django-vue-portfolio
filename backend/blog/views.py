from django.shortcuts import render
from django.views import View
from .models import Project


class HomeView(View):
    def get(self, request):
        context = {
        }
        return render(request, "index.html", context)
    

class AboutView(View):
    def get(self, request):
        context = {

        }
        return render(request, "about.html", context)
    

class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            "projects": projects,
        }
        return render(request, "projects.html", context)
    

class ProjectDetailView(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        context = {
            "project": project
        }
        return render(request, "detail.html", context)
    

class BlogView(View):
    def get(self, request):
        context = {

        }
        return render(request, "blog.html", context)