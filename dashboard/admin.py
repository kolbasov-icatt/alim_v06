from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Area)
admin.site.register(Gender)
admin.site.register(RespAcq)
admin.site.register(Generation)
admin.site.register(Frequency)
admin.site.register(GrowthRate)
admin.site.register(FoodCat)
admin.site.register(FoodStyle)
admin.site.register(UserProfile)


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    list_display = ['id_num', 'country', 'area', 'foodstyle', 'food', 'frequency', 'growthrate']
    list_filter = ['id_num', 'country', 'area', 'foodstyle', 'food', 'frequency', 'growthrate']
    #search_fields = ['title', 'body']
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ['author']
    #date_hierarchy = 'publish'
    ordering = ['id_num', ]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'food_cat', 'short_name', 'description', 'image']
    list_filter = ['food_cat', 'image' ]




