from django.test import TestCase
from ..models import CustomUser

#Importing forms classes
from ..forms import CustomUserCreationForm, ConnexionForm, CustomUserChangeForm

class FormsUsersTestCase(TestCase):
    """Class testing users/forms.py"""

    def setUp(self):
        """Creating data used with those tests"""
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')


    def test_CustomUserCreationForm_form_is_valid(self):
        """tests for CustomUserCreationForm (is_valid) """

        form_data = {"username":"test_user_create_acc",
                     "password":"123456",
                     "email":"gosh@test.com",
                    }

        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid)

    def test_ConnexionForm_form_is_valid(self):
        """test for ConnexionForm (is_valid)"""

        form_data = {"username":"testuser",
                     "password":"12345",
                    }

        form = ConnexionForm(data=form_data)
        self.assertTrue(form.is_valid)

    def test_CustomUserChangeForm_is_valid(self):
        """test for CustomUserChangeForm"""

        form_data = {"username":"testuser",
                     "password":"12345",
                    }

        ConnexionForm(data=form_data)
        form = CustomUserChangeForm(data={"username":"testuser2"})
        self.assertTrue(form.is_valid)

    def test_CustomUserChangePassword_is_valid(self):
        """test for CustomUserChangePassword"""

        form_data = {"username":"testuser",
                     "password":"12345",
                    }

        ConnexionForm(data=form_data)
        form = CustomUserChangeForm(data={"password":"123456"})
        self.assertTrue(form.is_valid)
