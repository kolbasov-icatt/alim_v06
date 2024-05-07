from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('foodstyles/', views.foodstyles, name='foodstyles'),
    
    # country urls
    path('country/<int:id>/', views.country_detail, name='country_detail'),
    path('country/<int:id>/gender/<str:gender>/', views.country_gender_detail, name='country_gender_detail'),
    path('country/<int:id>/generation/<str:generation>/', views.country_generation_detail, name='country_generation_detail'),
    path('country/<int:id>/resp/<str:resp>/', views.country_resp_detail, name='country_resp_detail'),
    
    # food
    path('food/<int:id>/', views.food_detail, name='food_detail'),
    # for testing
    path('foodtest/<int:id>/', views.food_detail_test, name='food_detail_test'),

    path('test/', views.test, name='test'),
]