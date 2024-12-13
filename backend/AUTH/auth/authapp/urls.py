from django.urls import path
from .views import SignUp
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #API's
    path('SignUp', SignUp.as_view(), name='Handle User Registration'),

    #Tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]