from django.db import models
from django.conf import settings


class Todo(models.Model):
    text = models.CharField(max_length=50)
    # user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
