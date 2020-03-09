# _*_ encoding:utf-8 _*_
from django.shortcuts import render

import json
from .models import gis_info


def test(request):
    # address_point = gis_info.objects.filter( p_type == '1' )

    address_point = gis_info.objects.all()

    address_longitude = []
    address_latitude = []
    address_data = []
    for i in range(len(address_point)):
        address_longitude.append(address_point[i].lon)
        address_latitude.append(address_point[i].lat)
        address_data.append(address_point[i].name)

    return render(request, 'map/map_address.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})


