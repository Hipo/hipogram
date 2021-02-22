from django.db import models


class Post(models.Model):
    image = models.ImageField()
    text = models.TextField()
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now_add=True)
