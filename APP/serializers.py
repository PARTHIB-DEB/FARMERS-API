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
    
    def create(self, validated_data):
        family_object = family.objects.create(**validated_data)
        child_data = validated_data.pop('child_names')
        child.objects.create(family_object=family_object, **child_data)
        cow_data = validated_data.pop('cow_names')
        cow.objects.create(family_object=family_object, **cow_data)
        sheap_data = validated_data.pop('sheap_names')
        sheap.objects.create(family_object=family_object, **sheap_data)
        goat_data = validated_data.pop('goat_names')
        goat.objects.create(family_object=family_object, **goat_data)
        return family_object
        