from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
import firebase_admin
from firebase_admin import credentials, auth
import YogiG.keyconfig as senv
import json
from rest_framework_simplejwt.tokens  import RefreshToken
from YogiG.settings import SIMPLE_JWT
from django.views import View
from rest_framework import viewsets

class Index(View):
    def get(self, request):
        return redirect('register')
    
class UserLoginView(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request):
        if not firebase_admin._apps:
            cred = credentials.Certificate(senv.CREDENTIALS_JSON)
            app = firebase_admin.initialize_app(cred)
        data = json.loads(request.body)
        if "firebase_id" not in data:
            return Response({"message": "Insufficient Query Params"}, status = status.HTTP_400_BAD_REQUEST)
        firebase_id = data["firebase_id"]
        try:
            user = auth.get_user(firebase_id)
            email = user.email
            app_user = AppUser.objects.filter(auth_user__email = email)
            if not app_user.exists():
                new_user, created = User.objects.get_or_create(username = email, email = email)
                app_user = AppUser.objects.create(auth_user = new_user)
            else:
                app_user = app_user[0]
                
            if not app_user.auth_user:
                return Response({"message": "Couldn't get access token"}, status = status.HTTP_400_BAD_REQUEST)
            if not app_user.auth_user.is_active:
                return Response({"message": "This account doesn't exist"}, status = status.HTTP_400_BAD_REQUEST)
            
            refresh = RefreshToken.for_user(app_user.auth_user)
            response = Response({'access': str(refresh.access_token), 'refresh': str(refresh), 'Static_ID': app_user.static_id, "access_lifetime": SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'], "refresh_lifetime": SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']}, status=status.HTTP_200_OK)
            response.set_cookie('jwt', refresh.access_token, httponly=False, secure=True, samesite='None')
            return response
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = Response({"message": "Logout Successful"},status=status.HTTP_200_OK)
        response.delete_cookie('jwt')
        return response
        

class ChatRequestViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = ChatRequestSerializer
    
    def get_queryset(self):
        return ChatRequest.objects.all()
    
    def list(self, request, *args, **kwargs):
        try:
            qs = self.get_queryset()
            user = AppUser.objects.filter(auth_user = request.user).first()
            qs = qs.filter(reciever = user)
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" : str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request):
        data = request.body
        if "new_status" not in data:
            return Response({"message": "Insufficient Query Params"}, status = status.HTTP_400_BAD_REQUEST)
        try:
            super().create(request)
            return Response({"message":"Updated"}, status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
        
            
            
        