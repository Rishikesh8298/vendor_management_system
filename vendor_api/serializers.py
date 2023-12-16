from rest_framework.serializers import ModelSerializer
from .models import Vendor
from .models import PurchaseOrder
from .models import HistoricalPerformance


class PurchaseOrderSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ('po_number',)


class VendorSerializer(ModelSerializer):
    vendor = PurchaseOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ('vendor_code',)


class HistoricalPerformanceSerializer(ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
