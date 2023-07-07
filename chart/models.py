from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    biography = models.TextField()
    streaming_count =models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    # Other song-related fields can be added here

    def __str__(self):
        return self.title

class ChartEntry(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    peak_position = models.PositiveIntegerField()
    weeks_on_chart = models.PositiveIntegerField()
    # Other chart-related fields can be added here

    def __str__(self):
        return f"{self.song.title} - Position: {self.position}"
