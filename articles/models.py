from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# Status choices for the Article model
STATUS = (
    (0, 'Save as Draft'),
    (1, 'Publish Now!')
)


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
    content = models.TextField(null=False, blank=False)
    image = ResizedImageField(
        size=[600, None], quality=75,
        upload_to='articles/',
        force_format='WEBP',
        blank=False, null=False,
        default='Placeholder'
    )
    status = models.IntegerField(choices=STATUS, default=0)
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
