from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta

from kategori.models import Kategori
from kategori.forms import KategoriForm
from kategori.views import index, buat_kategori
from catatanTransaksi.models import JenisTransaksi, CatatanTransaksi

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
            company_name="Test Company",  
            email="testuser@example.com" 
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
        total_nominal = self.kategori.get_kategori_nominal(start_date, end_date, self.user)
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
        

class KategoriModelDrivenTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            email="testuser@example.com"
        )

        # Create another invalid user
        self.invalid_user = get_user_model().objects.create_user(
            username="invaliduser",
            password="password123",
            email="invaliduser@example.com"
        )

        # Create transaction types
        self.jenis_pemasukan = JenisTransaksi.objects.create(jenis="Pemasukan")
        self.jenis_pengeluaran = JenisTransaksi.objects.create(jenis="Pengeluaran")

        # Create a category for the user
        self.kategori = Kategori.objects.create(
            user=self.user,
            nama="Test Kategori",
            jenis_kategori=self.jenis_pemasukan
        )
        
        # Create another category with no transactions
        self.empty_kategori = Kategori.objects.create(
            user=self.user,
            nama="Kategori Tanpa Transaksi",
            jenis_kategori=self.jenis_pemasukan
        )

        # Create transactions for the category
        self.transaction1 = CatatanTransaksi.objects.create(
            kategori=self.kategori,
            nominal=1000,
            tanggal=now() - timedelta(days=10)
        )
        self.transaction2 = CatatanTransaksi.objects.create(
            kategori=self.kategori,
            nominal=2000,
            tanggal=now() - timedelta(days=5)
        )

    # get_kategori_nominal (ISP)
    
    def get_test_dates(self):
        start_date = now() - timedelta(days=30)
        end_date = now()
        return start_date, end_date
    
    # A1B1C1
    def test_get_kategori_nominal_valid_user_valid_date_range(self):
        start_date, end_date = self.get_test_dates()
        total_nominal = self.kategori.get_kategori_nominal(start_date, end_date, self.user)
        self.assertEqual(total_nominal, 3000)  
        
    # A1B2C1
    def test_get_kategori_nominal_start_date_equals_end_date(self):
        start_date = end_date = now() - timedelta(days=10)
        total_nominal = self.kategori.get_kategori_nominal(start_date, end_date, self.user)
        self.assertEqual(total_nominal, 1000)  
    
    # A1B3C1  
    def test_get_kategori_nominal_end_date_before_start_date(self):
        start_date = now() - timedelta(days=5)
        end_date = now() - timedelta(days=10) 
        with self.assertRaises(ValueError):  
            self.kategori.get_kategori_nominal(start_date, end_date, self.user)
    
    # A3B1C1        
    def test_get_kategori_nominal_future_start_date(self):
        start_date = now() + timedelta(days=10)  
        end_date = now() + timedelta(days=20)
        total_nominal = self.kategori.get_kategori_nominal(start_date, end_date, self.user)
        self.assertEqual(total_nominal, 0)  
    
    # A1B1C2
    def test_get_kategori_nominal_no_transactions(self):
        user_with_no_transactions = get_user_model().objects.create_user(
            username="emptyuser",
            password="password123",
            email="emptyuser@example.com"
        )
        start_date, end_date = self.get_test_dates()
        total_nominal = self.kategori.get_kategori_nominal(start_date, end_date, user_with_no_transactions)
        self.assertEqual(total_nominal, 0)  
    
    # A1B1C3
    def test_get_kategori_nominal_invalid_user(self):
        start_date, end_date = self.get_test_dates()
        with self.assertRaises(Kategori.DoesNotExist):  
            self.kategori.get_kategori_nominal(start_date, end_date, self.invalid_user)
            
    
    # get_list_catatan_transaksi (ISP)
    
    # A1B1
    def test_get_list_catatan_transaksi_valid_user_valid_category(self):
        transactions = self.kategori.get_list_catatan_transaksi(self.user)
        self.assertEqual(transactions.count(), 2)
        self.assertIn(self.transaction1, transactions)
        self.assertIn(self.transaction2, transactions)
    
    # A1B2
    def test_get_list_catatan_transaksi_no_transactions(self):
        transactions = self.empty_kategori.get_list_catatan_transaksi(self.user)
        self.assertEqual(transactions.count(), 0)  
        
    # A1B3
    def test_get_list_catatan_transaksi_invalid_category(self):
        with self.assertRaises(Kategori.DoesNotExist):
            Kategori.objects.get(nama="Invalid Kategori", user=self.user).get_list_catatan_transaksi(self.user)
            
    # A2B1
    def test_get_list_catatan_transaksi_user_no_categories(self):
        with self.assertRaises(Kategori.DoesNotExist):
            Kategori.objects.get(nama="Test Kategori", user=self.user_no_categories).get_list_catatan_transaksi(self.user_no_categories)
    
    # A3B1 
    def test_get_list_catatan_transaksi_unauthenticated_user(self):
        with self.assertRaises(TypeError): 
            self.kategori.get_list_catatan_transaksi(self.invalid_user)












        
