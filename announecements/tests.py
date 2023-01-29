from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.contrib.auth.models import User
from announecements.models import annonce
from module.models import matiere

class SAnnounceViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password'
        )
        self.annonce = annonce.objects.create(
            owner=self.user,
            title='Test Title',
            description='Test Description'
        )
    
    def test_s_annonce_view(self):
        response = self.client.get(reverse('simpleuser:s_annonce', kwargs={'annonce_id': self.annonce.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single-announcement.html')
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Description')


class AnnonceModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password', is_teacher=True
        )
        self.matiere = matiere.objects.create(
            nom='Test Matiere'
        )
    
    def test_annonce_model(self):
        annonce = annonce.objects.create(
            owner=self.user,
            title='Test Title',
            module=self.matiere,
            duration=2,
            description='Test Description'
        )
        self.assertEqual(annonce.title, 'Test Title')
        self.assertEqual(annonce.module, self.matiere)
        self.assertEqual(annonce.duration, 2)
        self.assertEqual(annonce.description, 'Test Description')