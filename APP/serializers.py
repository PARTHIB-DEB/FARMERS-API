from APP.models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields = ['child_name']     
        
class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = cow
        fields = ['cow_name']

class SheapSerializer(serializers.ModelSerializer):
    class Meta:
        model = sheap
        fields = ['sheap_name']

class GoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = goat
        fields = ['goat_name']

class FamilySerializer(serializers.ModelSerializer):
    child_names=ChildSerializer()
    cow_names=CowSerializer()
    sheap_names=SheapSerializer()
    goat_names=GoatSerializer()
    class Meta:
        model = family
        fields = ['Farmer','Wife','children','child_names','cows','cow_names','sheaps','sheap_names','goats','goat_names']
        validators = [
            UniqueTogetherValidator(
                queryset=family.objects.all(),
                fields=['Farmer']
            )
        ]