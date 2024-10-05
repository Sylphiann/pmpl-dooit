from django.test import TestCase
from kategori.forms import KategoriForm
from catatanTransaksi.models import JenisTransaksi

class KategoriFormTest(TestCase):
    
    def setUp(self):
        self.jenis_transaksi = JenisTransaksi.objects.create(name="Jenis A") 

    def test_valid_form(self):
        # Test form with valid data
        form_data = {'nama': 'Test Kategori', 'jenis_kategori': self.jenis_transaksi.id}
        form = KategoriForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test form with missing data (invalid test)
        form_data = {'nama': ''}
        form = KategoriForm(data=form_data)
        self.assertFalse(form.is_valid())
