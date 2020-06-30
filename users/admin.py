from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    search_fields = ('first_name', 'last_name', 'email')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'gender', ]
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'image')}),
        (_('Permissions'), {
            'fields': ('is_admin', ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
