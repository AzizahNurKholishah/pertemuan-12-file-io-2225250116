# Pertemuan 12 - File I/O dan Error Handling

| Identitas | Keterangan |
|---|---|
| Nama | Azizah Nur Kholishah |
| NIM | 2225250116 |
| Kelas | 3-E |

## Tujuan

Mempelajari cara membaca, menulis, dan mengolah data dari file menggunakan Python. Selain itu, memahami cara memvalidasi data dan menangani error agar program tetap berjalan dengan baik.

## Format File Input

Data nilai disimpan dalam file `nilai.txt` dengan format NIM dan nilai yang dipisahkan menggunakan tanda koma.

```text
NIM,nilai
A001,85
A002,78
A003,92
```

## Cara Menjalankan

Jalankan program melalui terminal VS Code dari folder utama proyek dengan perintah:

```bash
python tugas/rekap_nilai_file.py
```

Program akan membaca data dari `data/nilai.txt`, menghitung rekap nilai, kemudian menyimpan hasilnya ke `data/hasil_rekap.txt`.

## Error yang Ditangani

- **FileNotFoundError:** Menangani kondisi ketika file input tidak ditemukan.
- **ValueError:** Menangani nilai yang tidak dapat diubah menjadi angka, sehingga baris yang tidak valid dapat dilewati tanpa menghentikan seluruh proses.

## Test Case

| No. | Kondisi Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Semua data valid | Semua data diproses dan rekap dihitung dengan benar | 3 data berhasil diproses, rata-rata 85, nilai minimum 78, dan maksimum 92 | Berhasil |
| 2 | File tidak ditemukan | Muncul pesan file tidak ditemukan dan program tidak crash | Program menampilkan pesan bahwa file tidak ditemukan | Berhasil |
| 3 | Nilai invalid (`A004,abc`) | Baris invalid dilewati dan data lainnya tetap diproses | Baris A004 dilewati, sedangkan 5 data lainnya berhasil diproses | Berhasil |
| 4 | Terdapat baris kosong | Baris kosong dilewati | Baris kosong dilewati dan 3 data lainnya tetap diproses | Berhasil |
| 5 | Terdapat nilai 60 | Nilai 60 dihitung sebagai lulus | Nilai 60 berhasil dihitung sebagai lulus karena memenuhi batas minimal kelulusan | Berhasil |

## Refleksi 

Pada tuas ini, saya mempelajari cara membaca dan mengolah data dari file menggunakan Python. Salah satu error yang ditemukan adalah `ValueError`, yaitu ketika program membaca nilai yang bukan berupa angka, seperti `abc`. Error tersebut ditangani menggunakan `try-except`, sehingga baris yang tidak valid dapat dilewati dan data lainnya tetap diproses. Dari praktikum ini, saya memahami pentingnya validasi data dan penanganan error agar program dapat berjalan dengan lebih baik.

## Exit Ticket

- **Perbedaan paling penting antara mode w dan a adalah** mode w digunakan untuk menulis file dengan mengganti isi sebelumnya, sedangkan mode a digunakan untuk menambahkan isi baru di akhir file tanpa menghapus isi yang sudah ada.
- **Error file yang paling perlu saya antisipasi adalah** FileNotFoundError, karena error ini terjadi ketika file yang ingin dibaca tidak ditemukan atau lokasi file tidak sesuai.
- **Alasan saya menggunakan with adalah** agar file tertutup secara otomatis setelah selesai digunakan, sehingga pengelolaan file menjadi lebih aman dan praktis.
- **Konsep Pertemuan 12 yang akan membantu debugging pada Pertemuan 13 adalah** penggunaan try-except untuk menangani error dan validasi data agar kesalahan dapat diketahui dan tidak langsung menghentikan program.

## Bantuan AI

Saya juga menggunakan AI sebagai panduan dalam menyusun kode, melakukan pengujian, dan membuat dokumentasi README. Seluruh kode tetap saya pelajari dan jalankan kembali di VS Code agar memahami cara kerja program.