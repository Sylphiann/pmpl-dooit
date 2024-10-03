# Design Spec Review

**Author**: Ahmad Rafi Wirana  
**Purpose**: Design Specification Review for PMPL Course

---

## Overview

Dooit adalah aplikasi manajemen keuangan berbasis web yang dirancang untuk membantu pemilik bisnis dalam mengelola transaksi keuangan mereka, merencanakan anggaran, dan berkonsultasi dengan pakar keuangan. Sistem aplikasi web ini bertujuan untuk menyederhanakan pelaporan keuangan dan menyediakan platform konsultasi untuk membantu pemilik bisnis dalam mengambil keputusan keuangan yang lebih baik.

---

## System Architecture

### Models

- **Pencatat Keuangan**: Peran sebagai Pemilik Bisnis yang bertanggung jawab mencatat transaksi keuangan, baik pemasukan maupun pengeluaran.
- **Konsultan Keuangan**: Peran sebagai Konsultan yang membantu pemilik bisnis dengan memberikan konsultasi mengenai perencanaan keuangan dan pengelolaan anggaran.

---

### Views

- **Dashboard Laporan Keuangan**: Layar yang menampilkan bagian laporan keuangan berupa grafik pemasukan dan pengeluaran bagi pencatat keuangan dan daftar konsultasi bagi konsultan keuangan.
- **Tampilan Manajemen Konsultasi**: Bagian layar untuk peran Konsultan supaya dapat menerima atau menolak permintaan konsultasi dari pencatat keuangan.

---

### Templates

- **Template Dashboard**: Template ini digunakan untuk menampilkan dashboard keuangan bagi pengguna yang disesuaikan dengan peran mereka, baik pencatat keuangan maupun konsultan.
- **Template Konsultasi**: Template untuk mengelola konsultasi, termasuk pengajuan dan penerimaan konsultasi melalui ruang obrolan.

---

### Static Files

- Berkas statis seperti CSS dan JavaScript diorganisir dalam direktori `static/` untuk menangani antarmuka pengguna dan elemen interaktif seperti pengelolaan transaksi dan konsultasi.

---

## Design Decisions

### Database Design

Basis data dirancang menggunakan model relasional dengan entitas utama seperti pengguna, transaksi, konsultasi, dan kategori. Normalisasi dilakukan untuk memastikan efisiensi penyimpanan dan menghindari redundansi data.

---

### Interface Design 

#### User Interface (UI)

Pada dasarnya, antarmuka pengguna yang dirancang sangat memberikan kemudahan navigasi antara dashboard keuangan untuk pencatat keuangan dan manajemen konsultasi untuk konsultan keuangan. Tampilan model dashboard sangat sederhana dan intuitif dipilih untuk memudahkan pengguna.

Penjelasan lebih lanjut ada di dokumen: [Design Review](design_review.md)

#### API

#### Internationalization (i18n) and Localization (l10n) 

---

### Security and Privacy

#### Authentication:

Aplikasi menggunakan otentikasi dan otorisasi untuk membatasi akses berdasarkan peran pengguna. Verifikasi data konsultan dilakukan setelah pendaftaran, dan semua data keuangan disimpan secara aman dengan enkripsi.

#### Authorization:

#### Data Protection:

---

### Error Handling and Logging

#### Error Code Message:

#### Logging Mechanisms:

---

### Testing Strategy

#### Unit testing approach

#### Acceptance criteria

---

## Review and Feedback

---

