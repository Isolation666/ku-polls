import django.test
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthTest(django.test.TestCase):
    def setUp(self):
        super().setUp()
        self.username = "testuser"
        self.password = "Fat-Chance!"
        self.user1 = User.objects.create_user(username=self.username,
                                              password=self.password,
                                              email="testuser@nowhere.com")
        self.user1.first_name = "Tester"
        self.user1.save()
