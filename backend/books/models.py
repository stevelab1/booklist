from django.db import models
from authors.models import Author
from ckeditor.fields import RichTextField


class Book(models.Model):
    class Section(models.TextChoices):
        SCI_FI_CLASSICS = 'Sci Fi Classics'
        LITERARY_CLASSICS = 'Literary Classics'
        HORROR = 'Horror'
        FANTASY = 'Fantasy'
        MISCELLANEOUS = 'Miscellaneous'

    
    class Mood(models.TextChoices):
        PURE_ESCAPISM = 'Pure escapism'
        SCARY = 'Scary'
        TENSE = 'Tense'
        LAUGH_OUT_LOUD = 'Laugh out loud'
        ROLLERCOASTER = 'Rollercoaster'
        HARD_TO_SAY = 'Hard to say'


    author = models.ForeignKey(Author, related_name='books_by_author', on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    rich_content = RichTextField(blank=True, null=True)
    section = models.CharField(max_length=50, choices=Section.choices)
    mood = models.CharField(max_length=50, choices=Mood.choices)
    featured = models.BooleanField(default=False)
    free_version_available = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos', blank=True)
    file_pdf_etc = models.FileField(upload_to='files', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title