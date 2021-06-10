from django.db import models


class Select(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)
    geom = models.TextField()
    inside_only = models.BooleanField(default=False)
    intersection_layers = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        pass
