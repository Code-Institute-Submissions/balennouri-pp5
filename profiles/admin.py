from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "message",
        "created_at",
    )

    ordering = ("name",)


admin.site.register(ContactForm, ContactFormAdmin)
