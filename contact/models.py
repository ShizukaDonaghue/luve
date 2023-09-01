from django.db import models


class Contact(models.Model):
    """ A model for contact messages """

    QUERY_TYPES = [
        ('', 'Query Type *'),
        ('Product Query', 'Product Query'),
        ('Order Query', 'Order Query'),
        ('Returns', 'Returns'),
        ('Other', 'Other')
        ]

    query_type = models.CharField(
        max_length=50, choices=QUERY_TYPES,
        null=False, blank=False,
    )
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Display messages by date in descending order"""
        ordering = ['-date']

    def __str__(self):
        return f'Message from {self.email}'
