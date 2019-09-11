from django.test import TestCase


class myTestCase(TestCase):
    """TestCase extended method"""
    fixtures = ['events.yaml']
