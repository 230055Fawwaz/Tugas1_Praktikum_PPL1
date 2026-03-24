# 📝 Todo API

RESTful API untuk manajemen tugas (To-Do) yang dibangun dengan Python Flask, Docker, dan GitHub Actions.

![CI](https://github.com/<username>/todo-api/actions/workflows/ci.yml/badge.svg)
![CS](https://github.com/<username>/todo-api/actions/workflows/cs.yml/badge.svg)

---

## 1. Deskripsi Project

API ini memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus tugas (CRUD). Dibangun menggunakan **Flask** sebagai framework, dikontainerisasi dengan **Docker**, dan dilengkapi pipeline **CI/CD** menggunakan GitHub Actions.

---

## 2. Dokumentasi API

### Base URL
```
http://localhost:5000
```

### Endpoint List

| Method | Endpoint        | Deskripsi              |
|--------|-----------------|------------------------|
| GET    | /health         | Cek status API         |
| GET    | /todos          | Ambil semua todo       |
| GET    | /todos/:id      | Ambil todo berdasarkan ID |
| POST   | /todos          | Buat todo baru         |
| PUT    | /todos/:id      | Update todo            |
| DELETE | /todos/:id      | Hapus todo             |

---

### Format Response

Semua response menggunakan format JSON standar berikut:

**✅ Success Response**
```json
{
  "status": "success",
  "message": "Todo created successfully",
  "data": {
    "id": 1,
    "title": "Belajar Docker",
    "description": "Pelajari Dockerfile dan docker-compose",
    "completed": false
  }
}
```

**❌ Error Response**
```json
{
  "status": "error",
  "message": "Todo with id 99 not found",
  "data": null
}
```

---

### Contoh Request & Response per Endpoint

#### GET /todos
```bash
curl http://localhost:5000/todos
```
```json
{
  "status": "success",
  "message": "Success",
  "data": [
    { "id": 1, "title": "Belajar Docker", "description": "", "completed": false }
  ]
}
```

#### POST /todos
```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Belajar Flask", "description": "Bikin API sederhana"}'
```
```json
{
  "status": "success",
  "message": "Todo created successfully",
  "data": { "id": 1, "title": "Belajar Flask", "description": "Bikin API sederhana", "completed": false }
}
```

**Error (title tidak ada):**
```json
{
  "status": "error",
  "message": "Field 'title' is required",
  "data": null
}
```

#### PUT /todos/1
```bash
curl -X PUT http://localhost:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```
```json
{
  "status": "success",
  "message": "Todo updated successfully",
  "data": { "id": 1, "title": "Belajar Flask", "description": "Bikin API sederhana", "completed": true }
}
```

#### DELETE /todos/1
```bash
curl -X DELETE http://localhost:5000/todos/1
```
```json
{
  "status": "success",
  "message": "Todo deleted successfully",
  "data": null
}
```

---

## 3. Panduan Instalasi (Docker)

### Prasyarat
- Docker & Docker Compose sudah terinstall

### Langkah Menjalankan

**1. Clone repository**
```bash
git clone https://github.com/<username>/todo-api.git
cd todo-api
```

**2. Jalankan dengan docker-compose**
```bash
docker-compose up --build
```

**3. Cek API berjalan**
```bash
curl http://localhost:5000/health
```

### Informasi Port

| Port Host | Port Container | Keterangan        |
|-----------|----------------|-------------------|
| 5000      | 5000           | Flask API         |

### Menghentikan Aplikasi
```bash
docker-compose down
```

---

## 4. Alur Kerja Git

### Branch yang Digunakan

| Branch         | Fungsi                                  |
|----------------|-----------------------------------------|
| `main`         | Branch produksi, selalu stabil          |
| `develop`      | Branch integrasi fitur                  |
| `feature/*`    | Branch pengembangan fitur baru          |

### Alur Branch
```
feature/add-login → develop → main
```

---

## 5. Status Automasi (GitHub Actions)

### Workflow yang Dibuat

**CI - Unit Testing** (`.github/workflows/ci.yml`)
- Berjalan otomatis saat `push` atau `pull_request` ke branch `main`, `develop`, atau `feature/**`
- Menginstall dependensi Python dan menjalankan `pytest`
- Memastikan semua unit test lulus sebelum merge

**CS - Security Scan** (`.github/workflows/cs.yml`)
- Berjalan otomatis saat `push` atau `pull_request`
- Menggunakan **Bandit** untuk scanning kerentanan keamanan pada kode Python
- Melaporkan issue keamanan tingkat medium ke atas

### Badge Status

Ganti `<username>` dengan username GitHub kamu:

```markdown
![CI](https://github.com/<username>/todo-api/actions/workflows/ci.yml/badge.svg)
![CS](https://github.com/<username>/todo-api/actions/workflows/cs.yml/badge.svg)
```
