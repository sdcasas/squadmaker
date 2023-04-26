from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET',])
def increase_one(request):
    number = request.GET.get('number', None)
    if number is None or not str(number).isdigit():
        return JsonResponse({"number": "argument number error"}, status=400)
    return JsonResponse({"number": int(number) + 1}, status=200)


@api_view(['GET',])
def minimum_common(request):
    numbers_str = request.query_params.get('numbers', None)
    numbers_list = numbers_str.split(',') if numbers_str else None
    if numbers_str is None or not isinstance(numbers_list, list):
        return JsonResponse({"numbers": "argument number error"}, status=400)

    for num in numbers_list:
        if str(num).isdigit():
            return JsonResponse({"numbers": "argument num is not number"}, status=400)
        

    return JsonResponse({"number": int(numbers_str) + 1}, status=200)