from django.db import models
from django.utils import timezone
from django.conf import settings


class Workshop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    detail = models.TextField()
    do_date = models.DateField(default=timezone.now())
    machines = (
        ('LC', 'レーザー加工機'),
        ('3D', '3Dプリンタ'),
        ('MM', 'ミリングマシン'),
    )
    used_machine = models.CharField(max_length=2, choices=machines)
    duration_time = models.DurationField()
    requirements = models.CharField(max_length=300)

    def __str__(self):
        return self.title
