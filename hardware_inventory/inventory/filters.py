import django_filters
from .models import HardwareItem

class HardwareItemFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')

    class Meta:
        model = HardwareItem
        fields = ['category']
