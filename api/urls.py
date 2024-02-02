from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView
from api.views import *


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('naats/', NaatsView.as_view()),
    path('getnaat/', GetNaatView.as_view()),
    path('search/<str:query>', SearchNaat.as_view()),
    path('naat-khwans/', GetNaatKhwans.as_view())
]
