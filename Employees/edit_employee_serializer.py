from rest_framework import serializers
from django.contrib.auth.models import User
from Projects.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('department', 'monthly_salary', 'tech_stack')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile_instance = instance.profile

        for key, value in profile_data.items():
            setattr(profile_instance, key, value)

        profile_instance.save()

        return super().update(instance, validated_data)





