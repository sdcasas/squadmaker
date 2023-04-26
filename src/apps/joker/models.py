from django.db import models


class Joker(models.Model):

    class JokerType(models.TextChoices):
        CHUCK = 'CHUCK', 'Chuck'
        DAD = 'DAD', 'Dad'

    number = models.AutoField(primary_key=True)
    value = models.TextField()
    joker_type = models.CharField(max_length=50, choices=JokerType.choices, blank=True, null=True)
    joker_id = models.CharField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.number} - {self.joker_type}: {self.value[:30]}"