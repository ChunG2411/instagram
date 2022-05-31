from pyexpat import model
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'picture',
            'full_name',
            'email',
            'phone_number',
            'biography',
            'website',
            'gender'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'picture':
                self.fields[field].widget.attrs.update({'class': 'form-control-file'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})