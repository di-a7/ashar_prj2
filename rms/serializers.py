from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      # fields = '__all__'
      fields = ['id', 'name']
      # exclude = ['id']


class FoodSerializer(serializers.ModelSerializer):
   price_with_vat = serializers.SerializerMethodField()
   # category = CategorySerializer()
   # category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   # category = serializers.StringRelatedField(read_only=True)
   class Meta:
      model = Food
      fields = ['id', 'name', 'description', 'price', 'price_with_vat', 'category']
   
   def get_price_with_vat(self, obj):
      return (obj.price * 0.12) + obj.price
   
   # create a method to calculate price with 10 percent discount, add field, method name should start with get_ followed by field name and include it in the fields



# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self,validated_data):
#       return Category.objects.create(**validated_data)
#       # return Category.objects.create(name = validated_data.get('name'), description = validated_data.get('description'))

# # validated_data = {'name':"Food",'description':"Food Category"}  # instance/object
# # PUT:   validated_data = {'name':"Foods",'description':"Food Category"}
# # PATCH:   validated_data = {'name':"Foods"}

#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name', instance.name)
#       instance.save()
#       return instance