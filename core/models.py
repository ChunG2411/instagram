from django.db import models
from django.contrib.auth import get_user_model
from random import choices

# Create your models here.
User = get_user_model()
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.pk)


class Comment(models.Model):
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/comment', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-commented_on']
    
    def __str__(self):
        return f"{self.user}-->{self.post.id}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-->{self.post.id}"


class Follow(models.Model):
    user = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name="followed", on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-followed_on']
    
    def __str__(self):
        return f"{self.user}-->{self.followed}"
