from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from django.contrib.auth import get_user_model

from kategori.models import Kategori
from kategori.forms import KategoriForm
from kategori.views import index, buat_kategori
from catatanTransaksi.models import JenisTransaksi

# Form Tests
class KategoriFormTest(TestCase):

    def setUp(self):
        self.jenis_transaksi = JenisTransaksi.objects.create(jenis=JenisTransaksi.PEMASUKAN)

    def test_valid_form(self):
        form_data = {'nama': 'Test Kategori', 'jenis_kategori': self.jenis_transaksi.id}
        form = KategoriForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'nama': ''}
        form = KategoriForm(data=form_data)
        self.assertFalse(form.is_valid())


# Model Tests
class KategoriModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            company_name="Test Company",  # Required field
            email="testuser@example.com"  # Required field
        )
        self.jenis_transaksi = JenisTransaksi.objects.create(jenis=JenisTransaksi.PEMASUKAN)
        self.kategori = Kategori.objects.create(user=self.user, nama="Test Kategori", jenis_kategori=self.jenis_transaksi)

    def test_kategori_creation(self):
        self.assertEqual(str(self.kategori), "Test Kategori")
        self.assertEqual(self.kategori.nama, "Test Kategori")

    def test_get_nama_method(self):
        self.assertEqual(self.kategori.get_nama(), "Test Kategori")

    def test_get_list_catatan_transaksi(self):
        transaksi_list = self.kategori.get_list_catatan_transaksi(self.user)
        self.assertEqual(transaksi_list.count(), 0)

    def test_get_kategori_nominal(self):
        start_date = timezone.now() - timezone.timedelta(days=30)
        end_date = timezone.now()
        total_nominal = self.kategori.get_kategori_nomimal(start_date, end_date, self.user)
        self.assertEqual(total_nominal, 0)


# URL Tests
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
        
# View Tests
class KategoriViewsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            company_name="Test Company",  
            email="testuser@example.com"
        )
        self.jenis_pemasukan = JenisTransaksi.objects.create(jenis=JenisTransaksi.PEMASUKAN)
        self.kategori = Kategori.objects.create(user=self.user, nama="Test Kategori", jenis_kategori=self.jenis_pemasukan)

    def test_create_kategori(self):
        kategori_count = Kategori.objects.count()
        new_kategori = Kategori.objects.create(user=self.user, nama="New Kategori", jenis_kategori=self.jenis_pemasukan)
        self.assertEqual(Kategori.objects.count(), kategori_count + 1)
        self.assertEqual(new_kategori.nama, "New Kategori")

    def test_read_kategori(self):
        kategori = Kategori.objects.get(nama="Test Kategori")
        self.assertEqual(kategori.nama, "Test Kategori")

    def test_update_kategori(self):
        kategori = Kategori.objects.get(nama="Test Kategori")
        kategori.nama = "Updated Kategori"
        kategori.save()
        self.assertEqual(kategori.nama, "Updated Kategori")

    def test_delete_kategori(self):
        kategori_count = Kategori.objects.count()
        kategori = Kategori.objects.get(nama="Test Kategori")
        kategori.delete()
        self.assertEqual(Kategori.objects.count(), kategori_count - 1)
        
