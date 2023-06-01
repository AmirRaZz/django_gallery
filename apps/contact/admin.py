from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ['first_name', 'last_name', 'email_address', 'subject', 'message','contact_time']

    list_display = ['subject', 'contact_time', 'responded_to', 'resolved']
    list_filter = ['responded_to', 'resolved']

    search_fields = ['email_address', 'subject', 'message']
    search_help_text = "Search email addresses, subjects, and messages."