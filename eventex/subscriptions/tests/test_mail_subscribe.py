from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        """Valid post should redirect to /inscricao/"""
        data = dict(name='John Lennon', cpf=12345678901,
                    email='john@lennon.com', phone='12-3456-7890')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'john@lennon.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'John Lennon',
            '12345678901',
            'john@lennon.com',
            '12-3456-7890',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
