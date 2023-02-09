from django.db import models
from django.utils import timezone
from django.conf import settings 


class Task(models.Model):

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField('Título', max_length=150, blank=False, null=False)
    description = models.TextField('Descrição')
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    deadline_date = models.DateTimeField('Data prazo',
        help_text='Data/hora em que a tarefa deve ser feita'+
        ' ou em que ela deve está concluída.'
    )
    date_conclusion = models.DateTimeField('Data de conclusão', null=True)
    status = models.BooleanField('Status', default=False)
    punctuality = models.BooleanField('Pontualidade', default=False)

    def __str__(self) -> str:
        return self.title
        