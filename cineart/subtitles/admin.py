from django.contrib import admin

from cineart.subtitles.models import Subtitle


@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    list_display = ["language", "movie"]
    list_display_links = ["language", "movie"]
    search_fields = ["language", "movie"]
    list_per_page = 20
