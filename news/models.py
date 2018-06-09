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
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)