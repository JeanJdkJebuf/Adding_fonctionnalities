from django.test import TestCase

from ..models import Favorites

# Importing models for tests
from dbproducts.models import Product
from users.models import CustomUser

class FavoritesModelTest(TestCase):

    def test_Favorites_representation(self):
        """Test that Favorites model saves correctly informations"""

        # Creating datas for tests
        fake_product = Product.objects.create(id=598745601, \
                                              product_name="cacahuètes au chocolat", \
                                              img_front_url="img_url.com", \
                                              nutri_grade=100, \
                                              img_nutrition_url="link_nutri.com", \
                                              web_link="link_openfoodfact.com", \
                                             )
        fake_result = Product.objects.create(id=6598745801, \
                                              product_name="amandes au chocolat", \
                                              img_front_url="img_url.com", \
                                              nutri_grade=98, \
                                              img_nutrition_url="link_nutri.com", \
                                              web_link="link_openfoodfact.com", \
                                             )
        entry = CustomUser.objects.create(username="test_user",
                                          password="123456")

        favorite_entry = Favorites.objects.create(substitute=fake_product,
                                                  original_prod=fake_result,
                                                  user=entry)
        self.assertTrue(isinstance(favorite_entry, Favorites))
