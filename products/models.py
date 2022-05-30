from django.db import models
from django.contrib.auth import get_user_model

# print(get_user_model())
CATEGORIES = (
    ('0', 'Computer accessories'),
    ('1', 'Laptops'),
    ('2', 'Tablets'),
    ('3', 'Smartphone'),
    ('4', 'Printers'),

)


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    image_link = models.URLField(max_length=555)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
