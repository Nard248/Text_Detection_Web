from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50)
    Img = models.ImageField(upload_to='Image_folder/Upload_image')
