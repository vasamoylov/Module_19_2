from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


# Create your views here.

def new_post(request):
    post = Post.objects.all().order_by('-create_date')
    per_page = request.GET.get('per_page', 3)
    paginator = Paginator(post, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj, 'per_page': per_page})
