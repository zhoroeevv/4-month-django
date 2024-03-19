from django.db import models

class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255
    )
    
    class Meta:
        verbose_name = "Данные пользователя"