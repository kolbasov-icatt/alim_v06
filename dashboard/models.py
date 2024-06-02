from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Country(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    color = models.CharField(max_length=25, blank=True, null=True)
    border_color = models.CharField(max_length=25, blank=True, null=True)
    color_empty = models.CharField(max_length=25, blank=True, null=True)
    border_color_empty = models.CharField(max_length=25, blank=True, null=True)
    color2 = models.CharField(max_length=25, blank=True, null=True)
    border_color2 = models.CharField(max_length=25, blank=True, null=True)
    color_empty2 = models.CharField(max_length=25, blank=True, null=True)
    border_color_empty2 = models.CharField(max_length=25, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('dashboard:country_detail', args=[self.id])
    
class Area(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    order = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title
    
class Gender(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    order = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.title

class Generation(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    order = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class RespAcq(models.Model):  # responsabili acquisti
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class Frequency(models.Model):
    title = models.CharField(max_length=30)
    cat = models.CharField(max_length=20, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    times_per_month = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class GrowthRate(models.Model):
    title = models.CharField(max_length=20)
    value = models.IntegerField(blank=True, null=True)  # +1 for growth, 0 for no change, -1 for decline
    order = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class FoodStyle(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title

class FoodCat(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(default='Description', blank=True, null=True)
    def __str__(self):
        return self.title

class Food(models.Model):
    title = models.CharField(max_length=70)
    short_name = models.CharField(max_length=70, blank=True, null=True)
    slug = models.SlugField(max_length=70)
    food_cat = models.ForeignKey(FoodCat, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_background = models.ImageField(upload_to='images/', blank=True, null=True)
    
    is_visible = models.BooleanField(default=False)
    is_product = models.BooleanField(default=True)
    # colors for charts
    color = models.CharField(max_length=25, default='rgba(0, 107, 162, 0.5)')
    border_color = models.CharField(max_length=25, default='rgba(0, 107, 162, 1)')
    color_empty = models.CharField(max_length=25, default='rgba(152, 218, 255, 0.1)')
    border_color_empty = models.CharField(max_length=25, default='rgba(152, 218, 255, 0)')
    color2 = models.CharField(max_length=25, default='rgba(62, 188, 210, 0.5)')
    border_color2 = models.CharField(max_length=25, default='rgba(62, 188, 210, 1)')
    color_empty2 = models.CharField(max_length=25, default='rgba(152, 218, 255, 0.1)')
    border_color_empty2 = models.CharField(max_length=25, default='rgba(152, 218, 255, 0)')
    def __str__(self):
        return self.title
    
class Respondent(models.Model):
    id_num = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    resp = models.ForeignKey(RespAcq, on_delete=models.CASCADE)
    foodstyle = models.ForeignKey(FoodStyle, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default='')
    frequency = models.ForeignKey(Frequency, on_delete=models.CASCADE, blank=True, null=True)
    growthrate = models.ForeignKey(GrowthRate, on_delete=models.CASCADE, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visible_foods = models.ManyToManyField(Food, blank=True, null=True)
    visible_foodstyles = models.ManyToManyField(FoodStyle, blank=True, null=True)

    def __str__(self):
        return self.user.username

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.userprofile.save()