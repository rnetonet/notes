from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name="images_created", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    users_likes = models.ManyToManyField(get_user_model(), related_name="images_liked", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
