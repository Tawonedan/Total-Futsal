from django.shortcuts import render
from projects.models import Project


def fields_catalog(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "fields/fields_lists.html", context)
