import multiprocessing
import os
import time


def tugas_a(event_a, event_b, hasil):
    print(f"[Core 1] PID {os.getpid()}")

    # Tugas A pertama
    nilai_1 = 1 * 1
    print(f"Tugas A: 1 * 1 = {nilai_1}")

    hasil.put(nilai_1)

    # Memberi sinyal bahwa A(1) sudah selesai
    event_a.set()

    # Menunggu Tugas B(3) selesai
    event_b.wait()

    # Tugas A kedua
    nilai_2 = 2 * 2
    print(f"Tugas A: 2 * 2 = {nilai_2}")

    hasil.put(nilai_2)


def tugas_b(event_a, event_b, hasil):
    print(f"[Core 2] PID {os.getpid()}")

    # Menunggu Tugas A(1) selesai
    event_a.wait()

    # Tugas B pertama
    nilai_1 = 3 * 3
    print(f"Tugas B: 3 * 3 = {nilai_1}")

    hasil.put(nilai_1)

    # Memberi sinyal bahwa B(3) sudah selesai
    event_b.set()

    # Tugas B kedua menunggu A(2)
    # Delay kecil hanya untuk memperlihatkan urutan
    time.sleep(0.01)

    nilai_2 = 4 * 4
    print(f"Tugas B: 4 * 4 = {nilai_2}")

    hasil.put(nilai_2)


if __name__ == "__main__":

    # Queue untuk mengirim hasil dari process
    hasil = multiprocessing.Queue()

    # Event untuk sinkronisasi antar-process
    event_a = multiprocessing.Event()
    event_b = multiprocessing.Event()

    # Process Core 1
    proses_a = multiprocessing.Process(
        target=tugas_a,
        args=(event_a, event_b, hasil)
    )

    # Process Core 2
    proses_b = multiprocessing.Process(
        target=tugas_b,
        args=(event_a, event_b, hasil)
    )

    # Menjalankan kedua process secara concurrent
    proses_a.start()
    proses_b.start()

    # Menunggu kedua process selesai
    proses_a.join()
    proses_b.join()

    # Mengambil seluruh hasil
    total = 0

    while not hasil.empty():
        total += hasil.get()

    print("\n======================")
    print("HASIL AKHIR")
    print("======================")
    print(f"Hasil = {total}")
