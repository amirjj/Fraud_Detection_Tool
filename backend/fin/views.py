from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import POSerializer, DupAmountSameSupSerializer, SplitPOSerializer, \
    SumOfPOPerSupSerializer, POCountPerSupSerializer
from .models import PO

#TODO
#Check using same Serializer working well?
class POViewSet(viewsets.ModelViewSet):
    serializer_class = POSerializer
    queryset = PO.custom_manager.get_all_pos()
    permission_classes = [permissions.IsAuthenticated]

class DupAmntSameSupDetailViewSet(viewsets.ModelViewSet):
    serializer_class = POSerializer
    queryset = PO.custom_manager.duplicate_amount_same_supplier_detail()
    permission_classes = [permissions.IsAuthenticated]

class DupAmountSameSupViewSet(viewsets.ModelViewSet):
    serializer_class = DupAmountSameSupSerializer
    queryset = PO.custom_manager.duplicate_amount_same_supplier()
    permission_classes = [permissions.IsAuthenticated]

class SplitPOViewSet(viewsets.ModelViewSet):
    serializer_class = SplitPOSerializer
    queryset = PO.custom_manager.split_po()
    permission_classes = [permissions.IsAuthenticated]

class SumOfPOPerSupViewSet(viewsets.ModelViewSet):
    serializer_class = SumOfPOPerSupSerializer
    queryset = PO.custom_manager.sum_of_po_amounts_per_supp()
    permission_classes = [permissions.IsAuthenticated]

class POCountPerSupViewSet(viewsets.ModelViewSet):
    serializer_class = POCountPerSupSerializer
    queryset = PO.custom_manager.po_count_per_supp()
    permission_classes = [permissions.IsAuthenticated]