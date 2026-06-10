from django.urls import path
from .views import home, layerforge, generate_svg, autolytics, autolytics_search, services, about

app_name = "core"

urlpatterns = [
    path("", home, name="home"),

    path(
        'layerforge/',
        layerforge,
        name='layerforge'
    ),

    path('generate/', generate_svg),

    path(
        'autolytics/',
        autolytics,
        name='autolytics'
    ),

    path(
        'autolytics/results/',
        autolytics_search,
        name='autolytics_search'
    ),

    path(
        'services/',
        services,
        name='services'
    ),

    path(
        'about/',
        about,
        name='about'
    ),
]