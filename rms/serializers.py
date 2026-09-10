from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField()
   
   def create(self,validated_data):
      return Category.objects.create(**validated_data)
      # return Category.objects.create(name = validated_data.get('name'), description = validated_data.get('description'))

# validated_data = {'name':"Food",'description':"Food Category"}  # instance/object
# PUT:   validated_data = {'name':"Foods",'description':"Food Category"}
# PATCH:   validated_data = {'name':"Foods"}

   def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.save()
      return instance