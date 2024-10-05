from django.test import Client, RequestFactory, TestCase
from unittest.mock import patch, MagicMock
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Konsultan
from konsultasi.models import Konsultasi
from django.contrib.auth import get_user_model
from users.models import CustomUser, CustomUserProfile

User = get_user_model()


class KonsultanViewTest(TestCase):

    def setUp(self):
        # Membuat user untuk tes
        self.client = Client()
        self.factory = RequestFactory()
        self.company_name = "test_company"
        self.username = "test_username"
        self.email = "test@email.com"
        self.password = "test_password"
        self.role = CustomUser.KONSULTAN
        self.user = CustomUser.objects.create_user(
            company_name=self.company_name,
            username=self.username,
            email=self.email,
            password=self.password,
        )
        if not CustomUserProfile.objects.filter(user=self.user).exists():
            self.user_profile = CustomUserProfile.objects.create(user=self.user)
        else:
            self.user_profile = CustomUserProfile.objects.get(user=self.user)

        self.konsultan = Konsultan.objects.create(
            user=self.user,
            user_profile=self.user_profile,
            first_name="John",
            last_name="Doe",
            is_approved=True,
        )
        # Create some mock Konsultasi objects
        self.konsultasi_pending = Konsultasi.objects.create(
            klien=self.user,
            konsultan=self.konsultan,
            status="Menunggu Persetujuan",
            alasan="Need consultation about a project",
            tanggal="2024-10-10",
        )

        self.konsultasi_accepted = Konsultasi.objects.create(
            klien=self.user,
            konsultan=self.konsultan,
            status="Sedang Berlangsung",
            alasan="Accepted consultation",
            tanggal="2024-10-11",
            is_accepted=True,
        )
        self.client.login(username="testuser", password="12345")
        return super().setUp()

    @patch("konsultan.views.Konsultan.objects.get")
    @patch("konsultan.views.Konsultasi.objects.filter")
    def test_dashboard_konsultan(self, mock_filter, mock_get):
        mock_get.return_value = self.konsultan
        mock_filter.return_value = MagicMock()

        response = self.client.get(reverse("konsultan:dashboard_konsultan"))

        self.assertEqual(response.status_code, 302)
