from django.test import TestCase, Client
from django.urls import reverse
from dbproducts.models import Product, Category

class DbProductsAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        #Products below are created for regular test for research substitute
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
        #Products below are created for MultipleObjectsReturned test
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

        # Creating vars for tests
        self.product_tested = Product.objects.get(id=598745601)
        self.fake_result = Product.objects.get(id=6598745801)

        # Creating fake_product_double for tests
        self.double_product = Product.objects.get(id=654785423)

        # Client for tests
        self.client = Client()

    def test_detail_page(self):
        """ This test will make sure url 'detail' returns the template"""

        product_id = self.product_tested.id
        response = self.client.get(reverse('detail', args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    def test_redirect_detail_page(self):
        """ This test will make sure url 'detail' redirects properly """

        product_id = self.product_tested.id
        response = self.client.get(reverse('detail', args=(product_id+1,)))
        self.assertEqual(response.status_code, 302)

    def test_research_substitute_page(self):
        """ This test will make sure url 'research_substitute' returns the \
template"""

        response = self.client.get(reverse('research_substitute'), \
                                           {"txtSearch":self.product_tested.product_name})
        self.assertEqual(response.status_code, 200)

    def test_ObjectDoesNotExist_research_substitute_page(self):
        """ This test will make sure url 'research_substitute' redirects to \
homepage if product doens't exists"""
        response = self.client.get(reverse('research_substitute'), \
                                           {"txtSearch":self.product_tested.product_name+"test"})
        self.assertEqual(response.status_code, 302)

    def test_MultipleObjectsReturned_research_substitute_page(self):
        """ This test will make sure url 'research_substitute'returns only one \
product if more than one contains that name"""
        response = self.client.get(reverse('research_substitute'), \
                                           {"txtSearch":self.double_product.product_name})
        self.assertEqual(response.status_code, 200)

    def test_autocomplete_research_registering_word(self):
        """ This test will make sure view 'autocomplete' registers words properly"""
        response = self.client.get(reverse('autocomplete'), \
                                           {"term":self.product_tested.product_name})
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            ['cacahuètes au chocolat']
        )
    def test_autocomplete_research_working(self):
        """ This test will make sure view 'autocomplete' renders Json answer"""
        response = self.client.get(reverse('autocomplete'), \
                                           {"term":self.product_tested.product_name})
        self.assertEqual(response.status_code, 200)
