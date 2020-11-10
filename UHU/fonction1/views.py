from django.shortcuts import render
# from .models import Post
# # Create your views here.
# def classification(request):
#    Data = {'Posts': Post.objects.all().order_by('-date')}
#    return render(request, 'blog/blog.html', Data)
def fonction1(request):
    return render(request, 'pages/fonction1.html')
