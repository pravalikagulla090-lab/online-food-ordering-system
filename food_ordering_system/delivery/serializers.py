from rest_framework import serializers
from .models import DeliveryTracking, DeliveryAgent

class DeliveryAgentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username') # [cite: 24]

    class Meta:
        model = DeliveryAgent
        fields = ['id', 'username', 'is_available', 'vehicle_number'] # [cite: 24]

class DeliveryTrackingSerializer(serializers.ModelSerializer):
    agent_details = DeliveryAgentSerializer(source='agent', read_only=True) # [cite: 24]

    class Meta:
        model = DeliveryTracking
        fields = ['id', 'order', 'agent', 'agent_details', 'status', 'estimated_delivery_time', 'updated_at'] # [cite: 25]