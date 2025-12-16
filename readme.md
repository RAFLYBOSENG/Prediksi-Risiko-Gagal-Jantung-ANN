# TA-11 — Evaluasi Model ANN (Prediksi Risiko Gagal Jantung)

Deskripsi

- Proyek ini menampilkan hasil evaluasi model Artificial Neural Network (ANN) yang dilatih pada dataset `heart_failure_clinical_records_dataset.csv`.
- Visualisasi (grafik loss/accuracy, heatmap korelasi, confusion matrix) disimpan dalam folder `static/` dan dirender lewat aplikasi Flask sederhana.

Struktur Proyek (ringkas)

- `app.py` — Aplikasi Flask yang merender `templates/index.html` dan melayani berkas statis dari `static/`.
- `model.ipynb` — Notebook untuk preprocessing, melatih model, menghasilkan visualisasi, dan menyimpan gambar ke `static/`.
- `static/` — Berisi gambar yang dirender: `training_validation_loss.png`, `training_validation_accuracy.png`, `correlation_heatmap.png`, `confusion_matrix.png`.
- `templates/index.html` — Template Jinja2 yang menampilkan gambar-gambar tersebut.
- `dataset/heart_failure_clinical_records_dataset.csv` — Data sumber.

Persyaratan

Pastikan Python 3.10+ (atau sesuai environment) dan dependency diinstal:

```bash
pip install -r requirements.txt
```

Menjalankan aplikasi Flask (lokal)

1. Aktifkan virtual environment jika ada.
2. Jalankan aplikasi:

```bash
python app.py
```

3. Buka browser ke: `http://127.0.0.1:5000/`

Debug & pengecekan file statis

- Untuk mengecek apakah Flask melihat folder `static` dan file yang ada, buka:
  - `http://127.0.0.1:5000/debug` — menampilkan path `static` dan daftar file.
  - Contoh akses langsung untuk memastikan file tersedia (ganti nama file jika perlu):
    - `http://127.0.0.1:5000/static/training_validation_loss.png`
    - `http://127.0.0.1:5000/static/training_validation_accuracy.png`
    - `http://127.0.0.1:5000/static/correlation_heatmap.png`
    - `http://127.0.0.1:5000/static/confusion_matrix.png`

Jika gambar tidak muncul di halaman

- Pastikan file gambar benar-benar ada di folder `static/` (lihat listing di root `static/`).
- Jika file ada tetapi terlihat kosong/putih, jalankan ulang `model.ipynb` (jalankan semua sel) untuk menghasilkan ulang gambar yang disimpan dengan `plt.savefig("static/...")`.
- Periksa Developer Tools → Network pada browser: apakah request ke `/static/<file>` mengembalikan status 200 atau 404/500? Jika 404, periksa nama file dan path.

Catatan tentang `model.ipynb`

- Notebook menyimpan gambar ke `static/` saat sel-sel yang membuat plot dipanggil. Jika Anda menjalankan notebook di Jupyter, jalankan sel sampai gambar tersimpan.
- Nama gambar yang digunakan di template: `training_validation_loss.png`, `training_validation_accuracy.png`, `correlation_heatmap.png`, `confusion_matrix.png`.

Langkah cepat untuk memperbaiki masalah umum

1. Jalankan `python app.py` dan buka `/debug`.
2. Jika `/debug` menampilkan file-file yang benar, buka masing-masing file static langsung di browser.
3. Jika file tidak ada, buka `model.ipynb` dan jalankan semua sel untuk menghasilkan gambar.
