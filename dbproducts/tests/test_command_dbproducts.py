# Tests meant for commands

from unittest.mock import patch
from django.test import TestCase
from django.core.management import call_command
from dbproducts.models import Product

class CommandTestCase(TestCase):
    @patch("requests.get")
    def test_populate_db_works_correctly(self, mock_get):
        mock_get.return_value.json.return_value = {
            "products":[{
                "_id":123456,
                "product_name_fr":"jambon",
                "image_front_url":"img.com",
                "nutrition_grades":"a",
                "image_nutrition_url":"www.google.com",
                "url":"anotherlink.com",
                "categories_hierarchy":["viande"]
            },
            ]
        }
        call_command("populate_db")
        product = Product.objects.all()
        self.assertEqual(len(product), 1)

        self.assertEqual(product[0].product_name, "jambon")
