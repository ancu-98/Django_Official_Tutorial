from django.contrib import admin
from .models import Question

# Register your models here.

admin.site.site_header = "Polls Admin"
admin.site.site_title = "The world's slicket Admin Panel"
admin.site.index_title = "New Title"

admin.site.register(Question)