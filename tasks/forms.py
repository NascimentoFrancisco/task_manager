from django import forms
from .models import Task

class CreateUpdadteTask(forms.ModelForm):


    class Meta:
        

        model = Task
        fields = ['title', 'start_date_task', 'deadline_date', 'description']

        widgets = {
            'title':forms.TextInput(),
            'deadline_date':forms.TextInput(
                attrs={'type':'datetime-local'}
            ),
            'start_date_task':forms.TextInput(
                attrs={'type':'datetime-local'}
            ), 
            'description':forms.Textarea(),
        }
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        if self.instance.status or self.instance.start_task:
            self.fields.pop('start_date_task')
            self.fields.pop('deadline_date')
    
        
        