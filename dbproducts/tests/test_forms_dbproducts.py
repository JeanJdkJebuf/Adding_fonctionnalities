from django.test import TestCase
from ..forms import ResearchProduct

class FormsTestCase(TestCase):

    def test_research_form_is_valid(self):
        data = {"product":"produit_1"}

        form = ResearchProduct(data=data)
        self.assertTrue(form.is_valid())
