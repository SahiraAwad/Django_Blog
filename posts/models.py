from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length= 1000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return self.title
