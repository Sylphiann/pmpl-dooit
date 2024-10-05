from django.test import TestCase
from django.urls import reverse, resolve
from kategori.views import index, buat_kategori
from django.contrib.auth import get_user_model

class KategoriUrlsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            company_name="Test Company",
            email="testuser@example.com"
        )
        self.client.login(username='testuser', password='password123')

    def test_index_url_resolves(self):
        url = reverse('kategori:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_buat_kategori_url_resolves(self):
        url = reverse('kategori:buat_kategori')
        self.assertEqual(resolve(url).func, buat_kategori)

    def test_index_url_status_code(self):
        response = self.client.get(reverse('kategori:index'))
        self.assertEqual(response.status_code, 200)  
