from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Tourism'

urlpatterns = [
    path('', views.home, name='tourism_home'),
    path('recommend/', views.recommendation_view, name='recommend'),
    path('success/', views.success_view, name='success'),
    path('all_recommend/', views.all_recommend, name='all_recommend'),
    path('search/results/', views.search_results, name='search_results'),
path('province/<slug:province_slug>/', views.show_province, name='show_province'),
    path('edit/<int:pk>/', views.edit_recommendation, name='edit_recommendation'),
    path('recommendation/<int:pk>/delete/', views.delete_recommendation, name='delete_recommendation'),
    path('view/<int:pk>/', views.view_description, name='view_description'),

    path("weather/", views.weather_by_province_view, name="weather_by_province"),





    # provinces

    path('provinces/buenos-aires/', views.buenos_aires, name='Buenos_Aires'),
    path('provinces/ciudad-buenos-aires/', views.ciudad_buenos_aires, name='Ciudad_Buenos_Aires'),
    path('provinces/catamarca/', views.catamarca, name='Catamarca'),
    path('provinces/chaco/', views.chaco, name='Chaco'),
    path('provinces/chubut/', views.chubut, name='Chubut'),
    path('provinces/cordoba/', views.cordoba, name='Cordoba'),
    path('provinces/corrientes/', views.corrientes, name='Corrientes'),
    path('provinces/entre-rios/', views.entre_rios, name='Entre_Rios'),
    path('provinces/formosa/', views.formosa, name='Formosa'),
    path('provinces/jujuy/', views.jujuy, name='Jujuy'),
    path('provinces/la-pampa/', views.la_pampa, name='La_Pampa'),
    path('provinces/la-rioja/', views.la_rioja, name='La_Rioja'),
    path('provinces/mendoza/', views.mendoza, name='Mendoza'),
    path('provinces/misiones/', views.misiones, name='Misiones'),
    path('provinces/neuquen/', views.neuquen, name='Neuquen'),
    path('provinces/rio-negro/', views.rio_negro, name='Rio_Negro'),
    path('provinces/salta/', views.salta, name='Salta'),
    path('provinces/san-juan/', views.san_juan, name='San_Juan'),
    path('provinces/san-luis/', views.san_luis, name='San_Luis'),
    path('provinces/santa-cruz/', views.santa_cruz, name='Santa_Cruz'),
    path('provinces/santa-fe/', views.santa_fe, name='Santa_Fe'),
    path('provinces/santiago-del-estero/', views.santiago_del_estero, name='Santiago_Del_Estero'),
    path('provinces/tierra-del-fuego/', views.tierra_del_fuego, name='Tierra_Del_Fuego'),
    path('provinces/tucuman/', views.tucuman, name='Tucuman'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)