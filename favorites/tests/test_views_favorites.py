from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser
from dbproducts.models import Product, Category
from favorites.models import Favorites

class FavoritesAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""

        # Creating user 1
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.login = self.client.login(username='testuser', password='12345')

        #Creating products to add into favorites
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
        #Adding categories to products
        fake_category = Category.objects.create(name="cat_name")
        fake_product.categories.add(fake_category)
        fake_result.categories.add(fake_category)

        Favorites.objects.create(substitute=fake_result,
                                 original_prod=fake_product,
                                 user=self.user
                                )

    def test_add_favorites_page(self):
        """ This test will make sure url 'add_favorites' returns homepage"""

        response = self.client.post(reverse('add_favorites'),
                                    {"prev_prod":6598745801,
                                     "new_sub":598745601,
                                    }
                                   )
        self.assertEqual(response.status_code, 200)

    def test_duplicate_add_favorites_page(self):
        """ This test will make sure url 'add_favorites' returns homepage with \
error message if product is already added to favorites"""

        # Trying to add some favorites we already added in the SetUp
        response = self.client.post(reverse('add_favorites'),
                                    {"prev_prod":598745601,
                                     "new_sub":6598745801,
                                    }
                                   )
        self.assertEqual(response.status_code, 200)

    def test_missing_data_add_favorites_page(self):
        """ This test will make sure url 'add_favorites' returns homepage with \
error message if some data is missing"""

        response = self.client.post(reverse('add_favorites'))
        self.assertEqual(response.status_code, 200)

    def test_consult_favorites_page(self):
        """ This test will make sure url 'consult_favorites' renders template"""

        response = self.client.post(reverse('consult_favorites'))
        self.assertEqual(response.status_code, 200)
