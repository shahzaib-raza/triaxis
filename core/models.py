from django.db import models

# Create your models here.


class PortfolioCategory(models.Model):
    class CategoryChoices(models.TextChoices):
        DESIGN = "design", "Design"
        DATA_SCRAPING = "data-scraping", "Data Scraping"
        RESEARCH = "research", "Research"
        DATA_ENTRY = "data-entry", "Data Entry"
        AUTOMATION = "automation", "Automation"
        AI = "ai", "AI"
        WEB_DEV = "web-development", "Web Development"
        VIDEO = "video", "Video"
        TRAINING = "training-education", "Training & Education"

    name = models.CharField(max_length=50, choices=CategoryChoices.choices)

    slug = models.SlugField(unique=True)

    icon = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(
        "PortfolioCategory",
        on_delete=models.CASCADE
    )

    short_description = models.CharField(max_length=300)
    description = models.TextField()

    featured = models.BooleanField(default=False)

    cover_image = models.ImageField(upload_to="portfolio/covers/")

    live_url = models.URLField(blank=True)
    publication_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PortfolioMedia(models.Model):

    IMAGE = "image"
    VIDEO = "video"

    MEDIA_CHOICES = [
        (IMAGE, "Image"),
        (VIDEO, "Video")
    ]

    portfolio = models.ForeignKey(
        PortfolioItem,
        on_delete=models.CASCADE,
        related_name="media"
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_CHOICES
    )

    image = models.ImageField(
        upload_to="portfolio/images/",
        blank=True
    )

    video = models.FileField(
        upload_to="portfolio/videos/",
        blank=True
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.portfolio.title} - {self.media_type}"