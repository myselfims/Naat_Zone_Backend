from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from api.serializers import *
from api.models import *
from api.naat_scrapper import *




class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        print(ser.errors)
        return Response(ser.errors)
    
class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(password=password,email=email)
            token = AccessToken.for_user(user=user)
            return Response({'token':str(token)})
        except Exception as e:
            return Response({'error':'Invalid credentails or user not available!'})
        
class NaatsView(APIView):
    def get(self, request):
        naats = SearchNaats('ramzan')
        return Response(naats[0])
        
class SearchNaat(APIView):
    def get(self, request,query):
        print(query)
        naats = SearchNaats(query)
        return Response(naats[0])
        
class GetNaatKhwans(APIView):
    def get(self, request):
        naats_khwans = get_naat_khwans()
        return Response(naats_khwans)
        
class GetNaatView(APIView):
    def post(self, request, url):
        url = request.data['url']
        print(request.data['url'])
        naats = SearchNaats('new')
        return Response(naats[0])