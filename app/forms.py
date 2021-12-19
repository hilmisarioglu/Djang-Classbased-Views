from django import  forms
from django.forms import fields
from .models import Student
from django.core.exceptions import ValidationError 


class StudentForm(forms.ModelForm):
    # Burada ilk yazilan isin clean olacak
    def clean_number(self):
        number = self.cleaned_data['number']
        if not(1<number<1000):
            raise ValidationError('Student should be between 1 and 1000')
        return number
    def clean_phone(self):
        phone = self.cleaned_data['phone']

        
    class Meta:
        model = Student
        fields = "__all__"