from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlaceRecommendationForm
from .models import PlaceRecommendation
from django.db.models import Q
import requests
from unidecode import unidecode
import re

province_templates = {
    "Buenos Aires": "Buenos_Aires.html",
    "Ciudad Autónoma de Buenos Aires": "Ciudad_de_Buenos_Aires.html",
    "Catamarca": "Catamarca.html",
    "Chaco": "Chaco.html",
    "Chubut": "Chubut.html",
    "Córdoba": "Cordoba.html",
    "Corrientes": "Corrientes.html",
    "Entre Ríos": "Entre_Rios.html",
    "Formosa": "Formosa.html",
    "Jujuy": "Jujuy.html",
    "La Pampa": "La_Pampa.html",
    "La Rioja": "La_Rioja.html",
    "Mendoza": "Mendoza.html",
    "Misiones": "Misiones.html",
    "Neuquén": "Neuquen.html",
    "Río Negro": "Rio_Negro.html",
    "Salta": "Salta.html",
    "San Juan": "San_Juan.html",
    "San Luis": "San_Luis.html",
    "Santa Cruz": "Santa_Cruz.html",
    "Santa Fe": "Santa_Fe.html",
    "Santiago del Estero": "Santiago_del_Estero.html",
    "Tierra del Fuego": "Tierra_del_Fuego.html",
    "Tucumán": "Tucuman.html",
}


def slugify_province(name):
    # Converts province name with accents to URL-friendly slug, e.g. "Río Negro" -> "rio-negro"
    return re.sub(r'\s+', '-', unidecode(name.lower()))

# Renders the home page with the main tourism map or welcome content
def home(request):
    return render(request, 'Tourism/tourism_home.html')

# Handles the place recommendation form: show form on GET, save recommendation on POST
def recommendation_view(request):
    if request.method == 'POST':
        form = PlaceRecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Tourism:success')
    else:
        form = PlaceRecommendationForm()
    return render(request, 'Tourism/recommend.html', {'form': form})

# Shows a success page after submitting a recommendation form successfully
def success_view(request):
    return render(request, 'Tourism/recommend_success.html')

# Shows all place recommendations saved in the database
def all_recommend(request):
    items = PlaceRecommendation.objects.all()
    return render(request, 'Tourism/all_recommend.html', {'items': items})

# Displays a filtered list of place recommendations based on search query (q parameter)
def recommendation_list(request):
    query = request.GET.get('q', '')
    if query:
        items = PlaceRecommendation.objects.filter(
            Q(place_name__icontains=query) |
            Q(description__icontains=query) |
            Q(province__icontains=query)
        )
    else:
        items = PlaceRecommendation.objects.all()
    return render(request, 'Tourism/recommendation_list.html', {'items': items, 'query': query})

# Displays search results page showing recommendations that match the search query
def search_results(request):
    query = request.GET.get('q', '')
    if query:
        items = PlaceRecommendation.objects.filter(
            Q(place_name__icontains=query) |
            Q(description__icontains=query) |
            Q(province__icontains=query)
        )
    else:
        items = PlaceRecommendation.objects.none()
    return render(request, 'Tourism/search_results.html', {'items': items, 'query': query})

# Edits a specific place recommendation identified by primary key (pk)
def edit_recommendation(request, pk):
    recommendation = get_object_or_404(PlaceRecommendation, pk=pk)
    if request.method == 'POST':
        form = PlaceRecommendationForm(request.POST, instance=recommendation)
        if form.is_valid():
            form.save()
            return redirect('Tourism:success')
    else:
        form = PlaceRecommendationForm(instance=recommendation)
    return render(request, 'Tourism/edit_recommendation.html', {'form': form})

# Shows detailed description for a specific recommended place by primary key (pk)
def view_description(request, pk):
    recommendation = get_object_or_404(PlaceRecommendation, pk=pk)
    return render(request, 'Tourism/view_description.html', {'recommendation': recommendation})

# Deletes a specific place recommendation when a POST request is made
def delete_recommendation(request, pk):
    recommendation = get_object_or_404(PlaceRecommendation, pk=pk)
    if request.method == "POST":
        recommendation.delete()
        return redirect('Tourism:all_recommend')

# Individual province views (optional if you want separate static pages)

def buenos_aires(request):
    return render(request, 'Tourism/provinces/Buenos_Aires.html')

def ciudad_buenos_aires(request):
    return render(request, 'Tourism/provinces/Ciudad_Buenos_Aires.html')

def catamarca(request):
    return render(request, 'Tourism/provinces/Catamarca.html')

def chaco(request):
    return render(request, 'Tourism/provinces/Chaco.html')

def chubut(request):
    return render(request, 'Tourism/provinces/Chubut.html')

def cordoba(request):
    return render(request, 'Tourism/provinces/Cordoba.html')

def corrientes(request):
    return render(request, 'Tourism/provinces/Corrientes.html')

def entre_rios(request):
    return render(request, 'Tourism/provinces/Entre_Rios.html')

def formosa(request):
    return render(request, 'Tourism/provinces/Formosa.html')

def jujuy(request):
    return render(request, 'Tourism/provinces/Jujuy.html')

def la_pampa(request):
    return render(request, 'Tourism/provinces/La_Pampa.html')

def la_rioja(request):
    return render(request, 'Tourism/provinces/La_Rioja.html')

def mendoza(request):
    return render(request, 'Tourism/provinces/Mendoza.html')

def misiones(request):
    return render(request, 'Tourism/provinces/Misiones.html')

def neuquen(request):
    return render(request, 'Tourism/provinces/Neuquen.html')

def rio_negro(request):
    return render(request, 'Tourism/provinces/Rio_Negro.html')

def salta(request):
    return render(request, 'Tourism/provinces/Salta.html')

def san_juan(request):
    return render(request, 'Tourism/provinces/San_Juan.html')

def san_luis(request):
    return render(request, 'Tourism/provinces/San_Luis.html')

def santa_cruz(request):
    return render(request, 'Tourism/provinces/Santa_Cruz.html')

def santa_fe(request):
    return render(request, 'Tourism/provinces/Santa_Fe.html')

def santiago_del_estero(request):
    return render(request, 'Tourism/provinces/Santiago_Del_Estero.html')

def tierra_del_fuego(request):
    return render(request, 'Tourism/provinces/Tierra_Del_Fuego.html')

def tucuman(request):
    return render(request, 'Tourism/provinces/Tucuman.html')


# Main province detail view:
# - shows all place recommendations in that province,
# - fetches current weather for that province from WeatherAPI,
# - passes all data to province template dynamically
def unslugify_province(slug):
    # Map back to full province names (add all as needed)
    province_map = {
        "buenos-aires": "Buenos Aires",
        "ciudad-autonoma-de-buenos-aires": "Ciudad Autónoma de Buenos Aires",
        "catamarca": "Catamarca",
        "chaco": "Chaco",
        "chubut": "Chubut",
        "cordoba": "Córdoba",
        "corrientes": "Corrientes",
        "entre-rios": "Entre Ríos",
        "formosa": "Formosa",
        "jujuy": "Jujuy",
        "la-pampa": "La Pampa",
        "la-rioja": "La Rioja",
        "mendoza": "Mendoza",
        "misiones": "Misiones",
        "neuquen": "Neuquén",
        "rio-negro": "Río Negro",
        "salta": "Salta",
        "san-juan": "San Juan",
        "san-luis": "San Luis",
        "santa-cruz": "Santa Cruz",
        "santa-fe": "Santa Fe",
        "santiago-del-estero": "Santiago del Estero",
        "tierra-del-fuego": "Tierra del Fuego",
        "tucuman": "Tucumán",
    }
    return province_map.get(slug, slug.replace("-", " ").title())

def fetch_weather_for(province_name):
    
    api_key = "***API KEY***"  # Where I put my actual API key
    try:
        response = requests.get("https://api.weatherapi.com/v1/current.json", params={
            "key": api_key,
            "q": province_name,
            "lang": "en"
        })
        data = response.json()
        return {
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "icon": data["current"]["condition"]["icon"],
            "local_time": data["location"]["localtime"],
        }
    except Exception:
        return None

def show_province(request, province_slug):
    province_name = unslugify_province(province_slug)
    items = PlaceRecommendation.objects.filter(province=province_name)
    weather = fetch_weather_for(province_name)

    template_name = province_templates.get(province_name)
    if not template_name:
        # fallback if province not found in dictionary
        template_name = f'{province_name.replace(" ", "_")}.html'

    return render(request, f'Tourism/provinces/{template_name}', {
        'items': items,
        'province': province_name,
        'weather': weather
    })


# View for showing weather summary of all provinces:
# fetches current weather for all provinces,
# prepares list of weather data to display in template with links to province pages
def weather_by_province_view(request):
    provinces = [
        "Buenos Aires", "Ciudad de Buenos Aires", "Catamarca", "Chaco", "Chubut",
        "Córdoba", "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja",
        "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", "San Luis",
        "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán"
    ]

    api_key = "***API KEY***"  # Where I put my actual API key
    weather_data = []

    for province in provinces:
        try:
            response = requests.get("https://api.weatherapi.com/v1/current.json", params={
                "key": api_key,
                "q": province,
                "lang": "en"
            })

            data = response.json()
            weather_data.append({
                "province": province,
                "slug": slugify_province(province),
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "icon": data["current"]["condition"]["icon"],
                "local_time": data["location"]["localtime"],
            })
        except Exception:
            weather_data.append({
                "province": province,
                "slug": slugify_province(province),  # add slug even if error!
                "error": "Could not fetch weather data"
            })

    return render(request, "Tourism/weather_by_province.html", {"weather_data": weather_data})
