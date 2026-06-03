from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import DeliveryTracking
from .serializers import DeliveryTrackingSerializer

class DeliveryTrackingViewSet(viewsets.ModelViewSet):
    queryset = DeliveryTracking.objects.all()
    serializer_class = DeliveryTrackingSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request, pk=None):
        tracking = self.get_object() # [cite: 26]
        new_status = request.data.get('status')
        
        valid_statuses = [choice[0] for choice in DeliveryTracking.DELIVERY_STATUS] # [cite: 26]
        if new_status not in valid_statuses:
            return Response({"error": "Invalid delivery status value"}, status=status.HTTP_400_BAD_REQUEST) # [cite: 26]
            
        tracking.status = new_status
        tracking.save() # [cite: 26]
     
        if new_status == 'DELIVERED':
            tracking.order.status = 'Completed' # Aligned with explicit choice matrix fields [cite: 27]
            tracking.order.save() # [cite: 27]
            
        return Response({"message": f"Status updated to {new_status}"}) # [cite: 27]