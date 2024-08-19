import os

from typing import List

from django.db import models
from django.conf import settings
from django.core.files import File


class Category(models.Model):
    title = models.CharField(verbose_name="title of the category", max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class ProductImage(models.Model): 
    # I've decided that all image management and product management 
    # will be separate in different forms (that we submit) at the front end.
    # TODO: Rename files when saving
    # TODO: Resize images when saving
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=False)

    def delete(self, **kwargs):
        try:
            os.remove(self.image.path)
        except FileNotFoundError: ...
        return super().delete(**kwargs)


class ProductManager(models.Manager): 
    """Product manager class
    
    Helps us to create product and images of product almost at the same time.
    """
    
    def create(self, **kwargs):
        images = kwargs.pop('images')
        product = Product(**kwargs)
        product.save()
        for image in images:
            ProductImage(image=image['image'], product=product).save()
        return product


class Product(models.Model):
    objects = ProductManager()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField("title of the product", max_length=100, null=False, blank=False)
    price = models.FloatField("price of the product", blank=False, null=False)
    description = models.TextField("description of the product", blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category of the product")
    rating = models.FloatField("rating of the product", default=0.0, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def images(self):
        return ProductImage.objects.filter(product=self)

    @images.setter
    def images(self, images: List[File]): # Set for testing in the shell
        for image in images:
            ProductImage(image=image, product=self).save()

    def delete(self, **kwargs): 
        # For some reasone it doesn't delete images from the settings.MEDIA_ROOT via CASCADE property
        # So I'll just call it explicitly.  
        for image in self.images:
            image.delete()
        return super().delete(**kwargs)

    def __str__(self):
        return f"{self.category} - {self.title}"
    
#     class Meta:
#         abstract = True
    

# class Car(Product):
#     class CarType(models.TextChoices): # Only 5 categories are available
#         A = 'A', 'A'
#         B = 'B', 'B'
#         C = 'C', 'C'
#         D = 'D','D'
#         M = 'M', 'M'
#     registry_sign = models.CharField(max_length=9, null=False)
#     type_of_transport = models.CharField(choices=CarType, max_length=1, null=False)
#     transport_model = models.CharField(null=False)
#     year = models.PositiveSmallIntegerField(null=False)
#     weight = models.PositiveSmallIntegerField(null=False)
#     # And many other characteristics


# class Apartament(Product):
#     class ApartamentType(models.TextChoices):

#     type_of_apartament = models.CharField("")