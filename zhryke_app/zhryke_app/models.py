from django.db import models
from datetime import datetime

class Message(models.Model):
    owner = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published", auto_now_add=True, blank=True)
    edit_date = models.DateTimeField("date edited", auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"User: {self.username}, Message: {self.text}"

    def is_edited(self) -> bool:
        return self.pub_date != self.edit_date
