from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

class UsersAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')

    def test_create_user_page(self):
        """This test will make sure url 'create_user' works properly"""
        form = {"username":"test_create_user",
                "password1":"azerJkdfe123",
                "password2":"azerJkdfe123",
                'email':"g@g.com",
                'first_name':"jean",
                'last_name':"claude",
               }
        response = self.client.post(reverse('create_user'),
                                    form
                                   )
        self.assertEqual(response.status_code, 302)

    def test_create_user_error_page(self):
        """This test will make sure url 'create_user' redirects properly"""
        CustomUser.objects.create(username="test_user_fail", password="123456")

        response = self.client.post(reverse('create_user'),
                                    {"username":"test_user_fail",
                                     "password1":"123456",
                                     "password2":"123456",
                                    },
                                   )
        self.assertEqual(response.status_code, 200)

    def test_log_ing_page(self):
        """ This test will make sure url 'log_in' returns the template"""

        result = self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('log_in'))
        self.assertTrue(result)
        self.assertEqual(response.status_code, 200)

    def test_disconnect_page(self):
        """ this test will make sure url 'disconnect_user' returns template"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('disconnect_user'))
        self.assertEqual(response.status_code, 302)

    def test_disconnect_page_follows(self):
        """ this test will make sure url 'disconnect_user' returns template"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('disconnect_user'),
                                  follow=True)
        self.assertTemplateUsed(response,"main/main.html")

    def test_user_informations_page(self):
        """ this test will make sure url 'user_informations' returns template"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_informations'))
        self.assertEqual(response.status_code, 200)

##################################################
# Tests for project 11, adding fonctionnalities
##################################################

    def test_edit_profile(self):
        """ this test will make sure url 'edit_profile' returns template"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)

        def test_edit_profile_changes_data(self):
            """this test will make sure url "edit_profile" actually edits something"""
            self.client.login(username='testuser', password='12345')
            form = {"username":"testuser",
                    "password1":"12345",
                    "password2":"12345",
                    'email':"g@g.com",
                    'first_name':"jean",
                    'last_name':"",
                   }
            response = self.client.post(reverse('edit_profile'),
                                        form,
                                       )
            user = CustomUser.objects.get(username="testuser")
            self.assertEqual(user.email, "g@g.com")

    def test_edit_password_page(self):
        """ this test will make sure url 'change_password' returns template"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

    def test_edit_password_works(self):
        """ this test will make sure url 'change_password' returns template"""
        self.client.login(username='testuser', password='12345')
        form = {"old_password":"12345",
                "new_password1":"azer123456",
                "new_password2":"azer123456",
               }
        response = self.client.post(reverse('change_password'), form)
        test_password = CustomUser.objects.get(username="testuser")
        self.assertEqual(response.status_code, 302)

    def test_edit_password_works_name(self):
        """ this test will make sure url 'change_password' returns template"""
        self.client.login(username='testuser', password='12345')
        form = {"old_password":"12345",
                "new_password1":"azer123456",
                "new_password2":"azer123456",
               }
        response = self.client.post(reverse('change_password'), form)
        test_password = CustomUser.objects.get(username="testuser")
        self.assertTrue(test_password.check_password("azer123456"))
