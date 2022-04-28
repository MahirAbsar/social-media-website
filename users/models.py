from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    full_name = models.CharField(max_length=300,null=True,blank=True)
    profile_pic = models.ImageField(default='guest-user.jpg',upload_to="profile_pics",null=True,blank=True)
    dob = models.DateTimeField(blank=True,null=True,verbose_name="Date Of Birth")
    description = models.TextField(blank=True,null=True)
    website  =models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    followers = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followers")
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="following")
    follow_date = models.DateTimeField(auto_now_add=True)
