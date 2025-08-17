from django.db import models

# Create your models here.

class Genre(models.Model):
    name=models.CharField(unique=True,max_length=50,null=True)

    def __str__(self):
        return f"{self.name}"


class TimeStempModel:
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Content(TimeStempModel):
    genres = models.ManyToManyField(Genre, related_name='contents')
    artist = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    clip_url = models.URLField(null=True, blank=True)
    duration = models.PositiveSmallIntegerField(help_text='Second')
    release_date = models.DateField()