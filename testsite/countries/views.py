from django.http import JsonResponse
from django.db.models import Sum
from .models import Country, Region

def stats(request):
    # TODO - Provide name, number_countries and total_population for each region

    total_population = 0 # default value
    data = [] # build the data list to return

    regions = Region.objects.all() # get all regions

    for region in regions:
        print('\nregion: ', region)
        for country in Country.objects.filter(region=region):
            print('country: ', country)
            print('country.population: ', country.population)
            number_countries = Country.objects.filter(region=region).count()
            # total_population = Country.objects.filter(region=region).aggregate(Sum('population'))
            total_population += country.population
            print('number_countries: ', number_countries)
            print('total_population: ', total_population)
            
        data.append([{"name": region.name, 
            "number_countries": number_countries,
            "total_population": total_population
        }])
        total_population = 0 # reset total_population

    response = {"regions": data}

    return JsonResponse(response)
