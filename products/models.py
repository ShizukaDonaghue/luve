from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    A model for the category of product
    """

    class Meta:
        verbose_name_plural = 'Categories'

    CATEGORY_CHOICES = (
        ('Baby & Kids', 'Baby & Kids'),
        ('Body', 'Body'),
        ('Face', 'Face'),
        ('Lips', 'Lips'),
        ('After Sun', 'After Sun'),
    )

    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    display_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.display_name


class Brand(models.Model):
    """
    A model for the brand of product
    """

    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.display_name


class Type(models.Model):
    """
    A model for the application type of product
    """

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

    def get_friendly_name(self):
        return self.display_name


class Product(models.Model):
    """
    A model for all products
    """
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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
