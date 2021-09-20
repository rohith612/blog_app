from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator

# Tag model for the each post
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption 


# Author model for the each posts
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# Post models need to manage all user posts
class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[
        MinLengthValidator(10)
    ])
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title