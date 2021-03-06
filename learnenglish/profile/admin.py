from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email')

    fieldsets = ((None, {'fields': ('username', 'email', 'password')}),)

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )


admin.site.register(User, UserAdmin)
