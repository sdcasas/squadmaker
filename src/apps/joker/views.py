from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from apps.joker.models import Joker
from apps.joker.serializers import JokerSerializer
from apps.joker.services import JokerService
from apps.joker.swagger import swagger_joker


@swagger_joker
@api_view(['GET', 'POST', 'PATCH'])
def api_joker(request, joker_type=None, number=None):

    if request.method == 'GET':
        if not joker_type in ['chuck', 'dad', None]:
            return JsonResponse({"message": "joker_type inválido"}, status=400)
        if number:
            try:
                joker = Joker.objects.get(number=number)
            except Joker.DoesNotExists:
                return JsonResponse({"number": "joker not found with number"}, status=400)
        else:
            js = JokerService(type=joker_type)
            joker = js.get_value()

        status_code = 200
        status = "Success"

    if request.method == 'POST':
        joker_value = request.data.get('joker', 'none')
        if not isinstance(joker_value, str):
            return JsonResponse({"joker": "value is not string"}, status=400)
        try:
            joker, created = Joker.objects.get_or_create(value = joker_value)
            status_code = 201 if created else 200
            status = 'created success' if created else "joke already exists"
        except Exception as e:
            return JsonResponse({"joker": "error in create joker object"}, status=400)

    if request.method == 'PATCH':
        joker_value = request.data.get('joker', 'none')
        if not isinstance(joker_value, str):
            return JsonResponse({"joker": "value is not string"}, status=400)
        if number is None:
            return JsonResponse({"number": "number is bad"}, status=400)
        try:
            joker = Joker.objects.get(number = number)
            joker.value = joker_value
            joker.save()
        except Joker.DoesNotExist:
            return JsonResponse({"number": "joker not found with number"}, status=400)
        except Exception as e:
            return JsonResponse({"joker": "error in create joker object"}, status=400)
        status_code = 200
        status = 'updated success'

    data = {
        'joker': joker.value,
        'number': joker.number,
        'joker_type': joker.joker_type or '',
        "status": status
    }
    return JsonResponse(data, status=status_code)


class JokerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Joker.objects.all()
    serializer_class = JokerSerializer
