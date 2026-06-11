from django.urls import path
from .views import home, layerforge, generate_svg, autolytics, autolytics_search, services, about, portfolio_category, portfolio_detail

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

    path(
        "portfolio/<slug:category>/",
        portfolio_category,
        name="portfolio_category"
    ),

    path(
        "portfolio/<slug:category>/<slug:slug>/",
        portfolio_detail,
        name="portfolio_detail"
    ),
]