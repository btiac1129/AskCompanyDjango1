from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return f'<img src="{post.photo.url}" />'
        return None

    def message_length(self, post):
        return f"{len(post.message)}글자"
    message_length.short_description = '메시지 글자 수'

# admin.site.register(Post, PostAdmin)
