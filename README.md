## ✅ `README.md`

# CV Builder 🧑‍💼📄

CV Builder adalah aplikasi web berbasis Django yang memungkinkan pengguna membuat dan melihat tampilan preview dari CV mereka secara instan. Aplikasi ini mendukung pengisian form, preview, dan cetak langsung via browser.

---

## 🔧 Fitur

- Form input data diri pengguna (nama, kontak, pengalaman, dll)
- Preview langsung tampilan CV
- Tombol **Print CV** untuk cetak ke PDF
- Desain responsif menggunakan Bootstrap
- Sistem template modular (base.html, form.html, preview.html)

---

## 🛠️ Teknologi yang Digunakan

- Python 3
- Django 5.2
- HTML + Bootstrap
- VS Code (dev tool)
- Git + GitHub

---

## 🚀 Cara Menjalankan Aplikasi di Localhost

1. **Clone repo ini:**

   ```bash
   git clone https://github.com/fqhtmpt/cv-builder.git
   cd cv-builder
````

2. **Aktifkan virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan server Django:**

   ```bash
   python manage.py runserver
   ```

5. **Buka di browser:**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📁 Struktur Folder

```bash
cv_builder/
├── cv/
│   ├── templates/
│   │   └── cv/
│   │       ├── base.html
│   │       ├── form.html
│   │       └── preview.html
│   ├── views.py
│   ├── forms.py
│   └── models.py
├── cv_project/
│   └── settings.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---
