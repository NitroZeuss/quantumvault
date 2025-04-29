from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import File
from .serializers import FileSerializer
import cloudinary.uploader

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cloudinary_response = cloudinary.uploader.upload(file)
            file_url = cloudinary_response.get('secure_url')

            new_file = File.objects.create(
                user=request.user,
                file_name=file.name,
                file_url=file_url
            )

            serializer = self.get_serializer(new_file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
