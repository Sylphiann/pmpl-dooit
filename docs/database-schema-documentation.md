# Dokumentasi Skema Database Dooit

Dokumentasi ini merupakan deskripsi singkat tentang skema database untuk proyek Dooit, termasuk deskripsi setiap tabel (model), kolom-kolomnya, dan relasi antar model.

## Daftar Isi

- [Dokumentasi Skema Database Dooit](#dokumentasi-skema-database-dooit)
  - [Daftar Isi](#daftar-isi)
  - [1. Anggaran](#1-anggaran)
  - [2. Catatantransaksi](#2-catatantransaksi)
  - [3. Catatantransaksi Jenistransaksi](#3-catatantransaksi-jenistransaksi)
  - [4. Kategori](#4-kategori)
  - [5. Konsultan](#5-konsultan)
  - [6. Konsultasi](#6-konsultasi)
  - [7. UsersCustomuser](#7-userscustomuser)
  - [8. UsersCustomuserprofile](#8-userscustomuserprofile)

---

## 1. Anggaran

**Deskripsi**: Tabel mengenai anggaran keuangan.

| Kolom           | Tipe        | Deskripsi                              |
|-----------------|-------------|----------------------------------------|
| nominal         | Float       | Jumlah anggaran                        |
| deskripsi       | CharField   | Deskripsi anggaran                     |
| tanggal_mulai   | DateField   | Tanggal mulai anggaran                 |
| tanggal_selesai | DateField   | Tanggal selesai anggaran               |
| kategori        | OneToOne    | Foreign key ke `Kategori`      |
| user            | ForeignKey  | Foreign key ke `UsersCustomuser`       |

---

## 2. Catatantransaksi

**Deskripsi**: Tabel yang mencatat detail transaksi.

| Kolom        | Tipe        | Deskripsi                                  |
|--------------|-------------|--------------------------------------------|
| deskripsi    | CharField   | Deskripsi transaksi                        |
| nominal      | Float       | Jumlah transaksi                           |
| tanggal      | DateField   | Tanggal transaksi                          |
| jenis        | ForeignKey  | Foreign key ke `CatatantransaksiJenistransaksi` |
| kategori     | ForeignKey  | Foreign key ke `Kategori`          |
| pencatat     | ForeignKey  | Foreign key ke `UsersCustomuser`           |

---

## 3. Catatantransaksi Jenistransaksi

**Deskripsi**: Tabel mewakili jenis-jenis transaksi.

| Kolom        | Tipe              | Deskripsi                  |
|--------------|-------------------|----------------------------|
| jenis        | PositiveSmallInt   | Jenis transaksi            |

---

## 4. Kategori

**Deskripsi**: Tabel mewakili kategori untuk transaksi.

| Kolom           | Tipe        | Deskripsi                              |
|-----------------|-------------|----------------------------------------|
| nama            | CharField   | Nama kategori                          |
| jenis_kategori  | ForeignKey  | Foreign key ke `CatatantransaksiJenistransaksi` |
| user            | ForeignKey  | Foreign key ke `UsersCustomuser`       |

---

## 5. Konsultan

**Deskripsi**: Tabel ini mewakili konsultan dalam sistem.

| Kolom           | Tipe        | Deskripsi                              |
|-----------------|-------------|----------------------------------------|
| first_name      | CharField   | Nama depan konsultan                   |
| last_name       | CharField   | Nama belakang konsultan                |
| is_approved     | Boolean     | Status persetujuan konsultan           |
| user            | OneToOne    | Foreign key ke `UsersCustomuser`       |
| user_profile    | OneToOne    | Foreign key ke `UsersCustomuserprofile` |

---

## 6. Konsultasi

**Deskripsi**: Tabel ini menyimpan catatan konsultasi.

| Kolom        | Tipe        | Deskripsi                              |
|--------------|-------------|----------------------------------------|
| status       | CharField   | Status konsultasi                      |
| alasan       | TextField   | Alasan konsultasi                      |
| tanggal      | DateField   | Tanggal konsultasi                     |
| is_accepted  | Boolean     | Apakah konsultasi diterima             |
| klien        | ForeignKey  | Foreign key ke `UsersCustomuser`       |
| konsultan    | ForeignKey  | Foreign key ke `Konsultan`    |

---

## 7. UsersCustomuser

**Deskripsi**: Tabel dengan model pengguna khusus yang menyimpan informasi pengguna.

| Kolom           | Tipe        | Deskripsi                              |
|-----------------|-------------|----------------------------------------|
| password        | CharField   | Password pengguna (di-hash)            |
| company_name    | CharField   | Nama perusahaan                        |
| username        | CharField   | Nama pengguna, unik                    |
| email           | CharField   | Email pengguna, unik                   |
| role            | PositiveSmallInt | Peran pengguna                    |
| date_joined     | DateTimeField | Tanggal registrasi pengguna          |
| last_login      | DateTimeField | Tanggal login terakhir               |
| created_date    | DateTimeField | Tanggal pembuatan pengguna           |
| modified_date   | DateTimeField | Tanggal perubahan terakhir           |
| is_admin        | Boolean     | Apakah pengguna adalah admin           |
| is_staff        | Boolean     | Apakah pengguna adalah staf            |
| is_active       | Boolean     | Apakah pengguna aktif                  |
| is_superadmin   | Boolean     | Apakah pengguna adalah superadmin      |

---

## 8. UsersCustomuserprofile

**Deskripsi**: Tabel yang menyimpan data profil tambahan untuk pengguna.

| Kolom              | Tipe        | Deskripsi                              |
|--------------------|-------------|----------------------------------------|
| company_prof_pic   | CharField   | Path ke foto profil pengguna           |
| company_bio        | CharField   | Biografi pengguna                      |
| user               | OneToOne    | Foreign key ke `UsersCustomuser`       |

---
