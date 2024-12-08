from django.urls import path
from .views import login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    #API's
    path('login', login),
    #Tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tpken/verify/', TokenVerifyView.as_view(), name='token_verify'),
]