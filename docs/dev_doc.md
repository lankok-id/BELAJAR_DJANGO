# Product CRUD System (Django + DRF Serializer)

Aplikasi manajemen inventaris produk yang dibangun dengan **Django**.
Project ini menggunakan **Django REST Framework (DRF) Serializer** sebagai engine validasi data di dalam **Django Views**.

---

## 🏗️ Architecture & Apps

Project terdiri dari 2 aplikasi utama:

### 1. `account`

* Login
* Logout
  (Menggunakan built-in Django Auth)

### 2. `product`

* Manajemen Produk
* Manajemen Kategori
* Manajemen Status

---

## 🗄️ Database Schema (Models)

### Category

| Field | Tipe      | Keterangan  |
| ----- | --------- | ----------- |
| id    | AutoField | Primary Key |
| name  | CharField | Unique      |

### Status

| Field | Tipe      | Keterangan  |
| ----- | --------- | ----------- |
| id    | AutoField | Primary Key |
| name  | CharField | Unique      |

### Product

| Field    | Tipe         | Keterangan                      |
| -------- | ------------ | ------------------------------- |
| name     | CharField    | Unique                          |
| price    | DecimalField | max_digits=10, decimal_places=2 |
| category | ForeignKey   | ke Category                     |
| status   | ForeignKey   | ke Status                       |

---

## 🛠️ Tech Highlights

* DRF Serializer digunakan untuk validasi data POST
* Error serializer ditampilkan lewat Django Messages
* Halaman list produk otomatis filter status **"bisa dijual"**

---

## 🚀 Instalasi & Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/lankok-id/BELAJAR_DJANGO
cd BELAJAR_DJANGO
```

### 2. Setup Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Jalankan Server

```bash
python manage.py runserver
```

Buka browser:

```
http://127.0.0.1:8000/product/
```

---

## 🔗 Endpoint List

### Product

| Method | Endpoint                | Deskripsi                         |
| ------ | ----------------------- | --------------------------------- |
| GET    | `/product/`             | List produk (status: bisa dijual) |
| POST   | `/product/create/`      | Tambah produk                     |
| POST   | `/product/<id>/update/` | Edit produk                       |
| POST   | `/product/<id>/delete/` | Hapus produk                      |

### Category

| Method     | Endpoint     | Deskripsi            |
| ---------- | ------------ | -------------------- |
| GET / POST | `/category/` | List & CRUD kategori |

### Status

| Method     | Endpoint   | Deskripsi          |
| ---------- | ---------- | ------------------ |
| GET / POST | `/status/` | List & CRUD status |

---

## 📌 Notes

* Gunakan Django `createsuperuser` untuk membuat akun admin
* Validasi sepenuhnya ditangani oleh DRF Serializer

---
