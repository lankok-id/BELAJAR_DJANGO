# BELAJAR DJANGO

## CLASS

### product class

- [ ] - id (auto_increment)
- [ ] - name (unique)
- [ ] - price
- [ ] - category_id
- [ ] - status_id
- [ ] - created_at (auto_now_add)
- [ ] - updated_at (auto_now)

### category class

- [ ] - id (auto_increment)
- [ ] - name (unique)
- [ ] - created_at (auto_now_add)
- [ ] - updated_at (auto_now)

### status class

- [ ] - id (auto_increment)
- [ ] - name (unique)
- [ ] - created_at (auto_now_add)
- [ ] - updated_at (auto_now)

## url

### product url

| Action            | Method   | URL                     | Penjelasan                                           |
| :---------------- | :------- | :---------------------- | :--------------------------------------------------- |
| **List**          | `GET`    | `/product/`             | Menampilkan semua produk (opsional filter status)    |
| **Form Create**   | `GET`    | `/product/create/`      | Render form tambah produk (Django template)          |
| **Action Create** | `POST`   | `/product/create/`      | Menyimpan data produk baru ke database               |
| **Form Edit**     | `GET`    | `/product/<id>/update/` | Render form edit dengan data lama                    |
| **Action Update** | `POST`   | `/product/<id>/update/` | Memperbarui data produk (ditangani oleh view update) |
| **Action Delete** | `DELETE` | `/product/<id>/delete/` | Menghapus produk dari database (view delete)         |

### category url

| Action            | Method | URL                      | Penjelasan                          |
| :---------------- | :----- | :----------------------- | :---------------------------------- |
| **List**          | `GET`  | `/category/`             | Menampilkan semua daftar kategori   |
| **Form Create**   | `GET`  | `/category/create/`      | Render form tambah kategori baru    |
| **Action Create** | `POST` | `/category/create/`      | Menyimpan kategori baru ke database |
| **Form Edit**     | `GET`  | `/category/<id>/update/` | Render form untuk edit kategori     |
| **Action Update** | `POST` | `/category/<id>/update/` | Memperbarui nama kategori           |
| **Action Delete** | `POST` | `/category/<id>/delete/` | Menghapus kategori                  |

### status url

| Action            | Method | URL                    | Penjelasan                        |
| :---------------- | :----- | :--------------------- | :-------------------------------- |
| **List**          | `GET`  | `/status/`             | Menampilkan semua daftar status   |
| **Form Create**   | `GET`  | `/status/create/`      | Render form tambah status baru    |
| **Action Create** | `POST` | `/status/create/`      | Menyimpan status baru ke database |
| **Form Edit**     | `GET`  | `/status/<id>/update/` | Render form untuk edit status     |
| **Action Update** | `POST` | `/status/<id>/update/` | Memperbarui nama status           |
| **Action Delete** | `POST` | `/status/<id>/delete/` | Menghapus status                  |
