from django import forms
from django.core import validators

#custom validation function
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name must start with Z')

class FormName(forms.Form):
    name = forms.CharField()#validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        email = self.cleaned_data.get('email', None)
        vemail = self.cleaned_data.get('verify_email', None)

        if email != vemail:
            raise forms.ValidationError('Emails do not match')

    # probably will never use this to catch a bot, use django.core validators instead
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher
