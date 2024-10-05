from django.test import TestCase
from kategori.models import Kategori
from users.models import CustomUser
from catatanTransaksi.models import JenisTransaksi
from django.utils import timezone

class KategoriModelTest(TestCase):
    
    def setUp(self):
        # Create a user and a related JenisTransaksi object
        self.user = CustomUser.objects.create(username="testuser", password="password123")
        self.jenis_transaksi = JenisTransaksi.objects.create(jenis=JenisTransaksi.PEMASUKAN) 

        # Create a Kategori object for testing only
        self.kategori = Kategori.objects.create(
            user=self.user, 
            nama="Test Kategori",
            jenis_kategori=self.jenis_transaksi
        )

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
