from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(verbose_name="title of the category", max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField("title of the product", max_length=100, null=False, blank=False)
    price = models.FloatField("price of the product", blank=False, null=False)
    description = models.TextField("description of the product", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category of the product")
    rating = models.FloatField("rating of the product", default=0.0, blank=False)
    image = models.ImageField(upload_to="image_of_products", blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.title}"
    