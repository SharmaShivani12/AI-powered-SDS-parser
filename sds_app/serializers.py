from rest_framework import serializers
from .models import SDSRecord

class SDSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDSRecord
        fields = '__all__'
