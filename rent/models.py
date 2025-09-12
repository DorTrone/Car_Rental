from django.db import models


class CarCategory(models.TextChoices):
    PREMIUM = "premium", "Premium"
    SPORT = "sport", "Sport"
    HYPER = "hyper", "Hyper"
    

class TransmissionType(models.TextChoices):
    AUTOMATIC = "automatic", "Automatic"
    MANUAL = "manual", "Manual"

class DriveType(models.TextChoices):
    FWD = "fwd", "FWD"
    RWD = "rwd", "RWD"
    AWD = "awd", "AWD"

class FuelType(models.TextChoices):
    PETROL = "petrol", "Petrol"
    ELECTRIC = "electric", "Electric"
    HYBRID = "hybrid", "Hybrid"


class CarStatus(models.TextChoices):
    AVAILABLE = "available", "Available"
    RENTED = "rented", "Rented"
    MAINTENANCE = "maintenance", "Maintenance"


class Material(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=50, help_text="Name of the social network")
    url = models.URLField(help_text="Link to your profile or page")
    icon = models.ImageField(upload_to="social_icons/", blank=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CarCategory.choices, default=CarCategory.PREMIUM)
    transmission = models.CharField(max_length=20, choices=TransmissionType.choices)
    acceleration = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, help_text="Time in seconds")
    drive_type = models.CharField(max_length=20, choices=DriveType.choices)
    fuel_type = models.CharField(max_length=20, choices=FuelType.choices)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField(help_text="Mileage in km")
    max_speed = models.PositiveIntegerField(help_text="Max speed in km/h")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per day")
    status = models.CharField(max_length=20, choices=CarStatus.choices, default=CarStatus.AVAILABLE)
    scale = models.CharField(max_length=50, blank=True, help_text="e.g. 1:8 scale")
    rarity = models.CharField(max_length=100, blank=True, help_text="e.g. Limited edition of 199 pieces")
    base_model = models.CharField(max_length=255, blank=True, help_text="Base dimensions and weight")
    cover_model = models.CharField(max_length=255, blank=True, help_text="Cover dimensions and weight")
    materials = models.ManyToManyField(Material, blank=True)
    material_composition = models.TextField(blank=True, help_text="Detailed composition, e.g. 85% Polyurethane")
    packing = models.TextField(blank=True, help_text="Packaging dimensions and weight")
    colors = models.ManyToManyField(Color, blank=True)
    thumbnail = models.ImageField(upload_to="cars/thumbnails/")
    description = models.TextField(blank=True, help_text="Description of the car")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        ordering = ["-created_at"]


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="cars/images/")

    def __str__(self):
        return f"Image of {self.car}"
    
    class Meta:
        ordering = ["car"]


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["question"]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        ordering = ["-created_at"]