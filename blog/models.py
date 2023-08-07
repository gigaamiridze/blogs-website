from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    excerpt = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)], null=False, blank=False)
    image_name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')

    def __str__(self):
        return self.title
