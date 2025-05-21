from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'city', 'state', 'pin_code']
    search_fields = ['user__username', 'user__email', 'phone_number', 'address', 'city', 'state', 'pin_code']
