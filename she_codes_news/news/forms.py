from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title','image', 'content']

    # Add calendar input to set publish date
        # widgets = {
        #     'pub_date': forms.DateInput(
        #             format='%m/%d/%Y',
        #             attrs={
        #                 'class':'form-control',
        #                 'placeholder':'Select a date',
        #                 'type':'date'
        #             }
        #         ),
        #     }
        
        # Set required fields when updating and adding story
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance.pk:
                self.fields['title'].required = True
                self.fields['content'].required = True
            else:
                # For DeleteStoryView, make fields not required
                self.fields['title'].required = False
                self.fields['content'].required = False