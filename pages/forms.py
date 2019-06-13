from django import forms

class ContactForm(forms.Form):
    """форма для разела 'КОНТАКТЫ'."""

    name = forms.CharField(
        widget=forms.fields.TextInput(attrs={
        'placeholder': 'Имя:',
        'class': 'form-control',
        })
    )