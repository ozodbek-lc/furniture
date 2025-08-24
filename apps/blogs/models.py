from django.db import models
from django.contrib.auth.models import User



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BlogCategory(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Blog Kategoriya"
        verbose_name_plural = "Blog Kategoriyalar"

    def __str__(self):
        return self.name


class Blog(BaseModel):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="blogs")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/images/", blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"

    def __str__(self):
        return self.title
