from django import forms
from .models import case

from .models import register_case

class register_new_case(forms.ModelForm):
    class Meta:
        model=register_case
        fields=['type_of_case','proofs','Descriptions']
class DateInput(forms.DateInput):
    input_type = 'date'
class update_case_form(forms.ModelForm):
    class Meta:
        model=case
        fields=['Date_of_hearing','Active','status','court_name']
        widgets = {
            'Date_of_hearing':DateInput(),
        }
        exclude=('client_id','lawyer','Description','image','case','client_id','lawyer')

