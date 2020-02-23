from datetime import datetime
from .models import Flight, Booking
from .serializers import FlightSerializer,BookingSerializer
from rest_framework.generics import ListAPIView

class Flightlist(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class Bookinglist(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookingSerializer
