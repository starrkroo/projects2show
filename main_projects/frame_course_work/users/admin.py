from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'avatar')

admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Message)