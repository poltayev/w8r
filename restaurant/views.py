from django.shortcuts import render, get_object_or_404

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Branch, MenuCategory, Restaurant
from .serializers import BranchSerializer, MenuCategorySerializer, RestaurantSerializer 

class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.all()
        
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.select_related('restaurant').all()
    serializer_class = BranchSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class MenuViewSet(ModelViewSet):
    serializer_class = MenuCategorySerializer

    def get_queryset(self):
        return MenuCategory.objects.filter(branch_id=self.kwargs['branch_pk'])
    
    def get_serializer_context(self):
        return {'branch_id': self.kwargs['branch_pk']}