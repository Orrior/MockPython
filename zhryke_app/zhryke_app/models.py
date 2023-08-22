from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    edit_date = models.DateTimeField("date edited", null=True, default=None, blank=True)

    def __str__(self):
        return f"User: {self.username}, Message: {self.text}"

    def is_edited(self) -> bool:
        return self.pub_date != self.edit_date
