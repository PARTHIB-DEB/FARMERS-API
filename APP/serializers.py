from APP.models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields = ["child_name"]

class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = cow
        fields = ["cow_name"]


class SheapSerializer(serializers.ModelSerializer):
    class Meta:
        model = sheap
        fields = ["sheap_name"]


class GoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = goat
        fields = ["goat_name"]

class FamilySerializer(serializers.ModelSerializer):
    child_names = ChildSerializer()
    cow_names = CowSerializer()
    sheap_names = SheapSerializer()
    goat_names = GoatSerializer()

    class Meta:
        model = family
        fields = [
            "Farmer",
            "Wife",
            "children",
            "child_names",
            "cows",
            "cow_names",
            "sheaps",
            "sheap_names",
            "goats",
            "goat_names",
        ]
        validators = [
            UniqueTogetherValidator(queryset=family.objects.all(), fields=["Farmer"])
        ]
    
    def create(self, validated_data):
        child_data = validated_data.pop('child_names')
        cow_data = validated_data.pop('cow_names')
        sheap_data = validated_data.pop('sheap_names')
        goat_data = validated_data.pop('goat_names')

        # Create child, cow, sheap and goat objects
        child_obj = child.objects.create(**child_data)
        cow_obj = cow.objects.create(**cow_data)
        sheap_obj = sheap.objects.create(**sheap_data)
        goat_obj = goat.objects.create(**goat_data)

        # Create family object with the nested objects
        fam = family.objects.create(
            child_names=child_obj,
            cow_names=cow_obj,
            sheap_names=sheap_obj,
            goat_names=goat_obj,
            **validated_data
        )
        return fam

