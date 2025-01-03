from django.contrib import admin

from django.contrib import admin
from .models import Listing, ListingImage


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1  # Allows adding one image initially

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'address')
