# from django.db import models
#
#
# class Word(models.Model):
#     definition = models.Textfield()
#     author = models.Charfield(max_length=255)
#     word = models.Charfield(max_length=255)
#     written_on = models.DateTimeField()
#     example = models.TextField()
#
#     def __str__(self):
#         return self.word
from django.db import models

class Word(models.Model):
    definition = models.TextField()  # Corrected the typo here
    author = models.CharField(max_length=255)  # Corrected the typo here
    word = models.CharField(max_length=255)  # Corrected the typo here
    written_on = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.word