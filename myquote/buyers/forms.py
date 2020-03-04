from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=45)
    email = forms.EmailField(label='Email', max_length=45, required=True)
    city = forms.CharField(label='City', max_length=45)
    CHOICES = [
        ('Support', 'Support'),
        ('Financial', 'Financial'),
        ('Others', 'Others')
    ]
    subject = forms.ChoiceField(label='Subject', choices=CHOICES, required=True)
    message = forms.CharField(label='Message', max_length=1024)

    def clean(self):
        super(ContactForm, self).clean()

        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        city = self.cleaned_data.get('city')
        message = self.cleaned_data.get('message')

        if len(name) > 45:
            self._errors['name'] = self.error_class([
                'Maximum 45 characters allowed.'
            ])
        if len(email) > 45:
            self._errors['email'] = self.error_class([
                'Maximum 45 characters allowed.'
            ])
        if len(city) > 45:
            self._errors['city'] = self.error_class([
                'Maximum 45 characters allowed.'
            ])
        if len(message) > 1024:
            self._errors['message'] = self.error_class([
                'Maximum 45 characters allowed.'
            ])

        return self.cleaned_data