from rest_framework import serializers
from django.contrib.auth.models import User
from Projects.models import Profile

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='profile.department')
    monthly_salary = serializers.IntegerField(source='profile.monthly_salary')
    tech_stack = serializers.CharField(source='profile.tech_stack')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'department', 'monthly_salary', 'tech_stack')
