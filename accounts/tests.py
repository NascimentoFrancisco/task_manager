from django.test import Client, TestCase
from django.urls import reverse


from .models import User
# Create your tests here.


class TasksViewsTestCase(TestCase):


    def setUp(self) -> None:

        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            name='Testando', 
            email='testuser@gmail.com', 
            password='senha123#'
        )

        return super().setUp()


    def test_create_user(self) -> None:

        url = reverse('accounts:create_user')
        response = self.client.post(url, {
            'username':'tests',
            'name':'Testando',
            'email':'teste@gmail.com',
            'password1':'testado#3',
            'password2':'testado#3'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)
        user = User.objects.get(username='tests')
        self.assertEqual(user.username, 'tests')
        self.assertEqual(user.name, 'Testando')
        self.assertEqual(user.email, 'teste@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_update_user(self) -> None:
    
        url = reverse('accounts:update_user')
        self.client.login(username='testuser',password='senha123#')
        response = self.client.post(url, {
            'username': 'testesupdate',
            'name':'Testando teste',
            'email': 'testeupdated@gmail.com',
        })

        self.assertEqual(response.status_code, 302)
        updated_user = User.objects.get(pk=self.user.pk)
        self.assertEqual(updated_user.username, 'testesupdate')
        self.assertEqual(updated_user.name, 'Testando teste')
        self.assertEqual(updated_user.email, 'testeupdated@gmail.com')
    

    def test_delete_user(self) -> None:

        url = reverse('accounts:delete_user')
        self.client.login(username='testuser',password='senha123#')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 0)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
