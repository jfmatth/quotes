from django.db import models

from taggit.managers import TaggableManager

# Create your models here.
class Quote(models.Model):
    quote = models.TextField(blank=False)

    tags = TaggableManager()
    
    def __str__(self):
        return f'{self.quote} - {u", ".join(o.name for o in self.tags.all()) }'

