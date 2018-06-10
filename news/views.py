from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    try:
        news_items = News.objects.filter(is_published = True)
        return render(request, 'index.html', {'news_items':news_items})
    except:
        return render(request, '500.html', {'msg':"Something went wrong"})

# def fetch_new_posts(request, last):
#     try:
#         if News.objects.filter(is_published = True, published_at__gte = last_post)

def view_post(request, post_id):
    try:
        # import pdb;pdb.set_trace()
        post = News.objects.filter(is_published=True, id=int(post_id)).first()
        return render(request, 'view_post.html', {'post': post})
    except:
        return JsonResponse({'msg':'Post Not Found'}, status=404)


def publish(request):
    try:
        # import pdb; pdb.set_trace()
        if request.method == 'POST':
            title = request.POST.get('title', '')
            author = request.POST.get('author', '')
            synopsis = request.POST.get('synopsis', '')
            content = request.POST.get('content', '')
            if all([title,author,synopsis,content]):
                news = News()
                news.title = title
                news.author = author
                news.content = content
                news.synopsis = synopsis
                news.is_published = True
                news.published_at = datetime.now()          
                news.save()
                return render(request, 'publish_form.html', {'msg': 'content published successfully'})
            else:
                return JsonResponse({'msg': 'all fields are mandotory'}, status=200)
        elif request.method == 'GET':
            return render(request, 'publish_form.html')
    except:
        return JsonResponse({'msg': 'Something went wrong'}, status=500)

def notify_admin(request):
    try:
        message = request.POST.get('email_content', '')
        return JsonResponse({'msg': 'Notification sent successfully'}, status=200)
    except:
        return JsonResponse({'msg': 'Something went wrong'}, status=500)