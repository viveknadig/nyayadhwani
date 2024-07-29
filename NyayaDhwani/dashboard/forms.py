from django import forms
from .models import case

from .models import register_case

class register_new_case(forms.ModelForm):
    class Meta:
        model=register_case
        fields=['type_of_case','proofs','Descriptions']
