from rest_framework import serializers
from django.contrib.auth.models import User
from Projects.models import Profile
from django.utils.text import slugify

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
       model = Profile
       fields = ('department', 'monthly_salary', 'tech_stack', 'profile_photo')

class AddUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        username = slugify(first_name + last_name)
    
        user = User.objects.create(username=username, **validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
