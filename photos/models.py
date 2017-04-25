#from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse



class ImageClass(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
#class ImageClass(models.Model):
    #class_name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photos:product_list_by_category', args=[self.slug])

class Photo(models.Model):
    category = models.ForeignKey(ImageClass, related_name = 'products')
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200, db_index =True)
    photo = models.ImageField(upload_to='./photos/media/photos/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    #boolean to enable or disable the product in the cataloge
    available = models.BooleanField(default=True)
    #stores when the object was created
    created = models.DateTimeField(auto_now_add=True)
    #when the object was last updated
    update = models.DateTimeField(auto_now_add=True)
    features = models.FileField(blank = True , upload_to= './photos/media/features/')


    class Meta:
        ordering = ('-created',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.name

    #check this if error
    def get_absolute_url(self):
        return reverse('photos:product_detail', args=[self.id,self.slug])







