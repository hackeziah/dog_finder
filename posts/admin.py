from django.contrib import admin

from posts.models import *


# Register your models here.
@admin.register(BreedType)
class BreedTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_per_page = 10
    ordering = ('name',)

    fieldsets = [
        ('Details', {'fields': [
            'name', 'description']})
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'contact_no',)
    list_per_page = 10
    ordering = ('last_name',)
    readonly_fields = (
        'get_full_name',
    )
    fieldsets = [
        ('Personal Information', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'contact_no', 'address'),
        }),
    ]

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = "Full Name"


@admin.register(PostLost)
class PostLostAdmin(admin.ModelAdmin):
    list_display = ('dog', 'description',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Post Information', {
            'fields': ('profile_id', 'dog', 'description',),
        }),
    ]
    formfield_querysets = {
        'profile_id': lambda: Profile.objects.all(),
        'dog': lambda: Dog.objects.all(),
    }


@admin.register(PostFound)
class PostLostAdmin(admin.ModelAdmin):
    list_display = ('dog', 'description',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Post Information', {
            'fields': ('profile_id', 'dog', 'description', 'found_by', 'contact_no', 'location'),
        }),
    ]

    formfield_querysets = {
        'profile_id': lambda: Profile.objects.all(),
        'dog': lambda: Dog.objects.all(),
    }


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed_type',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Dog Information', {
            'fields': ('name', 'age', 'gender', 'height', 'image', 'is_done', 'is_found', 'breed_type'),
        }),
    ]

    formfield_querysets = {
        'breed_type': lambda: BreedType.objects.all(),
    }


admin.site.headers = 'BCCT School Admin'
