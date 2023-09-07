# from django.utils.decorators import method_decorator
# from rest_framework import status
#
# from drf_yasg.utils import swagger_auto_schema
#
# from .serializers import SwaggerUserSerializer, SwaggerTokenRefreshCustomSerializers
#
#
# def response_with_user_swagger():
#     return method_decorator(swagger_auto_schema(responses={
#         status.HTTP_200_OK: SwaggerUserSerializer()
#     }, security=[]), 'post')
#
#
# def response_refresh_swagger():
#     return method_decorator(swagger_auto_schema(responses={
#         status.HTTP_200_OK: SwaggerTokenRefreshCustomSerializers()
#     }, security=[]), 'post')
