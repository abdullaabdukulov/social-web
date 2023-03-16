from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image as PilImage
from io import BytesIO
import os


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200,
                            blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    total_likes = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # resize the image
        img = PilImage.open(self.image)
        output = BytesIO()
        img = img.resize((800, 800), PilImage.ANTIALIAS)
        img.save(output, format='JPEG', quality=75)
        output.seek(0)

        # change the imagefield value to be the newly resized image value
        self.image = os.path.basename(self.image.name)
        self.image.save(self.image.name, output, save=False)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])


def pre_save_image_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


models.signals.pre_save.connect(pre_save_image_slug, sender=Image)
