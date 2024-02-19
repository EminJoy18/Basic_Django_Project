from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'images') # after MEDIA configuration, this images folder will be formed within "media" folder
    # to load media files
    designation = models.CharField(max_length = 100)
    email_address = models.EmailField(max_length = 100, unique = True)
    phone_no = models.CharField(max_length = 12, blank = True)
    # setting blank = True, makes the field optional

    created_at = models.DateTimeField(auto_now_add = True)
    # auto_now_add is perfect for one-time modification of field
    # i.e. when model instance is created and saved for the first time
    updated_at = models.DateTimeField(auto_now = True) 
    # auto_now is good for whenever the field needs to be changed, model instance gets saved with current time


    def __str__(self):
        return self.first_name
    # so that in the admin panel, you see it as <first_name> in case of 'Employee Object(1)'