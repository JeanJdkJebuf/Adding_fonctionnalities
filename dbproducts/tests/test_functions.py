from django.test import TestCase

from ..related_functions import symbol_removal

class functionsTestCase(TestCase):

    def test_symbol_removal_working(self):
        """Test that symbol removal works"""
        entry = "en:jéâî"
        answer = symbol_removal(entry)
        self.assertEqual("jeai", answer)

    def test_symbol_removal_advanced_working(self):
        """Test that symbol removal works, advanced tests"""
        entry = "en:jéâî $ç-v*"
        answer = symbol_removal(entry)
        self.assertEqual("jeai_$c_v*", answer)
