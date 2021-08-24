from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelstCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='A new title', body='Whats up danger.')
    
    def testTaskTitle(self):
        todo = Todo.objects.get(id=1)
        expected_obj_name = f'{todo.title}'
        self.assertEqual(expected_obj_name, 'A new title')

    def testTaskContent(self):
        todo = Todo.objects.get(id=1)
        expected_obj_content = f'{todo.body}'
        self.assertEqual(expected_obj_content, 'Whats up danger.')

