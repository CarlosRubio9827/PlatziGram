# Django

from django.contrib import admin

# Models

from users.models import Profile

# Register yoru models here
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user','phone_number')
    list_editable = ('picture','website')
    search_fields = ('user__email','user__first_name','user__last_name','phone_number')
    list_filter = ('created', 'modified')