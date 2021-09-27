from django.contrib import admin

from posts.models import *


# Register your models here.
@admin.register(TypeofPet)
class TypeofPetAdmin(admin.ModelAdmin):
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
    list_display = ('pet', 'description',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Post Information', {
            'fields': ('profile_id', 'pet', 'description',),
        }),
    ]
    formfield_querysets = {
        'profile_id': lambda: Profile.objects.all(),
        'pet': lambda: Pet.objects.all(),
    }


@admin.register(PostFound)
class PostLostAdmin(admin.ModelAdmin):
    list_display = ('pet', 'description',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Post Information', {
            'fields': ('profile_id', 'pet', 'description', 'found_by', 'contact_no', 'location'),
        }),
    ]

    formfield_querysets = {
        'profile_id': lambda: Profile.objects.all(),
        'pet': lambda: Pet.objects.all(),
    }


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_pet',)
    list_per_page = 10
    ordering = ('-created_at',)
    fieldsets = [
        ('Pet Information', {
            'fields': ('name', 'age', 'gender', 'height', 'image', 'is_done', 'is_found', 'type_of_pet'),
        }),
    ]

    formfield_querysets = {
        'type_of_pet': lambda: TypeofPet.objects.all(),
    }


# admin.site.headers = 'BCCT School Admin'
