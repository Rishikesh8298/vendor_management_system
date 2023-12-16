from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0),
    ])
    quality_rating_avg = models.FloatField(default=0.0, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0),
    ])
    average_response_time = models.FloatField(default=0.0, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0),
    ])
    fulfillment_rate = models.FloatField(default=0.0, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0),
    ])

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.vendor.filter(status='completed')
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date'))
        return (on_time_deliveries.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    def calculate_quality_rating_avg(self):
        completed_pos = self.vendor.filter(status='completed', quality_rating__isnull=False)
        return completed_pos.aggregate(models.Avg('quality_rating'))['quality_rating__avg'] or 0

    def calculate_average_response_time(self):
        completed_pos = self.vendor.filter(acknowledgment_date__isnull=False)
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_pos]
        return sum(response_times) / len(response_times) if len(response_times) > 0 else 0

    def calculate_fulfilment_rate(self):
        total_pos = self.vendor.all()
        fulfilled_pos = total_pos.filter(status='completed')
        return (fulfilled_pos.count() / total_pos.count()) * 100 if total_pos.count() > 0 else 0

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = self.autogenerate_vendor_code()
        super().save(*args, **kwargs)

    def autogenerate_vendor_code(self):
        import random
        return f'VMS-{str(random.randint(1000000, 9999999))}'

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.deletion.CASCADE, related_name="vendor")
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=15, default='Pending')
    quality_rating = models.FloatField(default=0.0, validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0),
    ])
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = self.autogenerate_po_number()
        if not self.delivery_date:
            self.delivery_date = self.delivery_date_assign()
        super().save(*args, **kwargs)

    def autogenerate_po_number(self):
        import random
        return f'PO-{str(random.randint(100000000, 999999999))}'

    def delivery_date_assign(self):
        import datetime
        return datetime.datetime.now() + datetime.timedelta(days=7)

    def __str__(self):
        return self.po_number


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.deletion.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor
