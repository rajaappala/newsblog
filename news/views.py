from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
from datetime import datetime
from django.core.mail import send_mail,EmailMessage
from .tasks import *
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 15)
def index(request):
    try:
        news_items = News.objects.filter(is_published = True).order_by('-published_at')
        last_inserted_item = News.objects.filter(is_published = True).last()
        return render(request, 'index.html', {'news_items':news_items, 'last_item_id': last_inserted_item.id})
    except:
        return render(request, '500.html', {'msg':"Something went wrong"})

def fetch_latest_posts(request, last_item_id):
    try:
        if News.objects.filter(is_published = True, id__gt = last_item_id).exists():
            return JsonResponse({'success': True, 'msg': 'new posts found!'}, status=200)
        else:
            return JsonResponse({'success': False, 'msg': 'No new posts found!'}, status=200)
    except:
        return JsonResponse({'msg': 'Something went wrong'}, status=500)

def view_post(request, post_id):
    try:
        post = News.objects.filter(is_published=True, id=int(post_id)).first()
        return render(request, 'view_post.html', {'post': post})
    except:
        return JsonResponse({'msg':'Post Not Found'}, status=404)


def publish(request):
    try:
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
                
                #purging the cache on each new publish
                cache.clear()

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
        notify_admin_via_email.delay(message)
        return JsonResponse({'msg': 'Notification sent successfully'}, status=200)
    except:
        return JsonResponse({'msg': 'Something went wrong'}, status=500)