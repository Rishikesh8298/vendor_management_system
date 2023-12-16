
from .models import PurchaseOrder
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, created, **kwargs):
    with transaction.atomic():
        if instance.status == 'completed':
            vendor = instance.vendor
            vendor.on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
            vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, created, **kwargs):
    with transaction.atomic():
        if instance.quality_rating is not None and instance.status == 'completed':
            vendor = instance.vendor
            vendor.quality_rating_avg = vendor.calculate_quality_rating_avg()
            vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    with transaction.atomic():
        if instance.acknowledgment_date is not None:
            vendor = instance.vendor
            vendor.average_response_time = vendor.calculate_average_response_time()
            vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfilment_rate(sender, instance, created, **kwargs):
    with transaction.atomic():
        vendor = instance.vendor
        vendor.fulfilment_rate = vendor.calculate_fulfilment_rate()
        vendor.save()
