from django.db import models
from ckeditor.fields import RichTextField



class Author(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    rich_content = RichTextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name