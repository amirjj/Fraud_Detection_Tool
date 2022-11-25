from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import POSerializer
from .models import PO

#TODO
#Check using same Serializer working well?
class POViewSet(viewsets.ModelViewSet):
    serializer_class = POSerializer
    queryset = PO.custom_manager.get_all_pos()
    permission_classes = [permissions.IsAuthenticated]

class DupAmntSameSupViewSet(viewsets.ModelViewSet):
    serializer_class = POSerializer
    queryset = PO.custom_manager.duplicate_amount_same_supplier()
    permission_classes = [permissions.IsAuthenticated]

