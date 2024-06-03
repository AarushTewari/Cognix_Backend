from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, username=validated_data['email'])
        AppUser.objects.create(auth_user = user)
        return user
    
class ChatRequestSerializer(serializers.ModelSerializer):
    reciever = serializers.CharField(write_only = True)
    
    class Meta:
        model = ChatRequest
        fields = ['static_id', 'reciever', 'status']
    
    def create(self, validated_data):
        reciever = validated_data.pop("reciever")
        reciever_instance = AppUser.objects.filter(static_id = reciever).first()
        sender_instance = AppUser.objects.filter(auth_user = self.context['request'].user).first()
        validated_data["reciever"]  = reciever_instance
        validated_data["sender"] = sender_instance
        return ChatRequest.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        instance.status = validate_data['new_status']
        instance.save()
        return instance