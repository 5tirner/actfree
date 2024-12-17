from django.urls import path
from .views import SignUp, login, activation
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #API's
    path('SignUp', SignUp.as_view(), name='Handle User Registration'),
    path('login', login.as_view(), name='Handle User Login'),
    path('activation', activation.as_view(), name='Activation Check'),
    #Tokens
    path('tokens', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('newAccessToken', TokenRefreshView.as_view(), name="To Refresh The Access Token"),
]