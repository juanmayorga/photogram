# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# models
from users.models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # orden en que se despliegan los datos en el admin django en los perfiles
    list_display = ('pk', 'user', 'website', 'phone_number', 'picture')
    list_display_links = ('pk', 'user', 'phone_number')

    # formas de buscar registros
    search_fields = ('user__email', 'user__first_name',
                     'user__username', 'user__phone_number')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra Information', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Date data', {
            'fields': (('created', 'modified'),)
        }),
    )

    # Datos no editables en el admin
    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
