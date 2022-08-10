from django.shortcuts import render
from .models import Post


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on') # все объекты из базы данных Post
    context = {
        'posts':posts
    } #создали словарь, чтобы потом передать его на страницу
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk = pk)#вызываем конкретный объект по уникальному рк(первичный ключ, ID из таблицы базы данных
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)
