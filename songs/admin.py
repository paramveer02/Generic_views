from django.contrib import admin

from .models import Album, Artist

admin.site.register(Album)


class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ("first_name", "last_name", "instrument", "full_name")

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


admin.site.register(Artist, ArtistAdmin)
