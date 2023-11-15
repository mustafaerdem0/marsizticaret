from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
# Create your models here.
def generate_filename(self, filename):
    url = "uploads/image/%s/%s" % (self.title, filename)
    return url


# model defination

class Product(models.Model):
    title = models.CharField(("Ürün Başlığı"), max_length=50)
    slug = AutoSlugField(populate_from='title')
    image = models.ManyToManyField("main_app.Image", verbose_name=("Ürün Resmi"),blank=True)
    price = models.PositiveIntegerField(("Ürün Fiyatı"))
    description = models.TextField(("Ürün Açıklaması"))
    size = models.ManyToManyField("main_app.Size", verbose_name=("Beden"))
    color  = models.ManyToManyField("main_app.Color", verbose_name=("Renk"))
    categories = models.ManyToManyField("main_app.Categories", verbose_name=("Kategori"),related_name="productcategory")
    gender = models.ManyToManyField("main_app.Gender", verbose_name=("Cİnsiyet"))
    is_active = models.BooleanField(("ürün aktifmi"),default=True)
    def __str__(self) :
        return self.title
    def p_category_names(self):
        category_list = []
        for category in self.categories.all():
            category_list.append(category)
        print("categorylst",category_list)
        return category_list
       

class Image(models.Model):
    title = models.CharField(("Ürün Resmi İsmi"), max_length=50,blank=True)
    image = models.FileField(("Ürün resmi"), upload_to=generate_filename, max_length=100)
    def __str__(self):
        return self.title
class Size(models.Model):
    title = models.CharField(("Ürün Bedenli"), max_length=15)
    def __str__(self) :
        return self.title

class Color(models.Model):
    title = models.CharField(("Ürün rengi"), max_length=50)
    color = ColorField(default='#FF0000')
    def __str__(self) :
        return self.title
class Categories(models.Model):
    title = models.CharField(("Ürün Kategori"), max_length=50)
    slug = AutoSlugField(populate_from='title')
    def __str__(self) :
        return self.title
    def category_name(self):
        return self.title
class Gender(models.Model):
    title = models.CharField(("Cinsiyet"), max_length=50)
    def __str__(self) :
        return self.title