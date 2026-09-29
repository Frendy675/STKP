from multiprocessing import Process, Queue


def tugas_a(queue):
    print("=== CORE 1 ===")

    hasil = 0

    for angka in [1, 2]:
        nilai = angka * angka

        print(
            f"Tugas A {angka}*{angka} = {nilai} | Core 1"
        )

        hasil += nilai

    queue.put(hasil)


def tugas_b(queue):
    print("=== CORE 2 ===")

    hasil = 0

    for angka in [3, 4]:
        nilai = angka * angka

        print(
            f"Tugas B {angka}*{angka} = {nilai} | Core 2"
        )

        hasil += nilai

    queue.put(hasil)


if __name__ == "__main__":

    queue = Queue()

    # Membuat 2 proses
    proses_a = Process(
        target=tugas_a,
        args=(queue,)
    )

    proses_b = Process(
        target=tugas_b,
        args=(queue,)
    )

    # Menjalankan secara concurrent
    proses_a.start()
    proses_b.start()

    # Menunggu kedua proses selesai
    proses_a.join()
    proses_b.join()

    # Mengambil hasil
    hasil_a = queue.get()
    hasil_b = queue.get()

    total = hasil_a + hasil_b

    print("\n=== HASIL AKHIR ===")
    print(f"Hasil Tugas A = {hasil_a}")
    print(f"Hasil Tugas B = {hasil_b}")
    print(f"Hasil = {total}")
