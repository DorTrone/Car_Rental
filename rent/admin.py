from django.contrib import admin
from .models import Car, Color, Material, CarImage

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')
    search_fields = ('name',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'brand', 'model', 'category', 'transmission', 
        'drive_type', 'max_speed', 'acceleration', 
        'description'
    )
    search_fields = ('brand', 'model')
    list_filter = ('category', 'drive_type', 'transmission')

    filter_horizontal = ('colors', 'materials')
    fieldsets = (
        (None, {
            'fields': ('brand', 'model', 'category', 'description', 'price', 'status')
        }),
        ('Technical Specs', {
            'fields': ('transmission', 'year', 'mileage', 'fuel_type', 'drive_type', 'max_speed', 'acceleration', 'scale', 'rarity', 'base_model', 'cover_model', 'packing', 'material_composition')
        }),
        ('Photos', {
            'fields': ('thumbnail',)
        }),
        ('Materials & Colors', {
            'fields': ('materials', 'colors')
        }),
    )

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')
