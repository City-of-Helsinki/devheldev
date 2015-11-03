from django.test import TestCase, Client
import urllib.request

class HomePageTestCase(TestCase):
    client = Client()

    def test_home(self):
        # Wagtail doesn't accept django client without subpage url
        # response = self.client.get('/')
        # Therefore, successful test requires running web server
        response = urllib.request.urlopen('http://localhost:8000')
        self.assertEquals(response.status, 200)
        self.assertIn('Code for Europe', response.read().decode())

