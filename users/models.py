from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics",null=True,blank=True,default='guest-user.jpg')
    website  =models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)

    def __str__(self):
        return self.user.username
