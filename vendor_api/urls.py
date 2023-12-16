from django.urls import path
from .apiviews import VendorListAPI
from .apiviews import VendorDetailsAPI
from .apiviews import PurchaseOrderListAPI
from .apiviews import PurchaseOrderDetailsAPI
from .apiviews import HistoricalPerformanceAPI


urlpatterns = [
    path('vendor/', VendorListAPI.as_view(), name='vendor-list'),
    path('vendor/<int:vendor_id>/', VendorDetailsAPI.as_view(), name='vendor-details'),
    path('purchase_order/', PurchaseOrderListAPI.as_view(),name='purchase-list'),
    path('purchase_order/<int:po_id>/', PurchaseOrderDetailsAPI.as_view(),name='purchase-details'),
    path('vendor/<int:vendor_id>/performance/', HistoricalPerformanceAPI.as_view(),name='performance'),
]
