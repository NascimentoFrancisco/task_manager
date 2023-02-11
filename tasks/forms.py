from django import forms
from .models import Task

class CreateUpdadteTask(forms.ModelForm):


    class Meta:
        

        model = Task
        fields = ['title', 'deadline_date', 'description']

        widgets = {
            'title':forms.TextInput(),
            'deadline_date':forms.TextInput(
                attrs={'type':'datetime-local'}
            ), 
            'description':forms.Textarea(),
        }
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        if self.instance.status:
            self.fields['deadline_date'].widget.attrs['disabled'] = True
            self.fields['deadline_date'].widget.attrs['readonly'] = True
        
        