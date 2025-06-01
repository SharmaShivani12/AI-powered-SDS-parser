from django.db import models

class SDSRecord(models.Model):
    product_name = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    cas_number = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    application = models.TextField(null=True, blank=True)
    hazard_statements = models.TextField(null=True, blank=True)
    composition = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name or "Unnamed SDS"
