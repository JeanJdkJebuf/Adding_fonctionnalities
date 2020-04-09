from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import FieldDoesNotExist, FieldError

from django.conf import settings
import requests
from dbproducts.models import Category, Product

from dbproducts.related_functions import symbol_removal

class Command(BaseCommand):
    """ This command will populate server. Only use once"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # informations that will be inserted into database
        self.informations_gathered = []
        # id gathered from website, usefull for unicity
        self.id_prod_website = []

    def handle(self, *args, **options):
        """ This function will populate the database"""
        # We first need to gather informations from
        # OpenFoodFacts.

        def gather_informations():
            """This function will gather informations using environment
            variables from django.conf.settings on OpenFoodFacts website and
            store them in self.informations_gathered list"""

            print("gathering informations from Open Food Facts.")

            for num, val in enumerate(settings.PROD_CATEGORIES):
                print("pass : {} / {}".format(num+1, len(settings.PROD_CATEGORIES)))
                # Adding a category to the dictionnary
                settings.SITE_PARAMETERS[settings.TAG_CAT] = val
                req = requests.get(settings.OPEN_FOOD_SITE,
                                   settings.SITE_PARAMETERS).json()
                # Removing useless valors
                req = req["products"]

                for prods in req:
                    if prods["_id"] not in self.id_prod_website \
                        and "product_name_fr" in prods and \
                        prods["product_name_fr"] not in \
                        self.informations_gathered:

                        try:
                            self.informations_gathered.append((prods["_id"],
                                                               prods["product_name_fr"],
                                                               prods["image_front_url"],
                                                               ord(prods["nutrition_grades"]),
                                                               prods["image_nutrition_url"],
                                                               prods["url"],
                                                               prods["categories_hierarchy"],
                                                              ))

                            self.id_prod_website.append(prods["_id"])
                        except KeyError:
                            pass
            print("{} products gathered from OpenFoodFacts website"\
                  .format(len(self.informations_gathered)))

        def populating_db():
            """This function will populate database with informations gathered
            from gather_informations() function"""

            # Message for admin
            print("Populating database with OpenFoodFacts informations")

            # Marker of sub categories.
            # Will be used to not add them if already inserted in database
            sub_cat = []

            #marker for insertion
            marker = 1
            show_five_hundred = 500

            # Inserting product into Products table
            for info_product in self.informations_gathered:
                try:
                    add_prod = Product.objects.create(id=info_product[0],
                                                      product_name=info_product[1],
                                                      img_front_url=info_product[2],
                                                      nutri_grade=info_product[3],
                                                      img_nutrition_url=info_product[4],
                                                      web_link=info_product[5],
                                                     )

                    marker += 1
                    if marker == show_five_hundred:
                        print("{} insertions into database so far".format(show_five_hundred))
                        show_five_hundred += 500

                    for num_sub_categories in info_product[6]:
                        # Creating a var without symbols, converted for
                        # SQL policy
                        sub_category = symbol_removal(num_sub_categories)

                        if sub_category in sub_cat:
                            add_sub_cat = Category.objects.get(name=sub_category)
                        else:
                            sub_cat.append(sub_category)
                            add_sub_cat = Category.objects.create(name=sub_category)
                        #Adding many to many relation between product and category
                        add_prod.categories.add(add_sub_cat)

                except FieldDoesNotExist:
                    print("The column you are trying to fullfill doesn't exist")

                except FieldError:
                    print("The information you are trying to enter \
                         into the database has incorrect values")
        # Running all functions wrote in "handle" Command function
        gather_informations()
        populating_db()
