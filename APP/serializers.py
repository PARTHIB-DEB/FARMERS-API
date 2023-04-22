from APP.models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = child
        fields = ["child_name"]

    # def create(self, validated_data):
    #     return validated_data


class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = cow
        fields = ["cow_name"]

    # def create(self, validated_data):
    #     return validated_data


class SheapSerializer(serializers.ModelSerializer):
    class Meta:
        model = sheap
        fields = ["sheap_name"]

    # def create(self, validated_data):
    #     return validated_data


class GoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = goat
        fields = ["goat_name"]

    # def create(self, validated_data):
    #     return validated_data


class FamilySerializer(serializers.ModelSerializer):
    name_child = ChildSerializer()
    name_cow = CowSerializer()
    name_sheap = SheapSerializer()
    name_goat = GoatSerializer()

    class Meta:
        model = family
        fields = [
            "Farmer",
            "Wife",
            "children",
            "name_child",
            "cows",
            "name_cow",
            "sheaps",
            "name_sheap",
            "goats",
            "name_goat",
        ]
        validators = [
            UniqueTogetherValidator(queryset=family.objects.all(), fields=["Farmer"])
        ]

    def create(self, validated_data):
        childs = validated_data.pop("name_child")
        cows = validated_data.pop("name_cow")
        sheaps = validated_data.pop("name_sheap")
        goats = validated_data.pop("name_goat")
        child.objects.create(**childs)
        cow.objects.create(**cows)
        sheap.objects.create(**sheaps)
        goat.objects.create(**goats)
        print(type(validated_data))
        fam = family.objects.create(
            child_names=childs,
            cow_names=cows,
            sheap_names=sheaps,
            goat_names=goats,
            **validated_data
        )
        # fam=family.objects.create(child_names=childs,
        #                           cow_names=cows,
        #                           sheap_names=sheaps,
        #                           goat_names=goats,
        #                           **validated_data)
        return fam
