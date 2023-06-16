from rest_framework import serializers
from django.contrib.auth.models import User
from Projects.models import Profile
from django.utils.text import slugify

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
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            first_name = validated_data.get('first_name', '')
            last_name = validated_data.get('last_name', '')
            username = slugify(first_name + last_name)
            
            user = User.objects.create(username=username, **validated_data)
            
            profile = profile_serializer.save(user=user.instance)
            
            return user
        else:
            raise serializers.ValidationError(profile_serializer.errors)






    






{
"first_name":"Tea",
"last_name":"Tea",
"profile": {
    "department":"Design",
"tech_stack":"UX/UI",
"monthly_salary":"1500.00"
}

}