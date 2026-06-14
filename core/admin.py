from django.contrib import admin

from .models import PortfolioItem, PortfolioMedia, PortfolioCategory, PortfolioSubCategory


class PortfolioMediaInline(admin.TabularInline):
    model = PortfolioMedia
    extra = 1


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(PortfolioSubCategory)
class PortfolioSubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "cover_ratio"
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        PortfolioMediaInline
    ]