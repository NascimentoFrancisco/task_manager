from django.db import models
from django.conf import settings 


class Task(models.Model):

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField('Título', max_length=150, blank=False, null=False)
    description = models.TextField('Descrição')
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    date_conclusion = models.DateTimeField('Data de conclusão', auto_now=True)
    status = models.BooleanField('Status', default=False)

    def __str__(self) -> str:
        return self.title
    