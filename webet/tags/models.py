from django.db import models

from base.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name
