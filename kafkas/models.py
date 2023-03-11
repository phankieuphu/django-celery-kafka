from django.db import models

# djago signals
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    print("User Created")
    print(instance.name)


@receiver(pre_save, sender=User)
def update_user(sender, instance, **kwargs):
    print("User Updated")
    print(instance.name)
