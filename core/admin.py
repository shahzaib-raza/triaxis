from django.contrib import admin

from .models import PortfolioItem, PortfolioMedia, PortfolioCategory


class PortfolioMediaInline(admin.TabularInline):
    model = PortfolioMedia
    extra = 1


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        PortfolioMediaInline
    ]