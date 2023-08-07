from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)], null=False, blank=False)
    image_name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.title
