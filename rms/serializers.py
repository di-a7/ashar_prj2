from rest_framework import serializers
from .models import *
from rest_framework.response import Response

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

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['id','food']

class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   total_price = serializers.FloatField(read_only=True)
   status = serializers.CharField(read_only=True)
   payment_status = serializers.BooleanField(read_only=True)
   items = OrderItemSerializer(many=True)
   class Meta:
      model = Order
      fields = ['id', 'user', 'quantity', 'total_price', 'status', 'payment_status','items']
      
   def create(self, validated_data):
      items = validated_data.pop('items')
      total_price = 0
      for i in items:
         food = Food.objects.get(pk = i.get('food').id)
         # total_price += food.price * i.get('quantity')
      order = Order.objects.create(user = validated_data.get('user'), quantity = validated_data.get('quantity'), total_price = total_price)
      for i in items:
         OrderItem.objects.create(order = order, food = i.get('food'))
      # OrderItem.objects.bulk_create([OrderItem(order = order, food = i.get('food')) for i in items])
      return order


# remodel Ordeitem:
# add quantity field in OrderItem and remove quantity from order

# validated_data = {
#    "quantity": 1,
# }

#    items =  {
#       "food": 11,
# "quantity": 2,
#    },{
#       "food": 12,
# "quantity": 1
#    }







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