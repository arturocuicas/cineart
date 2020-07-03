from django.db import models


class Movie(models.Model):
    """Movie model"""

    title = models.CharField(
        "Title",
        max_length=144
    )

    description = models.TextField(
        "Description",
        max_length=800
    )

    video = models.FileField(
        "Video",
        upload_to="videos/"
    )

    poster = models.FileField(
        "Poster",
        upload_to="poster/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return Movie Title"""

        return self.title