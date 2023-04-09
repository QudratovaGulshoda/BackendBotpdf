from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'telegram_id','status','added']
    search_fields = ['first_name', 'telegram_id']
    list_filter = ['added','status']
    list_per_page = 10