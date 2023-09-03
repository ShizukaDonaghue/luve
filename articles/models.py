from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .validators import textfield_not_empty


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='article_posts'
    )
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[textfield_not_empty])
    image = CloudinaryField('image', default='v1686206490/placeholder')
    likes = models.ManyToManyField(
        User,
        related_name='article_likes',
        blank=True
    )

    class Meta:
        """
        Ordering of articles by their creation dates in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """ Returns the article title as a string """
        return self.title

    def number_of_likes(self):
        """ Returns the total number of likes for each article """
        return self.likes.count()
