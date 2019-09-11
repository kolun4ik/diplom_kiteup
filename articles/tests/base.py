from django.test import TestCase


class myTestCase(TestCase):
    """TestCase extended method"""
    fixtures = ['articles.yaml', 'users.yaml']
