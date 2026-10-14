# Dashboard Statistik Deskriptif - Flask

## Menjalankan di Windows
1. Buka terminal pada folder project.
2. Buat virtual environment:
   `python -m venv .venv`
3. Aktifkan:
   `.venv\Scripts\activate`
4. Install:
   `pip install -r requirements.txt`
5. Jalankan:
   `python app.py`
6. Buka browser:
   `http://127.0.0.1:5000`

Dashboard menggunakan Flask + HTML + CSS + Vanilla JavaScript. Tidak membutuhkan database dan tidak memakai library chart eksternal.

## Isi dashboard
- KPI total observasi, mean keseluruhan, standard deviation, dan gap mean.
- Bar chart mean per variabel.
- Histogram frekuensi skor 1–10.
- Heatmap 10×10.
- Tabel statistik deskriptif.
- Analisis otomatis dan rekomendasi keputusan.
- Tombol unduh CSV.

## Catatan
Nama Column1–Column10 masih generik. Jika setiap column punya nama indikator sebenarnya, ganti field `columns` dan data pada `data/data.json`.
