from django.shortcuts import render, get_object_or_404
from .models import FoodStyle, Country, Food, Gender, Generation, Area, RespAcq, Respondent, FoodCat
from django.db.models import Count, Q, F, Case, When, Value, CharField, Avg
from .utils import context_country, context_food, context_foodstyle
from django.http import HttpResponseForbidden



def homepage(request):
    foodstyles = FoodStyle.objects.all().order_by('order')
    foods = Food.objects.all()
    countries = Country.objects.all()
    foodcats = FoodCat.objects.all()

    context = {
        'foodstyles': foodstyles,
        'foodcats': foodcats,
        'foods': foods,
        'countries': countries,
    }
    return render(request, 'dashboard/index.html', context)

def test(request):
    foodstyles = FoodStyle.objects.all()
    countries = Country.objects.all()

    respondents_query = Respondent.objects.all()

    # Aggregate the counts of each foodstyle
    foodstyle_counts = respondents_query.values('foodstyle__title').annotate(count=Count('foodstyle')).order_by('foodstyle')
    # Calculate the total count of all foodstyles
    total_count = sum(item['count'] for item in foodstyle_counts)

    # Calculate the percentage of each foodstyle
    labels = [item['foodstyle__title'] for item in foodstyle_counts]
    percentages = [(item['count'] / total_count * 100) for item in foodstyle_counts]

    context = {
        'foodstyles': foodstyles,
        'countries': countries,
        'respondents': respondents_query,
        'labels': labels,
        'data_values': percentages,  # Note that we're passing percentages here
    }
    return render(request, 'dashboard/test.html', context)

def country_detail_mobile(request, id):
    country = get_object_or_404(Country, id=id)
    respondents_query = Respondent.objects.filter(country=country)
    context = context_country(country, respondents_query)

    return render(request, 'dashboard/country_detail.html', context)



def country_detail(request, id):
    country = get_object_or_404(Country, id=id)
    respondents_query = Respondent.objects.filter(country=country)
    context = context_country(country, respondents_query)

    return render(request, 'dashboard/detail.html', context)

def country_gender_detail(request, id, gender):
    country = get_object_or_404(Country, id=id)
    respondents_query = Respondent.objects.filter(country=country, gender__title=gender)
    context = context_country(country, respondents_query)
    context['gender'] = gender
    return render(request, 'dashboard/country/country_gender_detail.html', context)

def country_generation_detail(request, id, generation):
    country = get_object_or_404(Country, id=id)
    respondents_query = Respondent.objects.filter(country=country, generation__title=generation)
    context = context_country(country, respondents_query)
    context['generation'] = generation
    return render(request, 'dashboard/country/country_generation_detail.html', context)

def country_resp_detail(request, id, resp):
    country = get_object_or_404(Country, id=id)
    respondents_query = Respondent.objects.filter(country=country, resp__title=resp)
    context = context_country(country, respondents_query)
    context['resp'] = resp
    return render(request, 'dashboard/country/country_resp_detail.html', context)


def food_detail_test(request, id):
    food = get_object_or_404(Food, id=id)
    foods = Food.objects.all()
    respondents_query = Respondent.objects.filter(food=food)
    context = context_food(food, respondents_query)
    context['foods'] = foods

    return render(request, 'dashboard/food_detail_test.html', context)

def food_detail(request, id):
    food = get_object_or_404(Food, id=id)
    if not food.is_visible:
        return HttpResponseForbidden("Sorry, you do not have access to this page.")

    foods = Food.objects.all()
    respondents_query = Respondent.objects.filter(food=food)
    context = context_food(food, respondents_query)
    context['foods'] = foods

    return render(request, 'dashboard/food_detail.html', context)

def foodstyle_detail(request, id):
    foodstyle = get_object_or_404(FoodStyle, id=id)
    if not foodstyle.is_visible:
        return HttpResponseForbidden("Sorry, you do not have access to this page.")

    foodstyles = FoodStyle.objects.all()
    respondents_query = Respondent.objects.filter(foodstyle=foodstyle)
    context = context_foodstyle(foodstyle, respondents_query)
    #context['foodstyle'] = foodstyles

    return render(request, 'dashboard/foodstyle_detail.html', context)

def foodstyles(request):
    foodstyles = FoodStyle.objects.all().order_by('order')
    countries = Country.objects.all()
    genders = Gender.objects.all()
    respondents_query = Respondent.objects.all()

    foodstyle_counts = respondents_query.values('foodstyle__title').annotate(count=Count('foodstyle')).order_by('foodstyle__order')
    total_count = sum(item['count'] for item in foodstyle_counts)

    # Calculate the percentage of each foodstyle
    labels = [item['foodstyle__title'] for item in foodstyle_counts]
    percentages = [(item['count'] / total_count * 100) for item in foodstyle_counts]

    country_labels = {}
    country_values = {}
    for country in countries:
        foodstyle_counts_country = respondents_query.values('foodstyle__title').filter(country__title=country.title).annotate(count=Count('foodstyle')).order_by('foodstyle__order')
        total_count_country = sum(item['count'] for item in foodstyle_counts_country)
        labels_country = [item['foodstyle__title'] for item in foodstyle_counts_country]
        percentages_country = [(item['count'] / total_count_country * 100) for item in foodstyle_counts_country]

        country_labels[country.title] = labels_country
        country_values[country.title] = percentages_country


    context = {
        'foodstyles': foodstyles,
        'countries': countries,
        'genders': genders,
        'respondents': respondents_query,
        'labels': labels,
        'data_values': percentages,  # Note that we're passing percentages here
        'country_labels': country_labels,
        'country_values': country_values,
    }
    return render(request, 'dashboard/foodstyles.html', context)