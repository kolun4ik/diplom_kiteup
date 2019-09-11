from django import forms


class ContactForm(forms.Form):
    """форма для разела 'КОНТАКТЫ'."""

    name = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'id': 'name',
            'placeholder': 'Имя:',
            'class': 'form-control',
            'data-error': 'Введите ваше имя',
        })
    )
    email = forms.CharField(
        widget=forms.fields.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'Email:',
            'class': 'form-control',
            'data-error': 'Введите адресс email',
        })
    )
    subject = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'id': 'subject',
            'placeholder': 'Тема:',
            'class': 'form-control',
            'data-error': 'Введите Тему сообщения',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'message',
            'rows': 8,
            'cols': False,
            'placeholder': 'Сообщение:',
            'data-error': 'Введите ваше сообщение',
        })
    )
