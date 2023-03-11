from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class ShortCuts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='short_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=250)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    desc = models.TextField(blank=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='short_liked',
                                        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created_at'])
        ]
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
