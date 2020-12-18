from django.contrib import admin

# Register your models here.


from app1.models import Image
from app1.models import myAudio

admin.site.register(Image)
admin.site.register(myAudio)
