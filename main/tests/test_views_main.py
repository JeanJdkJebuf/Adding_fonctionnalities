from django.test import TestCase
from django.urls import reverse

class MainAppTestCase(TestCase):
    def test_index_page(self):
        """ This test will make sure url 'homepage' returns the template"""
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_right_template(self):
        """ test """
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, "main/main.html")

    def test_index_page_as_right_title(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.context["title"], "Du gras, oui, mais de qualité")


    def test_copyright_page(self):
        """ This test will make sure url 'copyright' returns the template"""
        response = self.client.get(reverse('copyright'))
        self.assertEqual(response.status_code, 200)
