from django.db import models
from django.contrib.auth.models import *

class Message(models.Model):
    datetime = models.DateTimeField()
    taker = models.ForeignKey(User, related_name='taker')
    sender = models.ForeignKey(User, related_name='sender')
    message = models.TextField()

    def __unicode__(self):
        return self.message
