from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_global_request.middleware import get_request


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_project_dir/<filename>
    request = get_request()
    project_name_obj = Profile.objects.get(user_id=request.user.id)
    return '{0}/{1}'.format(project_name_obj.project_name, filename)


class Photo(models.Model):
    project = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to=user_directory_path)
    istagged = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        request = get_request()
        project_name_obj = Profile.objects.get(user_id=request.user.id)
        self.project = project_name_obj.id
        super().save(*args, **kwargs)


class Annotate(models.Model):
    coordinates = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
