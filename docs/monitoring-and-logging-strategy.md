# Monitoring and Logging Strategy

## Table of Contents

- [Monitoring and Logging Strategy](#monitoring-and-logging-strategy)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Objectives](#objectives)
  - [Monitoring Strategy](#monitoring-strategy)
    - [Key Metrics untuk Monitoring](#key-metrics-untuk-monitoring)
    - [Monitoring Tools](#monitoring-tools)
    - [Alerts and Notifications](#alerts-and-notifications)
  - [Logging Strategy](#logging-strategy)
    - [Logging Levels](#logging-levels)
    - [Structured Logging](#structured-logging)
    - [Error Tracking](#error-tracking)
    - [Log Management](#log-management)
  - [Reporting and Metrics](#reporting-and-metrics)
    - [Performance Dashboards](#performance-dashboards)
    - [Reporting Mechanisms for Key Metrics](#reporting-mechanisms-for-key-metrics)

---

## Introduction

### Objectives

Dokumen ini bertujuan untuk membuat rumusan strategi monitoring dan logging untuk proyek Dooit. Strategi ini dirancang untuk memastikan keandalan (reliability), ketersediaan (availability), dan pemeliharaan (maintenance) sistem dengan menyediakan wawasan/dokumentasi yang berkelanjutan tentang kinerja dan kesehatan sistem. Prinsip-prinsip yang ada di dokumen ini sejatinya berasal dari konsep Software Quality Assurance (SQA) dan pada dokumentasi ini kami memastikan tindakan yang dilakukan berupa tindakan proaktif yang diambil untuk mengidentifikasi dan menyelesaikan masalah sebelum berdampak pada pengguna.

## Monitoring Strategy

### Key Metrics untuk Monitoring

Pada dasarnya, monitoring sangat penting untuk menjaga kualitas sistem dan memastikan bahwa setiap masalah teridentifikasi lebih awal. Beberapa metrik kunci yang dimonitor merupakan:

- **Waktu Aktif (Uptime)**: Mengukur ketersediaan sistem. Memastikan waktu aktif sangat penting untuk menyediakan layanan yang berkelanjutan bagi pengguna.
- **Waktu Respons**: Memantau seberapa cepat sistem merespons permintaan pengguna. Metrik ini membantu untuk menilai pengalaman pengguna.
- **Latensi**: Melacak keterlambatan dalam transmisi data. Latensi rendah diperlukan untuk sistem yang responsif.
- **Penggunaan CPU dan Memori**: Membantu memahami penggunaan sumber daya dan mendeteksi potensi bottleneck atau kebocoran memori.
- **Disk I/O**: Mengukur kinerja baca/tulis sistem. Disk I/O yang tinggi dapat mengindikasikan bottleneck kinerja.

### Monitoring Tools

- **Prometheus**: Digunakan untuk mengumpulkan metrik dan memberikan peringatan secara real-time berdasarkan ambang batas.
- **Grafana**: Digunakan karena dapat meembuat visualisasi metrik dengan cara yang mudah dipahami, memungkinkan pemahaman kondisi sistem dari waktu ke waktu.

### Alerts and Notifications

Alert pada tahap productions digunakan untuk memastikan respons yang cepat terhadap masalah aplikasi Dooit, seperti:

- **Peringatan Threshold**: Ditetapkan untuk metrik kunci (misalnya, penggunaan CPU di atas 90% selama kurang lebih 5 menit, waktu respons API yang melebihi 500ms, dsb).
- **Notifikasi Channels**: Peringatan dikirim melalui saluran seperti Slack, email, atau SMS untuk memastikan anggota tim yang relevan segera diberitahu.

## Logging Strategy

### Logging Levels

Logging sangat penting untuk memahami perilaku sistem dan menyelesaikan masalah secara efektif karena pesan yang ditampilkan bisa sangat jelas. Pada kasus ini, ada tingkatan logging yang digunakan meliputi:

- **Info**: Informasi umum sistem, seperti keberhasilan memulai layanan atau login pengguna.
- **Peringatan**: Masalah non-kritis yang perlu diperhatikan tetapi tidak mempengaruhi fungsionalitas inti.
- **Error**: Log yang menunjukkan kegagalan dalam bagian sistem yang perlu diperbaiki.
- **Kritis**: Masalah serius yang dapat menyebabkan gangguan layanan dan memerlukan perhatian segera.

### Structured Logging

Hal ini dilakukan untuk memastikan log konsisten dan mudah diparsing:

- **Format dan Struktur Log**: Log harus dalam format terstruktur (misalnya, JSON) yang mencakup bidang seperti timestamp, tingkat keparahan, pesan, dan konteks.
- **Contoh Entri Log**:
  ```json
  {
    "timestamp": "2024-10-27T14:45:00Z",
    "level": "ERROR",
    "message": "Koneksi database gagal",
    "context": {
      "service": "user-auth",
      "request_id": "abc123"
    }
  }
  ```

### Error Tracking

- **Sentry**: Digunakan untuk melacak kesalahan aplikasi dan memberikan wawasan rinci tentang penyebab kegagalan, seperti stack trace dan konteks. Ini membantu mengidentifikasi pola dan masalah umum.

### Log Management

- **Penyimpanan Log**: Log disimpan di lokasi pusat agar mudah diakses.
- **Kebijakan Retensi**: Log disimpan selama 90 hari supaya bisa memastikan waktu yang cukup untuk audit dan analisis dari tim internal.

## Reporting and Metrics

### Performance Dashboards

- Dasbor dibuat menggunakan Grafana untuk memvisualisasikan metrik kinerja seperti waktu aktif, waktu respons, dan penggunaan sumber daya. Hal ini dilakukan supaya dapat memberikan gambaran cepat tentang kesehatan sistem.

### Reporting Mechanisms for Key Metrics

- **Laporan Waktu Respons dan Waktu Aktif**: Laporan ini dibuat setiap minggu untuk menilai keandalan sistem.
- **Laporan Frekuensi Error**: Data log dan pelacakan error dianalisis untuk mengidentifikasi masalah umum sehingga bisa membantu prioritas perbaikan dan peningkatan.

---
