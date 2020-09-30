from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Account

class AccountAdmin(BaseUserAdmin):

    # The fields to be used in displaying the Account model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_staff','is_admin')
    search_fields = ('email', 'username')

    readonly_fields=( 'last_login', 'date_joined')

    list_filter = ('is_admin',)
    ordering = ('email',)
    filter_horizontal = ()
    
admin.site.register(Account, AccountAdmin)