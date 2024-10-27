# Testing Strategy

## Table of Contents

- [Testing Strategy](#testing-strategy)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Purpose of Testing Strategy](#purpose-of-testing-strategy)
    - [Testing Objectives](#testing-objectives)
  - [Types of Testing](#types-of-testing)
    - [Unit Testing](#unit-testing)
    - [Functional Testing](#functional-testing)
    - [Performance Testing](#performance-testing)
  - [Testing Environment](#testing-environment)
    - [Local Testing Environment](#local-testing-environment)
    - [CI/CD Pipeline Integration](#cicd-pipeline-integration)
  - [Test Automation](#test-automation)
    - [Continuous Integration (CI) and Continuous Deployment (CD)](#continuous-integration-ci-and-continuous-deployment-cd)
  - [Test Case Management](#test-case-management)
    - [Test Case Design](#test-case-design)
    - [Test Case Documentation](#test-case-documentation)
    - [Test Case Prioritization](#test-case-prioritization)
  - [Test Execution Process](#test-execution-process)
    - [Test Scheduling and Frequency](#test-scheduling-and-frequency)
  - [Reporting and Metrics](#reporting-and-metrics)
    - [Test Result Reporting](#test-result-reporting)
    - [Bug Tracking and Issue Resolution](#bug-tracking-and-issue-resolution)
    - [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
  - [Maintenance of Test Strategy](#maintenance-of-test-strategy)
    - [Review and Update Cycle](#review-and-update-cycle)
    - [Continuous Improvement](#continuous-improvement)

## Introduction

### Purpose of Testing Strategy

Strategi pengujian ini bertujuan untuk memastikan bahwa proyek Dooit memenuhi standar kualitas perangkat lunak yang tinggi melalui pengujian menyeluruh di setiap fase siklus hidup pengembangan perangkat lunak. Pengujian membantu mengidentifikasi kesalahan dan memastikan bahwa sistem berfungsi sebagaimana mestinya sebelum dirilis ke pengguna.

### Testing Objectives

- Mengidentifikasi dan memperbaiki bug lebih awal untuk mengurangi biaya perbaikan di masa depan.
- Memastikan bahwa fungsionalitas utama Dooit dapat berfungsi dengan baik.
- Memastikan performa sistem sesuai dengan standar yang telah ditetapkan.

## Types of Testing

### Unit Testing

Unit testing dilakukan untuk memverifikasi bahwa setiap unit atau komponen individual berfungsi dengan benar.

- **Tools Used**: Menggunakan framework Django Test Case untuk memastikan pengujian yang efektif.
- **Test Coverage**: Menargetkan cakupan pengujian minimal 85% untuk memastikan bahwa sebagian besar kode diuji dengan baik.

### Functional Testing

Functional testing dilakukan untuk memastikan bahwa semua fungsi perangkat lunak bekerja sesuai persyaratan yang telah ditentukan.

- **User Acceptance Testing (UAT)**: Menguji sistem dengan melibatkan pengguna akhir untuk memastikan bahwa sistem memenuhi kebutuhan dan harapan mereka. [Link UAT](https://docs.google.com/spreadsheets/d/1YQqmOEBzx_XG3KdagBaLgjcqNArMwhS743xjrZ9dvd0/edit?gid=996467625#gid=996467625)

### Performance Testing

Performance testing memastikan bahwa aplikasi berfungsi dengan baik di bawah beban tertentu.

- **Load Testing**: Menguji bagaimana sistem berperilaku di bawah beban pengguna normal.
## Testing Environment

### Local Testing Environment

Pengujian dilakukan di lingkungan lokal sebelum diintegrasikan ke dalam pipeline CI/CD untuk memastikan bahwa tidak ada bug besar sebelum pengembangan lebih lanjut.

### CI/CD Pipeline Integration

Pengujian diintegrasikan ke dalam pipeline **CI/CD** untuk memastikan bahwa setiap perubahan kode diuji secara otomatis sebelum digabungkan ke dalam branch utama.

## Test Automation

### Continuous Integration (CI) and Continuous Deployment (CD)

CI/CD dilakukan dengan menggunakan Github Actions untuk mengotomatisasi pengujian setiap kali ada perubahan kode supaya bisa memastikan bahwa regresi dapat dideteksi dan diperbaiki dengan cepat.

## Test Case Management

### Test Case Design

Desain test case dilakukan berdasarkan spesifikasi persyaratan untuk memastikan semua fungsionalitas diuji.

### Test Case Documentation

Setiap test case terdokumentasi dengan baik, termasuk langkah-langkah pengujian, data yang diperlukan, dan hasil pengujian yang diharapkan.

### Test Case Prioritization

Test case diprioritaskan berdasarkan risiko dan dampak terhadap sistem. Fungsi inti aplikasi Dooit yang memiliki dampak besar akan diuji terlebih dahulu.

## Test Execution Process

### Test Scheduling and Frequency

Pengujian dilakukan secara berkala dengan pengujian regresi setiap kali ada pembaruan pada repository.

## Reporting and Metrics

### Test Result Reporting

Hasil pengujian dicatat dan dilaporkan untuk memberikan laporan pengujian yang terstruktur dan mudah dipahami.

### Bug Tracking and Issue Resolution

Bug yang ditemukan selama pengujian dicatat di sheets untuk pelacakan dan penyelesaian yang efisien.

### Key Performance Indicators (KPIs)

- **Test Coverage**: Persentase kode yang diuji oleh unit test.
- **Test Execution Success Rate**: Mengukur persentase pengujian yang berhasil dijalankan tanpa error.

## Maintenance of Test Strategy

### Review and Update Cycle

Strategi pengujian ditinjau dan diperbarui secara berkala untuk memastikan relevansi pengujian dengan perubahan dalam pengembangan perangkat lunak.

### Continuous Improvement

Pendekatan **Continuous Improvement** diadopsi untuk memastikan bahwa proses pengujian menjadi lebih efisien dari waktu ke waktu dengan belajar dari hasil pengujian sebelumnya dan feedback dari tim.
