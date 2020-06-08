from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField

User._meta.get_field('email').__dict__['_unique'] = True

class Profile(models.Model):
    user = AutoOneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True,null=True,default="من حال نداشتم این قسمت رو پر کنم.")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True,null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
        related_name='rel_from_set',
        on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
        related_name='rel_to_set',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
        db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} ' \
               'ws {}'.format(self.user_from,
                                      self.user_to)

User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))