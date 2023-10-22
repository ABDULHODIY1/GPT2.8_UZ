from django.db import models


class GPT(models.Model):
    messages=models.TextField(max_length=10000)

    def __str__(self):
        return str(self.messages)