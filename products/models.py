from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ A model for the category of product """

    class Meta:
        verbose_name_plural = 'Categories'

    CATEGORY_CHOICES = (
        ('baby_kids', 'Baby & Kids'),
        ('body', 'Body'),
        ('face', 'Face'),
        ('lips', 'Lips'),
        ('after_sun', 'After Sun'),
    )

    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    display_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Brand(models.Model):
    """ A model for the brand of product """

    name = models.CharField(max_length=50)

    class Meta:
        """ Ordering of brands in alphabetical order """
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(models.Model):
    """ A model for the application type of product """

    APPLICATION_TYPES = (
        ('Lotion', 'Lotion'),
        ('Spray', 'Spray'),
        ('Stick', 'Stick'),
        ('Roll-On', 'Roll-On'),
    )

    name = models.CharField(max_length=30, choices=APPLICATION_TYPES)
    display_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """ A model for all products """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=60, null=True,
                           blank=True, unique=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])
    image = CloudinaryField('image', default='v1686206490/placeholder')

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """ A model for product reviews """

    RATINGS = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=RATINGS, default=3)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ Ordering of creation date in ascending order """
        ordering = ['created_on']

    def __str__(self):
        """ Returns review content and user name """
        return f"Review {self.content} by {self.name}"

    def date_format_created_on(self):
        """ Date formatting for creation dates """
        return self.created_on.strftime('%d %b %y')
