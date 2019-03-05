from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings #引入settings中自定义的参数，此处为BLOGS_NUMBER_EACH_PAGE，即每页几篇博客参数

# Create your views here.

def blog_detail(request, blog_pk):
    context = {}
    context['Blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog_detail.html', context)


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator =Paginator(blogs_all_list, settings.BLOGS_NUMBER_EACH_PAGE)  #每页BLOGS_NUMBER_EACH_PAGE篇文章
    page_now = request.GET.get('page', 1)  #获取当前页码
    page_of_blogs = paginator.get_page(page_now)
    page_range = [x for x in range(int(page_now)-2, int(page_now)+3) if 0< x <= paginator.num_pages]
    if page_range[0] - 1 >= 2:
        page_range.insert(1, '...') #分页中增加省略号
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range[0] = 1
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog_list.html', context)

def blog_type_search(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_all_list, settings.BLOGS_NUMBER_EACH_PAGE)  # 每页BLOGS_NUMBER_EACH_PAGE篇文章
    page_now = request.GET.get('page', 1)  # 获取当前页码
    page_of_blogs = paginator.get_page(page_now)
    page_range = [x for x in range(int(page_now) - 2, int(page_now) + 3) if 0 < x <= paginator.num_pages]
    if page_range[0] - 1 >= 2:
        page_range.insert(1, '...')  # 分页中增加省略号
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range[0] = 1
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    context['blog_type'] = blog_type

    return render_to_response('blog_type_search.html', context)