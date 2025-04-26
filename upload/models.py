from django.db import models
from django.contrib.auth.models import User

## Write the views below

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate the file with a user
    file_name = models.CharField(max_length=255)
    file_url = models.URLField()  # Cloudinary URL to the uploaded file
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
