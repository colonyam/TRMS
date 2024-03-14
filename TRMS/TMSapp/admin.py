from django.contrib import admin
from .models import Message
from django.contrib import admin
from .models import Driver
from .models import Profile
from .models import Message
admin.site.register(Driver)

admin.site.register(Message)
admin.site.register(Profile)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'timestamp')