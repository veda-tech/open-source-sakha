import uuid

from django.db import models


class AbstractModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField("Время создания", auto_now_add=True)
    updated = models.DateTimeField("Время обновления", auto_now=True)

    class Meta:
        abstract = True
