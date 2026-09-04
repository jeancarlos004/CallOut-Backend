from django.contrib import admin
from .models import BlockedCall

@admin.register(BlockedCall)
class BlockedCallAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'user', 'call_date', 'call_time', 'location_name')
    list_filter = ('call_date', 'user')
    search_fields = ('phone_number', 'location_name', 'user__username')
    ordering = ('-call_date', '-call_time')
