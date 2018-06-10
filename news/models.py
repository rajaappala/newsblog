from django.db import models

# Create your models here.
class News(models.Model):
    class Meta:
        db_table = 'news'
        default_permissions = ()
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 200, null=True)
    author = models.CharField(max_length = 200, null=True)
    content = models.TextField(null=True)
    synopsis = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_at = models.DateTimeField(null=True)

class Comments(models.Model):
    class Meta:
        db_table = 'news'
        default_permissions = ()
    id = models.AutoField(primary_key = True)
    comment = models.CharField(max_length = 500, null=True)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
