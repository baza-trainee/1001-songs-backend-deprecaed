# from apps.auth.serializers import CustomTokenRefreshSerializers
# from apps.users.serializers import UserSerializer
#
#
# class SwaggerUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         fields = (
#             'id', 'email', 'is_active', 'is_scientist', 'is_staff', 'is_superuser',
#             'last_login', 'created_at', 'updated_at', 'profile'
#         )
#
#
# class SwaggerTokenRefreshCustomSerializers(CustomTokenRefreshSerializers):
#     def validate(self, attrs):
#         return super().validate(attrs)
#