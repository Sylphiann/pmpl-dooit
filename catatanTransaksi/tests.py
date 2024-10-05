from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from catatanTransaksi.views import *
from catatanTransaksi.models import CatatanTransaksi, JenisTransaksi
from kategori.models import Kategori
from datetime import date
from django.utils import timezone
from unittest.mock import MagicMock, patch, Mock
from users.models import CustomUser

User = get_user_model()


class CatatanTransaksiViewTest(TestCase):

    def setUp(self):
        # Membuat user untuk tes
        self.client = Client()
        self.factory = RequestFactory()
        self.company_name = "test_company"
        self.username = "test_username"
        self.email = "test@email.com"
        self.password = "test_password"
        self.role = CustomUser.PENCATAT
        self.user = CustomUser.objects.create_user(
            company_name=self.company_name,
            username=self.username,
            email=self.email,
            password=self.password,
        )
        self.jenis_pemasukan = JenisTransaksi.objects.create(
            jenis=JenisTransaksi.PEMASUKAN
        )
        self.jenis_pengeluaran = JenisTransaksi.objects.create(
            jenis=JenisTransaksi.PENGELUARAN
        )
        self.kategori_gaji = Kategori.objects.create(
            user=self.user, nama="Gaji", jenis_kategori=self.jenis_pemasukan
        )
        self.kategori_bensin = Kategori.objects.create(
            user=self.user, nama="Bensin", jenis_kategori=self.jenis_pengeluaran
        )

        self.catatan_transaksi_pemasukan = CatatanTransaksi.objects.create(
            pencatat=self.user,
            deskripsi="Gaji Masuk",
            nominal=5000000,
            tanggal=timezone.now().date(),
            kategori=self.kategori_gaji,
            jenis=self.jenis_pemasukan,
        )
        self.catatan_transaksi_pengeluaran = CatatanTransaksi.objects.create(
            pencatat=self.user,
            deskripsi="Bensin",
            nominal=300000,
            tanggal=timezone.now().date(),
            kategori=self.kategori_bensin,
            jenis=self.jenis_pengeluaran,
        )

        self.client.login(username="testuser", password="12345")

        return super().setUp()

    @patch("catatanTransaksi.views.CatatanTransaksi.objects.filter")
    @patch("catatanTransaksi.views.get_saldo_by_jenis")
    def test_index_valid(self, mock_filter, mock_saldo):
        mock_saldo.side_effect = [5000000, 300000]
        mock_filter.return_value.order_by.return_value = []
        response = self.client.get(reverse("catatan-transaksi:index"))
        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.views.CatatanTransaksi.objects.filter")
    def test_index_invalid(self, mock_filter):
        mock_filter.side_effect = Exception("Database error")
        response = self.client.get(reverse("catatan-transaksi:index"))
        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.views.CatatanTransaksi.objects.get")
    def test_detail_view(self, mock_get_catatan_transaksi):
        mock_get_catatan_transaksi.return_value = self.catatan_transaksi_pemasukan
        response = self.client.get(
            reverse(
                "catatan-transaksi:detail", args=[self.catatan_transaksi_pemasukan.id]
            )
        )
        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.views.CatatanTransaksi.objects.get")
    def test_detail_invalid(self, mock_get):
        mock_get.side_effect = CatatanTransaksi.DoesNotExist
        response = self.client.get(
            reverse(
                "catatan-transaksi:detail", args=[self.catatan_transaksi_pemasukan.id]
            )
        )
        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.forms.CatatanTransaksiForm.is_valid")
    def test_buat_view_post(self, mock_is_valid):
        mock_is_valid.return_value = True
        response = self.client.post(
            reverse("catatan-transaksi:buat"),
            {
                "deskripsi": "Gaji lagi",
                "nominal": 2000000,
                "tanggal": timezone.now().date(),
                "kategori": self.kategori_gaji,
                "jenis": self.jenis_pemasukan,
            },
        )

        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.forms.CatatanTransaksiForm.is_valid")
    def test_buat_invalid(self, mock_is_valid):
        mock_is_valid.return_value = False
        response = self.client.post(
            reverse("catatan-transaksi:buat"),
            {
                "deskripsi": "",
                "nominal": -100.0,
            },
        )
        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.views.CatatanTransaksi.objects.filter")
    def test_view_laporan_keuangan(self, mock_filter):
        mock_filter.return_value = MagicMock()

        response = self.client.get(reverse("catatan-transaksi:view"))

        self.assertEqual(response.status_code, 302)

    @patch("catatanTransaksi.views.get_total_by_waktu")
    def test_get_vis_pemasukan_pengeluaran_by_waktu(self, mock_get_total_by_waktu):
        mock_get_total_by_waktu.return_value = 100

        response = self.client.get(
            reverse("catatan-transaksi:get_vis_pemasukan_pengeluaran_by_waktu")
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                "expense_time_data": {
                    "January": 100,
                    "February": 100,
                    "March": 100,
                    "April": 100,
                    "May": 100,
                    "June": 100,
                    "July": 100,
                    "August": 100,
                    "September": 100,
                    "October": 100,
                    "November": 100,
                    "December": 100,
                },
                "income_time_data": {
                    "January": 100,
                    "February": 100,
                    "March": 100,
                    "April": 100,
                    "May": 100,
                    "June": 100,
                    "July": 100,
                    "August": 100,
                    "September": 100,
                    "October": 100,
                    "November": 100,
                    "December": 100,
                },
            },
        )

    @patch("catatanTransaksi.views.get_category")
    @patch("catatanTransaksi.views.CatatanTransaksi.objects.filter")
    def test_vis_pengeluaran_by_kategori(self, mock_category, mock_filter):
        mock_category.return_value = ["TestCategory"]
        mock_filter.return_value = MagicMock()
        response = self.client.get(
            reverse("catatan-transaksi:get_vis_pengeluaran_by_kategori")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("expense_category_data", response.json())
