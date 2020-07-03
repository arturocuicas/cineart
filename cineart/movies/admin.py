from django.contrib import admin

from cineart.movies.models import Movie
from cineart.subtitles.models import Subtitle


class SubtitleInline(admin.StackedInline):
    model = Subtitle
    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_display_links = ["title", "created_at"]
    search_fields = ["title", "created_at"]
    list_per_page = 20
    inlines = [SubtitleInline]
