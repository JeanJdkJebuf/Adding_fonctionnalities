from django.db import models

from dbproducts.models import Product
from django.conf import settings

class Favorites(models.Model):
    """Class linking primary key of users (users.models and the
    product id from dbproducts.models class"""

    substitute = models.ForeignKey("dbproducts.Product",
                                   related_name='favorite_as_substitute',
                                   on_delete=models.CASCADE,
                                  )
    original_prod = models.ForeignKey("dbproducts.Product",
                                      related_name='favorite_as_original',
                                      on_delete=models.CASCADE,
                                     )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE
                            )
