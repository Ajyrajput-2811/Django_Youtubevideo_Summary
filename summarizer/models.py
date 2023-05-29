from django.db import models

class Video(models.Model):
    title = models.CharField( max_length=200)
    youtube_url = models.URLField()
    summary = models.TextField(blank=True,null = True)

    def __str__(self):
      return self.title

