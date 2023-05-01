from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing
from .serializer import ThingSerializer


class ThingList(ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
