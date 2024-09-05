from django.db import models

# Create your models here.
class CreateTask(models.Model):
    class Meta:
        ordering = ["-date"]
    article = models.CharField(max_length=100)
    body = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todo/', blank=True, null=True)