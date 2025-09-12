import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    min_year = django_filters.NumberFilter(field_name="year", lookup_expr="gte")
    max_year = django_filters.NumberFilter(field_name="year", lookup_expr="lte")

    min_speed = django_filters.NumberFilter(field_name="max_speed", lookup_expr="gte")
    max_speed = django_filters.NumberFilter(field_name="max_speed", lookup_expr="lte")

    min_acceleration = django_filters.NumberFilter(field_name="acceleration", lookup_expr="gte")
    max_acceleration = django_filters.NumberFilter(field_name="acceleration", lookup_expr="lte")

    class Meta:
        model = Car
        fields = [
            "category", "drive_type", "transmission", "fuel_type", "status"
        ]
