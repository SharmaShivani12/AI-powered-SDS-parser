from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets
import os, uuid
from django.conf import settings
from .models import SDSRecord
from .serializers import SDSRecordSerializer
from .parser import parse_sds

class SDSRecordViewSet(viewsets.ModelViewSet):
    queryset = SDSRecord.objects.all()
    serializer_class = SDSRecordSerializer

class SDSUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        upload_dir = os.path.join(settings.BASE_DIR, 'sds_files')
        os.makedirs(upload_dir, exist_ok=True)

        filename = f"{uuid.uuid4()}_{uploaded_file.name}"
        upload_path = os.path.join(upload_dir, filename)

        with open(upload_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        sds_data = parse_sds(upload_path)
        print("✅ Parsed SDS Data:", sds_data)

        try:
            record = SDSRecord.objects.create(**sds_data)
            return Response(SDSRecordSerializer(record).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
