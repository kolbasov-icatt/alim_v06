from .models import FoodStyle, Country, Food, Gender, Generation, Area, RespAcq, Respondent, FoodCat
from django.db.models import Count, Q, F, Case, When, Value, CharField, Avg, FloatField


def context_country(country, respondents_query):
    """
    Returns a context for a country view based on:
        respondents_query 
    Examples of respondents_query:
        respondents_query = Respondent.objects.filter(country=country)
        respondents_query = Respondent.objects.filter(country=country, gender__title=gender)
    """
    countries = Country.objects.all()
    foodstyle_counts = (
        respondents_query
        .values('foodstyle__title')
        .annotate(count=Count('foodstyle'))
        .annotate(
            order=Case(
                When(foodstyle__title="Nessuno di questi", then=Value(2)),
                default=Value(1),
                output_field=CharField()
            )
        )
        .order_by('order', '-count')
    )
    total_count = sum(item['count'] for item in foodstyle_counts)  # number of entries
    

    # Calculate the percentage of each foodstyle
    labels = [item['foodstyle__title'] for item in foodstyle_counts]
    percentages = [(item['count'] / total_count * 100) for item in foodstyle_counts]

    # GENDER DISTRIBUTION
    genders = Gender.objects.all()
    gender_counts = respondents_query.values('gender__title').annotate(count=Count('gender')).order_by('-count')
    total_count_gender = sum(item['count'] for item in gender_counts)  # number of entries
    labels_gender = [item['gender__title'] for item in gender_counts]
    percentages_gender = [(item['count'] / total_count_gender * 100) for item in gender_counts]

    # GENERATION DISTRIBUTION
    generations = Generation.objects.all()
    generations_counts = respondents_query.values('generation__title').annotate(count=Count('generation')).order_by('-count')
    total_count_generations = sum(item['count'] for item in generations_counts)  # number of entries
    labels_generations = [item['generation__title'] for item in generations_counts]
    percentages_generations = [(item['count'] / total_count_generations * 100) for item in generations_counts]

    # RESPONSABILI ACQUISTI
    resps = RespAcq.objects.all()
    resp_counts = respondents_query.values('resp__title').annotate(count=Count('resp')).order_by('-count')
    total_count_resp = sum(item['count'] for item in resp_counts)  # number of entries
    labels_resp = [item['resp__title'] for item in resp_counts]
    percentages_resp = [(item['count'] / total_count_resp * 100) for item in resp_counts]
    
    # AREA
    labels_area = None
    percentages_area = None
    if country.title == "Italia":
        area_counts = respondents_query.values('area__title').annotate(count=Count('area')).order_by('-count')
        total_count_area = sum(item['count'] for item in area_counts)  # number of entries
        labels_area = [item['area__title'] for item in area_counts]
        percentages_area = [(item['count'] / total_count_area * 100) for item in area_counts]

    # FOOD
    foods = Food.objects.all()
    food_dictionary = {}
    for food in foods:
        result = respondents_query.filter(food=food
        ).aggregate(
            average_times_per_month=Avg('frequency__times_per_month'),
            total_growth=Count('growthrate__value'),
            positive_growth=Count('growthrate__value', filter=Q(growthrate__value=1)),
            positive_growth_rate=F('positive_growth') * 100.0 / F('total_growth'),           

            negative_growth=Count('growthrate__value', filter=Q(growthrate__value=-1)),
            negative_growth_rate=F('negative_growth') * 100.0 / F('total_growth'),           
        )
        average_times_per_month = result['average_times_per_month'] or 0 # Default to 0 if None
        if result['total_growth']:
            food_dictionary[food] = (average_times_per_month, result['positive_growth_rate'] - result['negative_growth_rate'] )
        else:
            food_dictionary[food] = (average_times_per_month, 0)

    sorted_foods = sorted(food_dictionary.items(), key=lambda item: item[1][0], reverse=True)

    # top 5 products by frequency
    food1_label = sorted_foods[0][0]
    food1_freq =  sorted_foods[0][1][0]
    food1_cam =  sorted_foods[0][1][1]
    food2_label = sorted_foods[1][0]
    food2_freq = sorted_foods[1][1][0]
    food2_cam =  sorted_foods[1][1][1]
    food3_label = sorted_foods[2][0]
    food3_freq = sorted_foods[2][1][0]
    food3_cam =  sorted_foods[2][1][1]
    food4_label = sorted_foods[3][0]
    food4_freq = sorted_foods[3][1][0]
    food4_cam =  sorted_foods[3][1][1]
    food5_label = sorted_foods[4][0]
    food5_freq = sorted_foods[4][1][0]
    food5_cam =  sorted_foods[4][1][1]

    context = {
        'navbar_title': country.title,
        'navbar_image': country.image,
        'total_count': foodstyle_counts,
        'country': country,
        'countries': countries,
        'genders': genders,
        'generations': generations,
        'resps': resps,
        'labels': labels,
        'data_values': percentages,
        'labels_gender': labels_gender,
        'values_gender': percentages_gender,
        'labels_generations': labels_generations,
        'values_generations': percentages_generations,
        'labels_resp': labels_resp,
        'values_resp': percentages_resp,
        'labels_area': labels_area,
        'values_area': percentages_area,
        'food_dictionary': food_dictionary,
        'sorted_foods': sorted_foods,
        'food1_label': food1_label,
        'food1_freq': food1_freq,
        'food2_label': food2_label,
        'food2_freq': food2_freq,
        'food3_label': food3_label,
        'food3_freq': food3_freq,
        'food4_label': food4_label,
        'food4_freq': food4_freq,
        'food5_label': food5_label,
        'food5_freq': food5_freq,
        'food1_cam': food1_cam,
        'food2_cam': food2_cam,
        'food3_cam': food3_cam,
        'food4_cam': food4_cam,
        'food5_cam': food5_cam,
    }
    
    return context

# helping function
def calculate_statistics(queryset, category_field, count_field):
    order_field = f'{count_field}__order'
    # Perform the query and annotate with counts
    category_counts = (
        queryset
        .exclude(**{f"{category_field}__isnull": True})  # Exclude entries where category_field is None
        .values(category_field)  # Group by the category field
        .annotate(count=Count(count_field))  # Count occurrences
        .order_by(order_field)  
    )

    # Calculate total count in a single query
    total_count = sum(item['count'] for item in category_counts)

    # Generate labels and percentages
    #labels = [item[category_field] for item in category_counts]
    labels = [item[category_field] for item in category_counts if item[category_field] is not None]
    percentages = [(item['count'] / total_count * 100) if total_count > 0 else 0 for item in category_counts]

    return labels, percentages

# helping function for "context_food" to calculate average frequency and growth for a product
def calculate_av_freq_growth(respondents_query):
    result = respondents_query.aggregate(
        average_times_per_month=Avg('frequency__times_per_month'),
        total_growth=Count('growthrate__value'),
        positive_growth=Count('growthrate__value', filter=Q(growthrate__value=1)),
        positive_growth_rate=Case(
            When(total_growth=0, then=Value(0.0)),  # Avoid division by zero by setting value to 0.0
            default=F('positive_growth') * 100.0 / F('total_growth'),  # Normal case
            output_field=FloatField()
        ),
        negative_growth=Count('growthrate__value', filter=Q(growthrate__value=-1)),
        negative_growth_rate=Case(
            When(total_growth=0, then=Value(0.0)),  # Avoid division by zero by setting value to 0.0
            default=F('negative_growth') * 100.0 / F('total_growth'),  # Normal case
            output_field=FloatField()
        ),
    )

    # Extract results, providing default values if None
    freq_av = result.get('average_times_per_month', 0)  # Default to 0 if None
    positive_growth_rate = result.get('positive_growth_rate', 0)
    negative_growth_rate = result.get('negative_growth_rate', 0)

    # Calculate the net growth rate
    growth_av = positive_growth_rate - negative_growth_rate
    return freq_av, growth_av


def context_food(food, respondents_query):
    freq_av, growth_av = calculate_av_freq_growth(respondents_query)

    countries = Country.objects.all()
    data_country = []
    for country in countries:
        query = respondents_query.filter(country=country)
        freq, growth = calculate_av_freq_growth(query)
        data_country.append((country.title, freq, growth))
    labels_country = [tup[0] for tup in data_country]
    freq_country = [tup[1] for tup in data_country]
    growth_country = [tup[2] for tup in data_country]
    countries_color = [country.color for country in countries] 
    countries_border_color = [country.border_color for country in countries] 

    label_italia, freq_italia, growth_italia = data_country[0]
    label_usa, freq_usa, growth_usa = data_country[1]
    label_francia, freq_francia, growth_francia = data_country[2]
    label_germania, freq_germania, growth_germania = data_country[3]

    areas = Area.objects.all().order_by('order')
    data_area = []
    for area in areas:
        query = respondents_query.filter(area=area)
        freq, growth = calculate_av_freq_growth(query)
        data_area.append((area.title, freq, growth))
    areas_titles = [s[0] for s in data_area]

    foodstyles = FoodStyle.objects.all().order_by('order')
    data_styles = []
    for foodstyle in foodstyles:
        query = respondents_query.filter(foodstyle=foodstyle)
        freq, growth = calculate_av_freq_growth(query)
        data_styles.append((foodstyle.title, freq, growth))
    foodstyles_titles = [s[0] for s in data_styles]
    labels_styles = [tup[0] for tup in data_styles]
    freq_styles = [tup[1] for tup in data_styles]
    growth_styles = [tup[2] for tup in data_styles]
    
    genders = Gender.objects.exclude(title="Altro")
    data_gender = []
    for gender in genders:
        query = respondents_query.filter(gender=gender)
        freq, growth = calculate_av_freq_growth(query)
        data_gender.append((gender.title, freq, growth))
    gender_titles = [s[0] for s in data_gender]
    
    generations = Generation.objects.all().order_by('order')
    data_generation = []
    for generation in generations:
        query = respondents_query.filter(generation=generation)
        freq, growth = calculate_av_freq_growth(query)
        data_generation.append((generation.title, freq, growth))
    generation_titles = [s[0] for s in data_generation]
    labels_generation = [tup[0] for tup in data_generation]
    freq_generation = [tup[1] for tup in data_generation]
    growth_generation = [tup[2] for tup in data_generation]

    resps = RespAcq.objects.all()
    data_resp = []
    for resp in resps:
        query = respondents_query.filter(resp=resp)
        freq, growth = calculate_av_freq_growth(query)
        data_resp.append((resp.title, freq, growth))
    resp_titles = [s[0] for s in data_resp]

    # for horizontal bars
    freq_labels, freq_percentages = calculate_statistics(
    respondents_query, 'frequency__cat', 'frequency'
    )
    growth_labels, growth_percentages = calculate_statistics(
        respondents_query, 'growthrate__title', 'growthrate'
    )

    context = {
        'navbar_title': food.short_name,
        'navbar_image': food.image,
        'food': food,
        'freq_av': freq_av,
        'growth_av': growth_av,
        'freq_labels': freq_labels,
        'freq_percentages': freq_percentages,
        'growth_labels': growth_labels,
        'growth_percentages': growth_percentages,
        # countries:
        'label_italia': label_italia, 
        'freq_italia': freq_italia, 
        'growth_italia': growth_italia,
        'label_usa': label_usa,
        'freq_usa':freq_usa, 
        'growth_usa':growth_usa,
        'label_francia':label_francia, 
        'freq_francia':freq_francia, 
        'growth_francia':growth_francia,
        'label_germania':label_germania, 
        'freq_germania':freq_germania, 
        'growth_germania':growth_germania,
        'foodstyles': foodstyles,
        'labels_country': labels_country,
        'freq_country': freq_country,
        'growth_country': growth_country,
        'countries_border_color': countries_border_color,
        'countries_color': countries_color,
        'labels_generation': labels_generation,
        'freq_generation': freq_generation,
        'growth_generation': growth_generation,
        'labels_styles': labels_styles,
        'freq_styles': freq_styles,
        'growth_styles': growth_styles,

    }

    for i, category in enumerate(foodstyles_titles):
        label, freq, growth = data_styles[i]  # Unpacking the tuple for each category
        context_key_prefix = category.lower().replace(" ", "")  # Creating a key name based on category
        context[f'label_{context_key_prefix}'] = label
        context[f'freq_{context_key_prefix}'] = freq
        context[f'growth_{context_key_prefix}'] = growth
    
    for i, category in enumerate(areas_titles):
        label, freq, growth = data_area[i]  # Unpacking the tuple for each category
        context_key_prefix = category.lower().replace(" ", "")  # Creating a key name based on category
        context[f'label_{context_key_prefix}'] = label
        context[f'freq_{context_key_prefix}'] = freq
        context[f'growth_{context_key_prefix}'] = growth

    for i, category in enumerate(gender_titles):
        label, freq, growth = data_gender[i]  # Unpacking the tuple for each category
        context_key_prefix = category.lower().replace(" ", "")  # Creating a key name based on category
        context[f'label_{context_key_prefix}'] = label
        context[f'freq_{context_key_prefix}'] = freq
        context[f'growth_{context_key_prefix}'] = growth
    
    for i, category in enumerate(generation_titles):
        label, freq, growth = data_generation[i]  # Unpacking the tuple for each category
        context_key_prefix = category.lower().replace(" ", "")  # Creating a key name based on category
        context[f'label_{context_key_prefix}'] = label
        context[f'freq_{context_key_prefix}'] = freq
        context[f'growth_{context_key_prefix}'] = growth

    for i, category in enumerate(resp_titles):
        label, freq, growth = data_resp[i]  # Unpacking the tuple for each category
        context_key_prefix = category.lower().replace(" ", "").replace("'", "")  # Creating a key name based on category
        context[f'label_{context_key_prefix}'] = label
        context[f'freq_{context_key_prefix}'] = freq
        context[f'growth_{context_key_prefix}'] = growth
    return context