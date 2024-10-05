from functools import wraps
from unittest import mock
from django.test import TestCase
from .views import *

mock_delete_expired = mock.MagicMock()
mock_filter = mock.MagicMock()

# Create your tests here.
class AnggaranViewTest(TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('anggaran.views.delete_expired_anggaran', mock_delete_expired)
    @mock.patch('anggaran.models.Anggaran.objects.filter', mock_filter)
    def test_index_success(self):
        mock_delete_expired.side_effect = [None]
        mock_filter.return_value = []

        response = self.client.get(reverse("anggaran:index"))
        self.assertEqual(response.status_code, 302)