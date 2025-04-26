from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import File
import cloudinary.uploader
from rest_framework import status

@api_view(['POST'])
def upload_file(request):
    if request.user.is_authenticated:
        file = request.FILES['file']  # Get the file from the request
        cloudinary_response = cloudinary.uploader.upload(file)  # Upload to Cloudinary
        file_url = cloudinary_response['secure_url']  # Get the file URL from Cloudinary

        # Save file metadata to SQLite database
        new_file = File.objects.create(
            user=request.user,
            file_name=file.name,
            file_url=file_url
        )

        return Response({'url': file_url}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
