from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'dashboard'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('foodstyles/', views.foodstyles, name='foodstyles'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('403/', views.custom_403_view, name='403_forbidden'),

    # country urls OLD
    path('country_old/<int:id>/', views.country_detail, name='country_detail_old'),
    path('country/<int:id>/gender/<str:gender>/', views.country_gender_detail, name='country_gender_detail'),
    path('country/<int:id>/generation/<str:generation>/', views.country_generation_detail, name='country_generation_detail'),
    path('country/<int:id>/resp/<str:resp>/', views.country_resp_detail, name='country_resp_detail'),
    
    # country urls NEW
    path('country/<int:id>/', views.country_detail_mobile, name='country_detail'),


    # food
    path('food/<int:id>/', views.food_detail, name='food_detail'),

    # foodstyle
    path('foodstyle/<int:id>/', views.foodstyle_detail, name='foodstyle_detail'),


    # for testing
    path('foodtest/<int:id>/', views.food_detail_test, name='food_detail_test'),

    path('test/', views.test, name='test'),
]