from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Quiz(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    options = models.JSONField()  # Assuming you store options as a JSON array
    correct_option = models.IntegerField()

    def __str__(self):
        return self.question
