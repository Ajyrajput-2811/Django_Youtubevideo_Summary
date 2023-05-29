from django.contrib import admin
from summarizer.models import *

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Video,VideoAdmin)


