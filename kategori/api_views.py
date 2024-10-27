from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Kategori
from .forms import KategoriForm
from rest_framework.permissions import IsAuthenticated

class KategoriListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        GET /api/kategori/
        List all categories for the authenticated user.
        """
        kategori_pemasukan = Kategori.objects.filter(user=request.user, jenis_kategori=1)
        kategori_pengeluaran = Kategori.objects.filter(user=request.user, jenis_kategori=2)

        response = {
            "kategori_pemasukan": [{"id": kat.id, "nama": kat.nama} for kat in kategori_pemasukan],
            "kategori_pengeluaran": [{"id": kat.id, "nama": kat.nama} for kat in kategori_pengeluaran],
        }

        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST /api/kategori/
        Create a new category for the authenticated user.
        """
        form = KategoriForm(request.data)
        if form.is_valid():
            try:
                kategori = form.save(commit=False)
                kategori.user = request.user  # Assign the user to the kategori
                kategori.save()
                return Response({"message": "Kategori berhasil dibuat!"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"error": "Kategori ini sudah pernah dibuat!"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
