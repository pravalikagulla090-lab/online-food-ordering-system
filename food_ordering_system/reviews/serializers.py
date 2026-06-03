from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='user.username') # [cite: 81]

    class Meta:
        model = Review # [cite: 82]
        fields = ['id', 'reviewer', 'restaurant', 'rating', 'comment', 'created_at'] # [cite: 82]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating integers must fall between 1 through 5.") # [cite: 82]
        return value