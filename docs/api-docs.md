# Dooit API Documentation

Dokumentasi ini memberikan gambaran umum mengenai berbagai endpoint API yang ada dalam proyek Dooit. Setiap endpoint dilengkapi dengan deskripsi singkat dan contoh respons dalam format JSON sehingga memudahkan untuk memahami cara penggunaan dan hasil yang akan diperoleh dari setiap permintaan API.

## Table of Contents

1. [Kategori API](#1-kategori-api)
2. [Anggaran API](#2-anggaran-api)
3. [Konsultan API](#3-konsultan-api)
4. [Konsultasi API](#4-konsultasi-api)
5. [Catatan Transaksi API](#5-catatan-transaksi-api)

---

## 1. Kategori API

### `GET /api/kategori/`

- **Deskripsi**: API untuk mengambil daftar semua kategori milik pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Respon**:
  - **200 OK**
    ```json
    {
      "kategori_pemasukan": [
        {"id": 1, "nama": "Pemasukan 1"},
        {"id": 2, "nama": "Pemasukan 2"}
      ],
      "kategori_pengeluaran": [
        {"id": 3, "nama": "Pengeluaran 1"},
        {"id": 4, "nama": "Pengeluaran 2"}
      ]
    }
    ```
  - **401 Unauthorized**: Pengguna tidak memiliki akses atau belum terautentikasi.

---

### `POST /api/kategori/`

- **Deskripsi**: API untuk membuat kategori baru untuk pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Parameter Body**:
  - `nama`: Nama kategori.
  - `jenis_kategori` : Jenis kategori.
- **Respon**:
  - **201 Created**
    ```json
    {"message": "Kategori berhasil dibuat!"}
    ```
  - **400 Bad Request**: Kesalahan input atau kategori sudah ada.
    ```json
    {"error": "Kategori ini sudah pernah dibuat!"}
    ```
---

## 2. Anggaran API

### `GET /api/anggaran/`

- **Deskripsi**: API untuk mengambil daftar semua anggaran milik pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Respon**:
  - **200 OK**
    ```json
    [
      {
        "id": 1,
        "nominal": 500000,
        "deskripsi": "Anggaran Bulanan",
        "kategori": "Belanja",
        "tanggal_mulai": "2024-01-01",
        "tanggal_selesai": "2024-01-31",
        "sisa": 200000,
        "persentase": 60
      },
      {
        "id": 2,
        "nominal": 1000000,
        "deskripsi": "Anggaran Liburan",
        "kategori": "Liburan",
        "tanggal_mulai": "2024-02-01",
        "tanggal_selesai": "2024-02-28",
        "sisa": 750000,
        "persentase": 25
      }
    ]
    ```
  - **401 Unauthorized**: Pengguna tidak memiliki akses atau belum terautentikasi.

---

### `POST /api/anggaran/`

- **Deskripsi**: API untuk membuat anggaran baru untuk pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Parameter Body**:
  - `nominal` : Jumlah nominal anggaran.
  - `deskripsi` : Deskripsi anggaran.
  - `kategori` : ID kategori anggaran (harus tipe pengeluaran).
  - `tanggal_mulai` : Tanggal mulai anggaran.
  - `tanggal_selesai`: Tanggal selesai anggaran.
- **Respon**:
  - **201 Created**
    ```json
    {"message": "Anggaran baru berhasil dibuat!"}
    ```
  - **400 Bad Request**: Kesalahan input, seperti tanggal lampau atau kategori sudah digunakan.
    ```json
    {"error": "Tanggal yang dimasukkan tidak boleh di masa lalu!"}
    ```
    ```json
    {"error": "Anggaran dengan kategori ini sudah pernah dibuat dan masih berjalan!"}
    ```

---

## 3. Konsultan API

### `GET /api/konsultan/`

- **Deskripsi**: API untuk mengambil daftar semua konsultan yang tersedia.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Respon**:
  - **200 OK**
    ```json
    [
      {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "is_approved": true
      },
      {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "is_approved": true
      }
    ]
    ```
  - **401 Unauthorized**: Pengguna tidak memiliki akses atau belum terautentikasi.

---

### `POST /api/konsultan/`

- **Deskripsi**: API untuk menambahkan konsultan baru.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Parameter Body**:
  - `first_name`: Nama depan konsultan.
  - `last_name`: Nama belakang konsultan.
- **Respon**:
  - **201 Created**
    ```json
    {"message": "Konsultan berhasil ditambahkan!"}
    ```
  - **400 Bad Request**: Kesalahan input atau data yang tidak valid.
    ```json
    {"error": "Isian formulir tidak valid!"}
    ```

---

## 4. Konsultasi API

### `GET /api/konsultasi/`

- **Deskripsi**: API untuk mengambil daftar semua pengajuan konsultasi milik pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Respon**:
  - **200 OK**
    ```json
    [
      {
        "id": 1,
        "konsultan": "John Doe",
        "status": "Menunggu Persetujuan",
        "alasan": "Ingin diskusi tentang manajemen waktu",
        "tanggal": "2024-01-15",
        "tanggal_diajukan": "2024-01-10T10:00:00Z",
        "tanggal_diubah": "2024-01-11T12:00:00Z",
        "is_accepted": false
      }
    ]
    ```
  - **401 Unauthorized**: Pengguna tidak memiliki akses atau belum terautentikasi.

---

### `POST /api/konsultasi/`

- **Deskripsi**: API untuk mengajukan permintaan konsultasi baru dengan konsultan tertentu.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Parameter Body**:
  - `konsultan_id`: ID konsultan yang dipilih.
  - `alasan`: Alasan pengajuan konsultasi.
  - `tanggal`: Tanggal konsultasi yang diinginkan.
- **Respon**:
  - **201 Created**
    ```json
    {"message": "Pengajuan konsultasi berhasil dikirimkan!"}
    ```
  - **400 Bad Request**: Kesalahan input, seperti tanggal lampau atau data yang tidak valid.
    ```json
    {"error": "Tanggal yang dimasukkan tidak boleh tanggal yang sudah lampau!"}
    ```
    ```json
    {"error": "Pengajuan konsultasi gagal dikirim, mohon cek kembali isi form"}
    ```

---

## 5. Catatan Transaksi API

### `GET /api/catatan-transaksi/`

- **Deskripsi**: API untuk mengambil daftar semua catatan transaksi milik pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Respon**:
  - **200 OK**
    ```json
    [
      {
        "id": 1,
        "deskripsi": "Belanja bulanan",
        "nominal": 150000,
        "tanggal": "2024-01-01",
        "kategori": "Kebutuhan Rumah Tangga",
        "jenis": "Pengeluaran"
      },
      {
        "id": 2,
        "deskripsi": "Gaji",
        "nominal": 5000000,
        "tanggal": "2024-01-05",
        "kategori": "Pendapatan",
        "jenis": "Pemasukan"
      }
    ]
    ```
  - **401 Unauthorized**: Pengguna tidak memiliki akses atau belum terautentikasi.

---

### `POST /api/catatan-transaksi/`

- **Deskripsi**: API untuk membuat catatan transaksi baru untuk pengguna yang terautentikasi.
- **Headers**:
  - `Authorization: Token <user_token>`
- **Parameter Body**:
  - `deskripsi`: Deskripsi catatan transaksi.
  - `nominal`: Jumlah nominal transaksi.
  - `tanggal`: Tanggal transaksi.
  - `jenis`: Jenis transaksi (1 untuk pemasukan, 2 untuk pengeluaran).
  - `kategori`: ID kategori transaksi.
- **Respon**:
  - **201 Created**
    ```json
    {"message": "Catatan transaksi baru berhasil dibuat!"}
    ```
  - **400 Bad Request**: Kesalahan input, seperti data yang tidak valid.
    ```json
    {"error": "Isian formulir tidak valid!"}
    ```

---
