from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title','image', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                    format='%m/%d/%Y',
                    attrs={
                        'class':'form-control',
                        'placeholder':'Select a date',
                        'type':'date'
                    }
                ),
            }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Set fields required for UpdateStoryView and AddStoryView
            if self.instance.pk:
                self.fields['title'].required = True
                self.fields['pub_date'].required = True
                self.fields['content'].required = True
            else:
                # For DeleteStoryView, make fields not required
                self.fields['title'].required = False
                self.fields['pub_date'].required = False
                self.fields['content'].required = False