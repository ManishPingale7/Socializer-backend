from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'description', 'address',
                  'contact_info', 'interests', 'photo', 'latitude', 'longitude', 'username']

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get(
                'description', instance.description)
            instance.address = validated_data.get('address', instance.address)
            instance.contact_info = validated_data.get(
                'contact_info', instance.contact_info)
            instance.interests = validated_data.get(
                'interests', instance.interests)
            instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
