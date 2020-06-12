from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='images_created',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
        blank=True,allow_unicode=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,
        db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    total_likes = models.PositiveIntegerField(db_index=True,
                                              default=0)

    filter = models.CharField(max_length=60,default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title,allow_unicode=True)

        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    image = models.ForeignKey(Image,
            on_delete=models.CASCADE,
            related_name='comments')
    user = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='comments')
    active = models.BooleanField(default=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)