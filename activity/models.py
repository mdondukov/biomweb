from django.db import models

from pages.models import Base


# Direction class
class Direction(Base):
    content = models.TextField(blank=True, help_text='Enter the page content')

    def __str__(self):
        return self.title
