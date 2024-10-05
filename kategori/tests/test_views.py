from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kategori.models import Kategori
from catatanTransaksi.models import JenisTransaksi
from kategori.forms import KategoriForm

class KategoriViewsTest(TestCase):

    def setUp(self):
        # Create a user and log them in
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            company_name="Test Company",   
            email="testuser@example.com" 
        )
        self.client.login(username='testuser', password='password123')

        # Create sample JenisTransaksi
        self.jenis_pemasukan = JenisTransaksi.objects.create(id=1, nama="Pemasukan")
        self.jenis_pengeluaran = JenisTransaksi.objects.create(id=2, nama="Pengeluaran")

        # Create sample Kategori for the user
        Kategori.objects.create(user=self.user, nama="Kategori Pemasukan", jenis_kategori=self.jenis_pemasukan)
        Kategori.objects.create(user=self.user, nama="Kategori Pengeluaran", jenis_kategori=self.jenis_pengeluaran)

    def test_index_view_status_code(self):
        response = self.client.get(reverse('kategori:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        response = self.client.get(reverse('kategori:index'))
        self.assertEqual(len(response.context['kategoris_pemasukan']), 1)
        self.assertEqual(len(response.context['kategoris_pengeluaran']), 1)
        self.assertEqual(response.context['kategoris_pemasukan'][0].nama, "Kategori Pemasukan")
        self.assertEqual(response.context['kategoris_pengeluaran'][0].nama, "Kategori Pengeluaran")

    def test_buat_kategori_view_get(self):
        response = self.client.get(reverse('kategori:buat_kategori'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], KategoriForm)

    def test_buat_kategori_view_post_valid(self):
        form_data = {
            'nama': 'Kategori Baru',
            'jenis_kategori': self.jenis_pemasukan.id
        }
        response = self.client.post(reverse('kategori:buat_kategori'), data=form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Kategori.objects.filter(nama="Kategori Baru").exists())

    def test_buat_kategori_view_post_invalid(self):
        form_data = {
            'nama': '',
            'jenis_kategori': self.jenis_pemasukan.id
        }
        response = self.client.post(reverse('kategori:buat_kategori'), data=form_data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(Kategori.objects.filter(nama="").exists())  

    def test_buat_kategori_view_duplicate(self):
        form_data = {
            'nama': 'Kategori Pemasukan', 
            'jenis_kategori': self.jenis_pemasukan.id
        }
        response = self.client.post(reverse('kategori:buat_kategori'), data=form_data)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Kategori ini sudah pernah dibuat!')  
