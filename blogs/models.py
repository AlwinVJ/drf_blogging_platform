from django.db import models
from drfblog import settings

# Create your models here.
# Category model
class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category
    
# Blog model
class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'), ('published','Published')
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    
    short_description = models.TextField(max_length=500)
    blog_content = models.TextField()
    
    featured_image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True
    )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title