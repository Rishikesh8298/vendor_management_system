from rest_framework.response import Response
from rest_framework import status
from .serializers import PurchaseOrderSerializer, VendorSerializer, HistoricalPerformanceSerializer
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class VendorListAPI(APIView):
    """
    Models: Vendor
    HTTP method: GET, POST
    Content-Type: application/json
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetailsAPI(APIView):
    """
        MODELs: Vendor
        HTTP method: GET, PUT, DELETE
        Content-Type: application/json
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PurchaseOrderListAPI(APIView):
    """
        MODELs: PurchaseOrder
        HTTP method: GET, POST
        Content-Type: application/json
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderDetailsAPI(APIView):
    """
        MODELs: PurchaseOrder
        HTTP method: GET, PUT, DELETE
        Content-Type: application/json
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except KeyError:
                return Response(serializer.errors)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HistoricalPerformanceAPI(APIView):
    """
        Models: HistoricalPerformance
        HTTP method: GET
        Content-Type: application/json
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id):
        try:
            vendor = HistoricalPerformance.objects.get(vendor=Vendor.objects.get(pk=vendor_id))
        except HistoricalPerformance.DoesNotExist:
            vendor_id = Vendor.objects.get(pk=vendor_id)
            history = HistoricalPerformance(vendor=vendor_id,
                                            date=datetime.datetime.now(),
                                            on_time_delivery_rate=vendor_id.on_time_delivery_rate,
                                            quality_rating_avg=vendor_id.quality_rating_avg,
                                            average_response_time=vendor_id.average_response_time,
                                            fulfillment_rate=vendor_id.fulfillment_rate,
                                            )
            history.save()
            serializer = HistoricalPerformanceSerializer(history)
            return Response(serializer.data)
        else:
            vendor_id = Vendor.objects.get(pk=vendor_id)
            history = HistoricalPerformance.objects.get(vendor=vendor_id)
            history.date = datetime.datetime.now()
            history.on_time_delivery_rate = vendor_id.on_time_delivery_rate
            history.quality_rating_avg = vendor_id.quality_rating_avg
            history.average_response_time = vendor_id.average_response_time
            history.fulfillment_rate = vendor_id.fulfillment_rate
            history.save()
            history = get_object_or_404(HistoricalPerformance, pk=vendor.pk)
            serializer = HistoricalPerformanceSerializer(history)
            return Response(serializer.data)
