from django.contrib import admin

# Register your models here.
from posts.models import Post


# Register yoru models here
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    """Posts Admin model"""

    list_display = ('pk', 'user', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('picture',)
    list_filter = (
                'created',
                'modified'
    )