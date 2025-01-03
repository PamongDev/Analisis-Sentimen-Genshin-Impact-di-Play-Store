# Sentiment Analysis

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis sentimen pada ulasan aplikasi dengan menggunakan model pembelajaran mesin. Data yang digunakan diambil dari ulasan pengguna pada platform tertentu. Proses analisis melibatkan langkah-langkah preprocessing, ekstraksi fitur menggunakan BERT, dan pembangunan model prediktif untuk mengklasifikasikan sentimen.

## Langkah-langkah Proyek

### 1. Pengumpulan Data
Data dikumpulkan menggunakan Google Play Scraper, dengan parameter:
- Aplikasi: Genshin Impact
- Bahasa: Bahasa Indonesia
- Negara: Indonesia
- Jumlah Ulasan: 1000 ulasan

### 2. Preprocessing Data
Langkah-langkah preprocessing data meliputi:
- **Pembersihan Data**: Menghapus ulasan yang kosong, duplikat, atau mengandung informasi yang tidak relevan.
- **Normalisasi Teks**: Mengubah teks menjadi huruf kecil, menghapus tanda baca, angka, dan karakter khusus.
- **Tokenisasi**: Memecah teks menjadi token untuk analisis lebih lanjut.

### 3. Ekstraksi Fitur
Ekstraksi fitur dilakukan menggunakan model **BERT (Bidirectional Encoder Representations from Transformers)**. Langkah-langkahnya adalah:
- Memuat model BERT yang telah dilatih sebelumnya.
- Mengekstraksi representasi fitur dari teks ulasan.
- Menghasilkan embedding untuk setiap ulasan sebagai input ke model klasifikasi.

### 4. Pembangunan Model
Model prediktif yang digunakan meliputi:
- **Support Vector Machine (SVM)**
- **Logistic Regression**

Model dilatih menggunakan data training dan dievaluasi menggunakan metrik akurasi, presisi, recall, dan F1-score.

## Hasil Analisis
Hasil dari proses analisis sentimen menunjukkan bahwa:
- Model **Logistic Regression** memberikan performa terbaik dengan akurasi 85%.
- Model dapat membedakan sentimen positif dan negatif secara efektif.

## Kesimpulan
Proyek ini menunjukkan bahwa pendekatan menggunakan **BERT untuk ekstraksi fitur** dapat meningkatkan akurasi klasifikasi sentimen. Pendekatan ini dapat diterapkan pada berbagai jenis teks ulasan untuk mendapatkan wawasan yang lebih mendalam mengenai persepsi pengguna.
