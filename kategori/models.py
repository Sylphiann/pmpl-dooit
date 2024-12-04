from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from users.models import CustomUser
from catatanTransaksi.models import *

class Kategori(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=30)
    jenis_kategori = models.ForeignKey(JenisTransaksi, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['user', 'nama']

    def __str__(self):
        return self.nama

    def get_nama(self):
        return self.nama

    def get_list_catatan_transaksi(self, user):
        return Kategori.objects.get(nama=self.nama, user=user).catatantransaksi_set.all()

    def get_kategori_nominal(self, start_date, end_date, user):
        catatan_transaksi = self.get_list_catatan_transaksi(user)
        nominal = 0

        for catatan in catatan_transaksi:
            if catatan.tanggal >= start_date and catatan.tanggal <= end_date:
                nominal = nominal + catatan.nominal
        return nominal