from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing
from .serializer import ThingSerializer
from .permissions import isOwnerOrReadOnly


class ThingList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
