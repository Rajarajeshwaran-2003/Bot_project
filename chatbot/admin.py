from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ChatHistory

# Extend or customize User admin if needed
# admin.site.unregister(User)
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     pass

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_message', 'bot_response', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'user_message', 'bot_response')
    readonly_fields = ('timestamp',)

# Optionally, register User with default configuration
# admin.site.register(User, UserAdmin)
