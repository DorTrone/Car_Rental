from rest_framework import serializers
from .models import Car, Color, Material, CarImage, FAQ, ContactMessage

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True, read_only=True)
    materials = MaterialSerializer(many=True, read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']