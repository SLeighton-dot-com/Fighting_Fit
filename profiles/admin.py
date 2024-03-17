from django.contrib import admin
class NewsletterSubscriber(admin.ModelAdmin):
    list_display = (
        'email',
    )
