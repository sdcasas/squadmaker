from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


swagger_joker = swagger_auto_schema(
        method='get',
        operation_summary='Joker',
        data_format='application/json',
        responses={
            200: 'success'
        }
    )