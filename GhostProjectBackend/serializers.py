from rest_framework import serializers
from PerformanceTab.models import Performance

class PerformanceSeliarizer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'