from django.db import models
from tinymce import HTMLField
from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill


# Simple abstract class.
class Base(models.Model):
    title = models.CharField(max_length=255)

    slug = models.SlugField(default='', unique=True)

    PUB_STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('a', 'Archive'),
    )

    status = models.CharField(verbose_name='Status',
                              help_text='Select the post status',
                              max_length=1,
                              choices=PUB_STATUS,
                              default='d')

    summary = models.TextField(max_length=501, blank=True, help_text='Enter the brief description')

    class Meta:
        abstract = True


# Page class
class Page(Base):
    head_image = ProcessedImageField(blank=True,
                                     help_text='Upload the image file',
                                     upload_to='pages/%Y/%m/%d',
                                     # processors=[ResizeToFill(1200, 200)],
                                     format='JPEG',
                                     options={'quality': 70})

    content = HTMLField(blank=True, help_text='Enter the page content')

    def __str__(self):
        return self.title
