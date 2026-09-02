from rest_framework import serializers
from .models import Blog, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class BlogSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(read_only = True) #Respresenting category relationship
    author = UserSerializer(read_only = True) #Respresenting user relationship
    class Meta:
        model = Blog
        fields =    '__all__'

