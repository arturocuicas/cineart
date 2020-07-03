from django.db import models

LANGUAGES = [
    ("es", "Spanish"),
    ("en", "English"),
    ("fr", "French")
]


class Subtitle(models.Model):
    """Subtitle Model"""

    language = models.CharField(
        "Language", 
        choices=LANGUAGES, 
        max_length=2
    )
    
    text = models.FileField(
        "Text",
        upload_to="subtitles/"
    )

    movie = models.ForeignKey(
        "movies.Movie", 
        related_name="subtitles",
        verbose_name="Movie",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Return Language"""

        return self.language