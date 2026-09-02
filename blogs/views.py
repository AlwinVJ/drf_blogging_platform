from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

class BlogList(APIView):
    
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs,many = True)
        
        return Response(serializer.data)


class BlogDetails(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        
        return Response(serializer.data)