from django.db import models

class Recipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_dis = models.TextField()
    receipe_img = models.ImageField(upload_to='recipes/')


    
