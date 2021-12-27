from django.db import models

# Create your models here.
class Thread(models.Model):
    thread_title = models.CharField(max_length=80)
    thread_date = models.DateTimeField('date published')
    def __str__(self):
        return self.thread_title

class Post(models.Model):
    post_text = models.CharField(max_length=500)
    post_date = models.DateTimeField('date published')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    def __str__(self):
        return self.post_text
