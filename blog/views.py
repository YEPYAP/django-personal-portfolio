from django.shortcuts import render,get_object_or_404
from .models import Project_1

def all_blogs(request):
    projects = Project_1.objects.order_by('-time')[:5]
    return render(request, 'blog/all_blogs.html', {'projects': projects})
def detail(request, blog_id):
    blog = get_object_or_404(Project_1, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})