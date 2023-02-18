from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError 


def validate_date(value):

    if value < timezone.now():
        raise ValidationError(
            "Essa data/hora não pode ser em um periódo já ultrapassada!"
        )

class Task(models.Model):

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField('Título', max_length=150, blank=False, null=False)
    description = models.TextField('Descrição')
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    start_date_task = models.DateTimeField('Data de início da tarefa', 
        help_text='Data/hora em que a tarefa terá sua execução iniciada.',
        validators=[validate_date]
    )
    deadline_date = models.DateTimeField('Data prazo',
        help_text='Data/hora em que a tarefa deve ser feita'+
        ' ou em que ela deve está concluída.',
        validators=[validate_date]
    )
    date_conclusion = models.DateTimeField('Data de conclusão', null=True)
    startup_date = models.DateTimeField('Data de inicialização', null=True)
    status = models.BooleanField('Status', default=False)
    punctuality = models.BooleanField('Pontualidade', default=False)
    start_task = models.BooleanField('Iniciar tarefa', default=False)

    def __str__(self) -> str:
        return self.title
    
    def save(self) -> None:

        if self.start_date_task == self.deadline_date:
            raise ValidationError(
                "Data/hora de inicio e Data/hora prazo não podem ser iguais."
            )

        return super().save()