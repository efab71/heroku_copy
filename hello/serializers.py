from rest_framework import serializers
from hello.models import Main

class MainSerializer(serializers.Serializer):
    
    userId=serializers.CharField(max_length=100)
    timestamp= serializers.IntegerField()
    alt=serializers.FloatField()
    lng=serializers.FloatField()
    accSpeedX=serializers.FloatField()
    accSpeedY=serializers.FloatField()
    accSpeedZ=serializers.FloatField()
    
    def create(self, validated_data):
        return Main.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.userId=validated_data.get('userId', instance.title)
        instance.timestamp= validated_data.get('timestamp', instance.timestamp)
        instance.alt=validated_data.get('alt', instance.alt)
        instance.lng=validated_data.get('lng', instance.lng)
        instance.accSpeedX=validated_data.get('accSpeedX', instance.accSpeed)
        instance.accSpeedY=validated_data.get('accSpeedY', instance.accSpeed)
        instance.accSpeedZ=validated_data.get('accSpeedZ', instance.accSpeed)
        
    
