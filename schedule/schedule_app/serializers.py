from rest_framework import serializers
from collections import defaultdict
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data): 
        instance.title = validated_data.get('title', instance.title)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.number = validated_data.get('number', instance.number)
        instance.day_of_week = validated_data.get('day_of_week', instance.day_of_week)
        instance.save()
        return instance
    
    