def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    # Menyimpan data valid
                    data.append((nim, nilai))

                except ValueError:
                    print(f"Baris {nomor_baris} tidak valid, dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:

        jumlah = len(data)

        if jumlah == 0:
            file.write("Tidak ada data valid untuk direkap.\n")
            return

        daftar_nilai = [nilai for nim, nilai in data]

        rata_rata = sum(daftar_nilai) / jumlah
        minimum = min(daftar_nilai)
        maksimum = max(daftar_nilai)

        lulus = sum(1 for nilai in daftar_nilai if nilai >= 60)

        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("==========================\n")
        file.write(f"Jumlah data valid : {jumlah}\n")
        file.write(f"Rata-rata nilai   : {rata_rata:.2f}\n")
        file.write(f"Nilai minimum     : {minimum}\n")
        file.write(f"Nilai maksimum    : {maksimum}\n")
        file.write(f"Jumlah lulus      : {lulus}\n")


# Alur utama program
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    tulis_rekap(output_file, data)
    print("\nRekap nilai berhasil dibuat.")
    print(f"Jumlah data valid: {len(data)}")
    print(f"Hasil disimpan di: {output_file}")