from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    image = models.ImageField(default="guest-user.jpg",upload_to='post_images',null=True,blank=True)
    caption = models.CharField(max_length=2000,null=True,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-post_date']
    def __str__(self):
        return self.author.username

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="liked_post")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="liker")

    def __str__(self):
        return self.user.username
