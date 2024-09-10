from django_filters.fields import ChoiceField
from django_filters.filterset import FilterSet, NumberFilter

from .models import Advertisement


class AdvertisementFilter(FilterSet):
    repair_type = ChoiceField()
    rooms_qty_from = NumberFilter(lookup_expr='gte', field_name='rooms_qty_from')
    rooms_qty_to = NumberFilter(lookup_expr='lte', field_name='rooms_qty_to')

    class Meta:
        model = Advertisement
        fields = ['auction_allowed', 'category', 'repair_type', 'property_type', 'district', 'user']
