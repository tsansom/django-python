from django import forms
from AppTwo.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify email address')

    def clean(self):
        email = self.cleaned_data.get('email', None)
        vemail = self.cleaned_data.get('verify_email', None)

        if email != vemail:
            raise forms.ValidationError('Emails do not match')

    class Meta:
        model = User
        fields = '__all__'
