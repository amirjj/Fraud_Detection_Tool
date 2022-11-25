from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import POSerializer
from .models import PO

class POViewSet(viewsets.ModelViewSet):
    serializer_class = POSerializer
    queryset = PO.objects.all()
    permission_classes = [permissions.IsAuthenticated]
