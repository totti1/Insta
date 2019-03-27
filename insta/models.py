from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length =100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user).first()
        return profile
    
    @classmethod
    def get_many_profiles(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    @classmethod
    def get_profile_id(cls, user):
        profile = cls.objects.get(pk =user)
        return profile

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True)
    name = models.CharField(max_length =60)
    caption = models.TextField()
    likes = models.IntegerField(null=True)
    profile = models.ForeignKey(Profile, null=True)
    user = models.ForeignKey(User, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def get_images_by_id(cls, id):
        images = cls.objects.filter(profile = id).all()
        return images

    @classmethod
    def update_image(cls, my_id, like):
        image = cls.objects.filter(id = my_id).update(likes =like)
        return image

class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True)
    date_followed = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_followers(cls, user):
        followers = cls.objects.filter(user=user).first()
        return followers