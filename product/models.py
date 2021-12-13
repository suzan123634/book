from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='category_imae')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Brand(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class UnitMeasure(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    internal_reference = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    sales_price = models.FloatField()
    cost_price = models.FloatField()
    on_hand = models.IntegerField()
    image = models.ImageField(upload_to='product_image')
    slug = models.SlugField(max_length=250)
    unit_measure = models.ForeignKey(UnitMeasure ,on_delete=models.CASCADE)
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag_short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = "Images"