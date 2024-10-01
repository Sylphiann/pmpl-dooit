from django.test import TestCase
from django.urls import reverse, resolve
from kategori.views import index, buat_kategori

class KategoriUrlsTest(TestCase):
    
    def test_index_url_resolves(self):
        # Test the 'index' URL 
        url = reverse('kategori:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_buat_kategori_url_resolves(self):
        # Test the 'buat_kategori' URL
        url = reverse('kategori:buat_kategori')
        self.assertEqual(resolve(url).func, buat_kategori)

    def test_index_url_status_code(self):
        response = self.client.get(reverse('kategori:index'))
        self.assertEqual(response.status_code, 200)

    def test_buat_kategori_url_status_code(self):
        response = self.client.get(reverse('kategori:buat_kategori'))
        self.assertEqual(response.status_code, 200)
