from django.test import TestCase

import datetime

from ..models import CustomUser

class CustomUserModelTest(TestCase):

    def test_CustomUser_representation(self):
        """Test that Customuser model insert users properly"""
        entry = CustomUser.objects.create(username="test_user",
                                          password="123456")
        self.assertTrue(isinstance(entry, CustomUser))

    def test_CustomUser_full_entry(self):
        """Test that CustomUser model inserts all entries"""

        entry = CustomUser.objects.create(username="test_user_2",
                                          email="something@mail.com",
                                          first_name="jhon",
                                          last_name="doe",
                                          password="123456",
                                          birth_date=datetime.date(1997, 10, 9)
                                         )
        self.assertTrue(isinstance(entry, CustomUser))

    def test_CustomUser_returns_str(self):
        """Test that CustomUser returns username"""

        entry = CustomUser.objects.create(username="test_user_3",
                                          password="123456")
        self.assertEqual(str(entry), entry.username)
