from django.contrib import admin
from .models import Album, Artist

# Register models so they appear in the Django admin interface
admin.site.register(Album)
admin.site.register(Artist)
