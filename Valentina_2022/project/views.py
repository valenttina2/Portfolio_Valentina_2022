from django.shortcuts import render
from .models import Project
# Create your views here.
def project_index(request):
    projects = Project.objects.all() #создали переменную, в нее излекли все объекты из базы данных Project
    context = {
        'projects':projects
    } #создали словарь, чтобы потом передать его на страницу
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk = pk)#вызываем конкретный объект по уникальному рк(первичный ключ, ID из таблицы базы данных
    context = {
        'project': project
    }
    return render(request, 'project_details.html', context)