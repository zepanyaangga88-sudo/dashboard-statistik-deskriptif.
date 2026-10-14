# Panduan hosting

Project siap deploy ke layanan hosting Python seperti Render.

1. Ekstrak ZIP.
2. Upload seluruh isi folder project ke repository GitHub.
3. Login ke https://render.com lalu pilih New + > Web Service.
4. Hubungkan repository GitHub.
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`
7. Pilih paket yang tersedia, lalu klik Deploy.
8. Buka URL publik yang diberikan setelah deploy selesai.

Project ini tidak memerlukan database. Paket gratis hosting dapat memiliki batasan dan kebijakan yang berubah, jadi periksa ketentuan terbaru penyedia. Jangan unggah data rahasia ke hosting publik.
