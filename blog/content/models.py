from django.db import models
from django.utils import timezone
import os
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
def save_image(obj, filename):
    return f"blogs/{obj.id}/{filename}"


class BlogPost(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False, unique=True)
    date = models.DateField(blank=False, null=False, default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True, upload_to=save_image)

    class Meta:
        ordering = ("-date",)


@receiver(models.signals.post_delete, sender=BlogPost)
def delete_file(sender, instance, *args, **kwargs):
    if instance.thumbnail and os.path.isfile(instance.thumbnail.path):
        os.remove(instance.thumbnail.path)
