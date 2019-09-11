from django.test import TestCase
from pages.forms import ContactForm
from unittest import skip


class ContactFormTest(TestCase):
    """тест формы в разделе 'КОНТАКТЫ'."""

    def test_form_input_items_have_placeholder_and_css_classes(self):
        """тест: поля ввода формы имеют атриббуты placeholder и css классы"""
        form = ContactForm()
        # form.as_p() - выводит форму в виде HTML разметки

        self.assertIn('placeholder="Имя:"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())

        self.assertIn('placeholder="Email:"', form.as_p())

        self.assertIn('placeholder="Тема:', form.as_p())

        self.assertIn('placeholder="Сообщение', form.as_p())
