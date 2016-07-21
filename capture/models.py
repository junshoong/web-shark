from django.db import models

class Packet(models.Model):
    # date = models.DateTimeField('Packet time')
    context = models.BinaryField()

    def __str__(self):
        return self.context
