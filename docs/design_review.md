# Design Review

**Author**: Ahmad Rafi Wirana  
**Purpose**: Design Review for PMPL Course

---

## Introduction

Tinjauan desain ini bertujuan untuk mengevaluasi desain aplikasi Dooit yang telah dikembangkan sebagai platform manajemen keuangan berbasis web. Aplikasi ini dirancang untuk membantu pemilik bisnis dalam mengelola transaksi keuangan, merencanakan anggaran, dan berkonsultasi dengan pakar keuangan. Dalam tinjauan ini, akan dijelaskan keputusan desain yang diambil, kekuatan, kelemahan, serta saran perbaikan yang dapat diterapkan untuk meningkatkan kualitas desain sistem aplikasi web secara keseluruhan.

---

## Design Objectives

Aplikasi Dooit memiliki beberapa tujuan desain utama:

- **Sederhana dan Minimalis**: Aplikasi web harus memiliki desain antarmuka yang sederhana dan minimalis supaya pengguna dapat dengan mudah dalam melakukan navigasi. Selain itu, desain yang minimalis juga dapat membuat pengguna baru yang pertama kali memakai aplikasi web Dooit bisa dengan mudah menggunakannya.
- **Efisien**: Setiap fitur utama, seperti pencatatan transaksi, pembuatan anggaran, dan konsultasi harus dapat diakses dengan cepat tanpa terlalu banyak langkah navigasi.
- **Responsif**: Aplikasi Dooit harus dapat bekerja dengan baik pada berbagai ukuran layar, termasuk perangkat desktop dan seluler.

---

## Design Choices

- **Sidebar Navigasi**: Navigasi aplikasi yang diletakkan pada sidebar di sisi kiri dengan ikon yang jelas dan teks deskriptif dapat mempermudah pengguna berpindah antar halaman.
- **Pemisahan Fungsi Berdasarkan Peran**: Desain dari aplikasi memungkinkan pemisahan antara fungsi pencatat keuangan dan konsultan keuangan sehingga pengguna dengan peran yang berbeda mendapatkan tampilan dan akses fitur yang sesuai dengan peran mereka.
- **Visualisasi Interaktif**: Laporan keuangan memiliki tampilan visualisasi dalam bentuk grafik, seperti grafik garis untuk membandingkan pemasukan dan pengeluaran sehingga dapat memberikan gambaran yang lebih mudah dipahami oleh pengguna.

---

## Evaluation of Design

### Strengths

- **Antarmuka Sederhana**: Desain menggunakan elemen-elemen antarmuka yang sangat minimalis sehingga memudahkan pengguna dalam memahami fitur utama dan navigasi aplikasi. Penggunaan sidebar navigasi yang jelas juga sangat mempermudah akses navigasi ke berbagai fitur fitur utama Dooit.
- **Visualisasi Data yang Informatif**: Penggunaan visualisasi grafik yang membandingkan pemasukan dan pengeluaran sangat membantu pengguna dalam menganalisis kondisi keuangan mereka secara cepat.

---

### Weaknesses

- **Minimasi Informasi di Halaman Kosong**: Pada halaman seperti Anggaran dan Konsultasi, ketika data tidak tersedia, hanya muncul ikon kosong tanpa informasi tambahan. Hal ini bisa membuat pengguna merasa kurang tahu apa yang harus dilakukan selanjutnya.
- **Antarmuka Terlalu Umum**: Antarmuka (UI) saat ini terlihat terlalu sederhana dan kurang mencerminkan tampilan profesional yang diharapkan oleh pengguna pada umumnya, terutama dari kalangan pebisnis.
- **Kurangnya Standar Desain**: Desain sidebar dan navbar saat ini tidak sepenuhnya memanfaatkan prinsip desain antarmuka untuk aplikasi yang berupa platform keuangan dan memerlukan peningkatan untuk menyelaraskan dengan standar umum desain antarmuka.

---

### Suggested Improvements

- **Tingkatkan Profesionalitas pada Antarmuka**: Desain antarmuka aplikasi Dooit saat ini seharusnya lebih profesional untuk mencerminkan penggunaan aplikasi di kalangan pebisnis. Cara perbaikan ini bisa termasuk dengan perbaikan pada penggunaan skema warna, tipografi (teks), dan tata letak yang lebih formal dan terstandarisasi.
- **Tingkatkan Konsistensi Desain Antar Halaman**: Pada dasarnya, untuk menciptakan pengalaman pengguna yang lebih mulus, konsistensi desain antar halaman sangat penting. Elemen seperti tombol, margin, navigasi, dan ukuran font sebaiknya seragam di seluruh aplikasi. Keselarasan ini akan memberikan kesan aplikasi yang lebih terorganisir dan membantu pengguna dalam memahami interaksi antarmuka dengan lebih baik.

---
