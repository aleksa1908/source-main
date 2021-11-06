from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class UserAdmin(UserAdmin):
    model = User
    search_fields = ('email', 'first_name', 'last_name')
    list_display = ('email', 'get_full_name')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = []
    filter_horizontal = ('groups', 'permissions')

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'created_at', 'updated_at')
        }),
        ('Additional Data', {
            'classes': ('wide',),
            'fields': ('image', 'about', 'date_of_birth')
        }),

        ('Permissions', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('is_active', 'is_staff', 'is_admin'), 'groups', 'permissions')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'image', 'about', 'date_of_birth',
                       'is_active', 'is_staff', 'is_admin', 'groups', 'permissions')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super(UserAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(User, UserAdmin)
