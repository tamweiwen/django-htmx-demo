from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Note


class NotesForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.add_input(Submit('submit', 'Add Note', css_class='btn-primary'))
    # helper.form_method = 'POST'

    class Meta:
        model = Note
        fields = ['name', 'content']

    
