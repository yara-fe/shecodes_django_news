from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    image = models.URLField(max_length=200, null=True) #Add a new field to have images
    pub_date = models.DateTimeField()
    content = models.TextField()

