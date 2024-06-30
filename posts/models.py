from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField
    image = models.ImageField(upload_to="images/")
    aura = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
