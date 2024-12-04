from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.title
