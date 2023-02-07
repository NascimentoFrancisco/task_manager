from django.test import Client, TestCase
from django.urls import reverse
from accounts.models import User

from .models import Task
# Create your tests here.


class TasksViewsTestCase(TestCase):
    
    
    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            name='Testando', 
            email='testuser@gmail.com', 
            password='senha123#'
        )

        self.task = Task.objects.create(
            user = self.user,
            title='Tarefa 1',
            description='Descrição teste'
        )

        return super().setUp()


    def test_create_task(self):

        url = reverse('tasks:create_tasks')
        self.client.login(username='testuser',password='senha123#')
        response = self.client.post(url, {
            'title':'Tarefa 2',
            'description':'Descrição teste tarefa 2'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)


    def test_update_task(self):

        url = reverse('tasks:update_tasks', kwargs={'pk':self.task.pk})
        self.client.login(username='testuser',password='senha123#')
        response = self.client.post(url,{
            'title':'Tarefa 1 alterada',
            'description':'Descrição teste 1 alterado'
        })

        self.assertEqual(response.status_code, 302)
        task_update = Task.objects.get(pk=self.task.pk)
        self.assertEqual(task_update.title,'Tarefa 1 alterada')
        self.assertEqual(task_update.description,'Descrição teste 1 alterado')
    

    def test_delete_task(self):

        url = reverse('tasks:delete_tasks', kwargs={'pk':self.task.pk})
        self.client.login(username='testuser',password='senha123#')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
