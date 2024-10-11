from django_filters.filterset import FilterSet, NumberFilter, CharFilter

from .models import Advertisement


class AdvertisementFilter(FilterSet):
    quadrature_from = NumberFilter(lookup_expr='gte', field_name='quadrature_from')
    quadrature_to = NumberFilter(lookup_expr='lte', field_name='quadrature_to')
    price_from = NumberFilter(lookup_expr='gte', field_name='price')
    price_to = NumberFilter(lookup_expr='lte', field_name='price')
    floor_from = NumberFilter(lookup_expr='gte', field_name='floor_from')
    floor_to = NumberFilter(lookup_expr='lte', field_name='floor_to')
    house_quadrature_from = NumberFilter(lookup_expr='gte', field_name='house_quadrature_from')
    house_quadrature_to = NumberFilter(lookup_expr='lte', field_name='house_quadrature_to')
    rooms = CharFilter(lookup_expr='in', method='get_rooms_in', label='кол-во комнат в')

    def get_rooms_in(self, queryset, field_name, value):
        rooms_temp = []
        rooms_range = [{'adv_id': obj.pk, 'rooms': obj.get_rooms_qty()} for obj in queryset]
        for room in rooms_range:
            rooms = room.get('rooms')
            rooms = list(range(rooms[0], rooms[1] + 1))
            room.update(rooms=rooms)
        query_rooms = list(map(lambda i: int(i), value.split(',')))
        for room in query_rooms:
            for obj in rooms_range:
                if room not in obj.get('rooms'):
                    continue
                ad_obj = Advertisement.objects.get(id=obj.get('adv_id')).pk
                rooms_temp.append(ad_obj)
        return queryset.filter(id__in=rooms_temp)

    class Meta:
        model = Advertisement
        fields = ['category', 'repair_type', 'property_type', 'district', 'is_studio', 'operation_type',
                  'rooms', 'user', 'is_moderated']
