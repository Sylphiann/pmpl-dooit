# Design Specification Review

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

- **Dashboard Laporan Keuangan**: Halaman yang menampilkan bagian laporan keuangan berupa grafik pemasukan dan pengeluaran bagi pencatat keuangan dan daftar konsultasi bagi konsultan keuangan.
- **Tampilan Manajemen Konsultasi**: Bagian halaman untuk peran Konsultan supaya dapat menerima atau menolak permintaan konsultasi dari pencatat keuangan.

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

Basis data dirancang menggunakan model relasional dengan entitas utama seperti pengguna, transaksi, konsultasi, dan kategori. PostgreSQL dipilih untuk memastikan skalabilitas dan kinerja yang baik. Selain itu, normalisasi juga dilakukan untuk memastikan efisiensi penyimpanan dan menghindari redundansi data.

---

### Interface Design

#### User Interface (UI)

Pada dasarnya, antarmuka pengguna yang dirancang sangat memberikan kemudahan navigasi antara dashboard keuangan untuk pencatat keuangan dan manajemen konsultasi untuk konsultan keuangan. Tampilan model dashboard dipilih karena sangat sederhana dan intuitif dipilih untuk memudahkan pengguna dari segala kalangan.

Penjelasan lebih lanjut ada di dokumen: [Design Review](design_review.md)

#### API

Antarmuka pemrograman aplikasi (API) atau yang sering disebut Application Programming Interface digunakan untuk menghubungkan bagian frontend dengan backend supaya dapat menangani permintaan data dari klien, serta menyediakan layanan untuk pencatatan transaksi dan pengelolaan konsultasi.

---

### Security and Privacy

#### Authentication

Aplikasi Dooit menggunakan mekanisme autentikasi untuk memastikan bahwa hanya pengguna yang terdaftar dapat mengakses sistem. Pengguna harus melalui proses login yang aman dengan validasi kredensial menggunakan metode enkripsi untuk menjaga keamanan informasi selama proses autentikasi.

#### Authorization

Akses kontrol dilakukan dengan mekanisme berbasis peran supaya bisa dipastikan hanya pengguna dengan otoritas yang sesuai yang dapat mengakses data tertentu (misalnya, konsultan hanya dapat mengakses permintaan konsultasi dan sebaliknya).

#### Data Protection

Semua data yang terkait dengan keuangan dan pengguna disimpan dalam basis data dengan enkripsi untuk menjaga keamanan dan privasi pengguna. Data juga dilindungi dari potensi kebocoran atau akses tidak sah yang dapat merugikan pengguna.

---

### Error Handling and Logging

#### Error Code Message

Setiap error yang terjadi dalam aplikasi dikategorikan dan ditampilkan dengan pesan yang jelas agar pengguna dapat mengetahui jenis kesalahan yang terjadi. Kode error yang sesuai juga ditampilkan untuk memudahkan penyelesaian masalah baik oleh pengguna ataupun pengembang aplikasi.

#### Logging Mechanisms

Mekanisme logging diterapkan untuk mencatat setiap error dan aktivitas penting di aplikasi Doot. Data log ini nantinya disimpan di server untuk referensi dan debugging lebih lanjut supaya aplikasi Dooit bisa berjalan dengan lancar.

---

### Testing Strategy

#### Unit testing approach

Pada bagian pengujian unit, digunakan framework Django TestCase karena  mendukung pengujian fitur dasar seperti pencatatan transaksi, pengelolaan kategori, dan konsultasi keuangan. Pengujian ini bertujuan untuk memastikan bahwa setiap fungsi berjalan sesuai dengan harapan.

#### Usability Testing

Selain melakukan unit test, usability testing juga dilakukan untuk memastikan bahwa pengguna dapat dengan mudah memahami dan menggunakan antarmuka (UI) aplikasi. Pengujian ini dilakukan dengan berfokus pada kemudahan navigasi, aksesibilitas fitur, dan kepuasan pengguna dalam menggunakan aplikasi Dooit.

#### Performance Testing

Performance testing juga direncanakan untuk dilakukan supaya bisa dipastikan bahwa aplikasi dapat menangani beban kerja dengan baik, terutama ketika banyak transaksi dilakukan sekaligus. Hal ini dilakukan dengan maksud untuk menjaga performa dan skalabilitas dari aplikasi Dooit saat digunakan oleh banyak pengguna secara bersamaan.

#### Acceptance criteria

Kriteria penerimaan ditentukan berdasarkan fungsionalitas utama dari Dooit, yaitu fitur pencatatan transaksi, manajemen anggaran, dan fitur konsultasi yang berjalan sesuai dengan kebutuhan bisnis pengguna.

---

### Deployment and Maintenance

#### Deployment process

Proses deployment dilakukan menggunakan Railway, platform yang mendukung deployment aplikasi web secara otomatis. Deployment juga dilakukan secara berkelanjutan setelah setiap update atau perubahan fitur diuji dan dipastikan stabil pada kondisi production.

#### Monitoring and alerting

Proses monitoring dan logging dilakukan melalui Railway untuk memantau status server dan keseluruhan performa aplikasi. Selain itu, kami juga menggunakan teknologi seperti **SonarQube** untuk menginspeksi kode supaya kami dapat memastikan kualitas dan standar kode yang baik sebelum aplikasi di-deploy.

---

## Review and Feedback

- Beberapa pengguna memberikan umpan balik awal yang menunjukkan bahwa proses konsultasi dapat lebih disederhanakan agar lebih user-friendly. 
- Beberapa kasus pengujian juga menyoroti pentingnya validasi yang lebih baik dalam proses input data. 

---
