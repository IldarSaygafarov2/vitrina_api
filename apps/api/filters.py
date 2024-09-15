from django_filters.fields import ChoiceField
from django_filters.filterset import FilterSet, NumberFilter

from .models import Advertisement


class AdvertisementFilter(FilterSet):
    repair_type = ChoiceField()
    floor_from = NumberFilter(lookup_expr='gte', field_name='floor_from')
    floor_to = NumberFilter(lookup_expr='lte', field_name='floor_to')
    quadrature_from = NumberFilter(lookup_expr='gte', field_name='quadrature_from')
    quadrature_to = NumberFilter(lookup_expr='lte', field_name='quadrature_to')
    price_from = NumberFilter(lookup_expr='gte', field_name='price')
    price_to = NumberFilter(lookup_expr='lte', field_name='price')

    class Meta:
        model = Advertisement
        fields = ['category', 'repair_type', 'property_type', 'district', 'is_studio']
