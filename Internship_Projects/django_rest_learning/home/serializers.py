from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Color
        fields = ['color']

class PeaopleSerializer(serializers.ModelSerializer):
    
    color = ColorSerializer(many = False,required = False)
    aaa = serializers.SerializerMethodField()

    class Meta:

        model = models.Person
        # fields = "__all__"
        fields = ['name','age','color','aaa']
        # depth = 1
    
    def get_aaa(self,obj):

        return 'India'

    def validate(self,data):

        speacial_character = "!@#$%^&*()_=-+?/>,<.|"
        if any(c in speacial_character for c in data['name']):
            raise serializers.ValidationError('name cannot contain special chars')

        if data['age'] < 18:

            raise serializers.ValidationError('Age must be greater than 18')
        
        return data
    
class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                serializers.ValidationError('username is already taken')

        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                serializers.ValidationError('email is already taken')

        return data
    
    def create(self , data):
        user = User.objects.create(username = data['username'],email = data['email'])
        user.set_password(data["password"])
        return data

