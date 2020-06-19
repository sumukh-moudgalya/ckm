from django.db import models

# Create your models here.
class Explores(models.Model):
    name=models.TextField(max_length=180)
    short_desc=models.TextField(max_length=None)
    desc=models.TextField(max_length=None)
    google_map_html=models.TextField(max_length=None,blank=True)
    google_map_link=models.TextField(max_length=None,blank=True)
    dist_from_bang=models.TextField(max_length=None,blank=True)
    dist_from_mys=models.TextField(max_length=None,blank=True)
    dist_from_ckm=models.TextField(max_length=None,blank=True)
    thumbnail=models.ImageField(upload_to='explores',blank=True)
    facebook_link_thumbnail=models.TextField(max_length=None,blank=True)
    rank=models.PositiveIntegerField()
    three_view=models.TextField(max_length=None,blank=True)
    image_1=models.ImageField(upload_to='explores',blank=True)
    image_2=models.ImageField(upload_to='explores',blank=True)
    image_3=models.ImageField(upload_to='explores',blank=True)
    image_4=models.ImageField(upload_to='explores',blank=True)
    image_5=models.ImageField(upload_to='explores',blank=True)
    image_6=models.ImageField(upload_to='explores',blank=True)
    image_7=models.ImageField(upload_to='explores',blank=True)
    image_8=models.ImageField(upload_to='explores',blank=True)
    image_9=models.ImageField(upload_to='explores',blank=True)
    image_10=models.ImageField(upload_to='explores',blank=True)

    def __str__(self):
        return str(self.rank)+":"+self.name





class Hotels(models.Model):
    name=models.TextField(max_length=None)
    desc=models.TextField(max_length=None,blank=False)
    google_link=models.TextField(max_length=None,blank=False)
    thumbnail=models.ImageField(max_length=None,blank=False)

    google_map_html=models.TextField(max_length=None,blank=False)
    rank=models.PositiveIntegerField()
    google_rating=models.TextField(max_length=15)
    veg=models.BooleanField()

    def __str__(self):
        return self.name
