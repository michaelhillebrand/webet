from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('created at', null=False, auto_now_add=True, blank=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by_related", related_query_name="%(app_label)s_%(class)ss_created_by", null=False, on_delete=models.DO_NOTHING)
    modified_at = models.DateTimeField('modified at', null=False, auto_now_add=True, blank=True)
    modified_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_modified_by_related", related_query_name="%(app_label)s_%(class)ss_modified_by", null=False, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
