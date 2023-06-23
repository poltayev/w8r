from rest_framework import serializers
from .models import Branch, MenuCategory, Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'logo_path']
    
class BranchSerializer(serializers.ModelSerializer):
    addr = serializers.CharField(max_length=250, source='address')
    restaurant = serializers.HyperlinkedRelatedField(
        queryset=Restaurant.objects.all(),
        view_name='merchants-detail'
    )
    
    class Meta:
        model = Branch
        fields = ['id', 'restaurant', 'addr']

class MenuCategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        branch_id = self.context['branch_id']
        return MenuCategory.objects.create(branch_id=branch_id, **validated_data)
    
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'branch']
    