from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import User
from announecements.models import annonce
from module.models import matiere

class HomeViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        self.matiere = matiere.objects.create(nom='Math')
        self.annonce = annonce.objects.create(
            owner=self.user,
            module=self.matiere,
            title='Test Title',
            description='Test Description'
        )
    
    def test_redirect_if_not_authenticated(self):
        response = self.client.get(reverse('simpleuser:home'))
        self.assertRedirects(response, '/simpleuser/signin/?next=/simpleuser/home/')

    def test_home_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('simpleuser:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Math')
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Description')

    def test_post_request(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            reverse('simpleuser:home'),
            {
                'title': 'Test Title 2',
                'description': 'Test Description 2',
                'module': 'Math'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/simpleuser/home/')
        self.assertEqual(annonce.objects.count(), 2)