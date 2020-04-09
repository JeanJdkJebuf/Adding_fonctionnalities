from django.test import TestCase

from ..models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        #Products below are created for substitute's test
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
        #Products below are created for substitute's filter test
        fake_double_product = Product.objects.create(id=654785423, \
                                              product_name="pudding", \
                                              img_front_url="img_url.com", \
                                              nutri_grade=100, \
                                              img_nutrition_url="link_nutri.com", \
                                              web_link="link_openfoodfact.com", \
                                             )
        fake_double_product_two = Product.objects.create(id=324785654, \
                                              product_name="pudding", \
                                              img_front_url="img_url.com", \
                                              nutri_grade=99, \
                                              img_nutrition_url="link_nutri.com", \
                                              web_link="link_openfoodfact.com", \
                                             )
        # Many to many link
        fake_category = Category.objects.create(name="cat_name")

        fake_product.categories.add(fake_category)
        fake_result.categories.add(fake_category)

        fake_double_product_two.categories.add(fake_category)
        fake_double_product.categories.add(fake_category)

        # functions for tests
        self.product_tested = Product.objects.get(product_name="cacahuètes au chocolat")
        self.doubled_name = Product.objects.get(id=654785423)

        #Expected answers
        self.answerone = Product.objects.get(id=6598745801)
        self.answertwo = Product.objects.get(id=324785654)

    def create_product(self,
                       product_name="test_product",
                       id_product=123545654,
                       img_front_url="url.com",
                       nutri_grade=97,
                       img_nutrition_url="google.com",
                       web_link="yup.com"):
        return Product.objects.create(product_name=product_name,
                                      id=id_product,
                                      img_front_url=img_front_url,
                                      nutri_grade=nutri_grade,
                                      img_nutrition_url=img_nutrition_url,
                                      web_link=web_link)

    def test_product_representation(self):
        """Test that Product model insert products properly"""

        entry = self.create_product()
        self.assertTrue(isinstance(entry, Product))

    def test_Category_representation(self):
        """Test that Category model insert products properly"""

        entry = Category.objects.create(name="ham")
        self.assertTrue(isinstance(entry, Category))

    def test_substitute_Custom_manager(self):
        """Test that substitute function works properly"""
        substitutes = Product.objects.substitute(self.product_tested)
       # self.assertQuerysetEqual([self.answertwo, self.answerone], substitutes)
