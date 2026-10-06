import time
import random
from multiprocessing import Pool, cpu_count


def tahap_sekuensial_load_data():
    time.sleep(0.5)
    data_nilai_angka = [random.randint(0, 100) for _ in range(100)]
    return data_nilai_angka


def konversi_ke_huruf(nilai_angka):
    if nilai_angka >= 85:
        nilai_huruf = 'A'
    elif nilai_angka >= 70:
        nilai_huruf = 'B'
    elif nilai_angka >= 55:
        nilai_huruf = 'C'
    elif nilai_angka >= 40:
        nilai_huruf = 'D'
    else:
        nilai_huruf = 'E'
    time.sleep(0.045)
    return (nilai_angka, nilai_huruf)


if __name__ == "__main__":
        # Sequential Computing
        t_seq_start = time.perf_counter()
        daftar_nilai = tahap_sekuensial_load_data()
        waktu_sekuensial = time.perf_counter() - t_seq_start
        print("Daftar nilai:", daftar_nilai)

        # Parallel Computing
        N = min(len(daftar_nilai), cpu_count())
        t_par_start = time.perf_counter()
        with Pool(processes=N) as pool:
                hasil_konversi = pool.map(konversi_ke_huruf, daftar_nilai)
        waktu_paralel = time.perf_counter() - t_par_start
        for i, (angka, huruf) in enumerate(hasil_konversi[:10], 1):
                print(f"Mahasiswa {i:2d}: Nilai Angka = {angka:3d} -> Nilai Huruf = {huruf}")

        total_waktu = waktu_sekuensial + waktu_paralel
        print(f"Waktu Sekuensial : {waktu_sekuensial:.3f} detik")
        print(f"Waktu Paralel : {waktu_paralel:.3f} detik")
        print(f"Total Waktu Eksekusi : {total_waktu:.3f} detik")