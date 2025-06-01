from django.contrib import admin
from .models import SDSRecord

@admin.register(SDSRecord)
class SDSRecordAdmin(admin.ModelAdmin):
    list_display = ("product_name", "manufacturer", "cas_number", "uploaded_at")
    search_fields = ("product_name", "cas_number", "manufacturer")
    list_filter = ("uploaded_at",)
    ordering = ("-uploaded_at",)
