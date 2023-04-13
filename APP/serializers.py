from APP.models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = family
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=family.objects.all(),
                fields = ['Farmer']
            )
        ]

class ChildSerializer(serializers.ModelSerializer):
    Parent=FamilySerializer()
    class Meta:
        model = child
        fields = '__all__'     
        
class CowSerializer(serializers.ModelSerializer):
    Parent=FamilySerializer()
    class Meta:
        model = cow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=cow.objects.all(),
                fields = ['cow_name']
            )
        ]

class SheapSerializer(serializers.ModelSerializer):
    Parent=FamilySerializer()
    class Meta:
        model = sheap
        fields = '__all__'

class GoatSerializer(serializers.ModelSerializer):
    Parent=FamilySerializer()
    class Meta:
        model = goat
        fields = '__all__'