from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('normal', 'Normal'),
        ('organic', 'Organic'),
    ]
    
    SUB_CATEGORY_CHOICES = [
        ('anaj', 'Anaj (Grains)'),
        ('fruits', 'Fruits'),
        ('vegetables', 'Vegetables'),
    ]
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    category_type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    
    def __str__(self):
        return f"{self.get_category_type_display()} - {self.get_sub_category_display()}"
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.category_type}-{self.sub_category}")
        super().save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True)
    is_featured = models.BooleanField(default=False)
    unit = models.CharField(max_length=20, default='kg', help_text='Unit of measurement (kg, g, piece)')
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='farmers/')
    products = models.ManyToManyField(Product, related_name='farmers', blank=True)
    
    def __str__(self):
        return self.name
