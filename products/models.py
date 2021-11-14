from django.db import models
from django.utils.text import slugify

# Create your models here.

UNIT_CHOICES = (
    ("KG", "kg"),
    ("LTR", "Ltr"),
    ("GM", "Gm"),
    ("ML", "mL"),
)


class Product(models.Model):
    name = models.CharField(max_length=50,  null=True, blank=True)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, null=True, blank=True)
    amount = models.IntegerField()
    unit_price = models.FloatField()
    total_stock = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, default='banner-6.png')
    slug = models.SlugField(null=False, unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    