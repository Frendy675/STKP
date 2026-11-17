#concurrent-single-core-asyncio

import asyncio

# Data
angka = [1, 2, 3, 4]


async def tugas_A(data):
    hasil = 0

    for angka in data:
        print(f"Tugas A {angka}*{angka} = {angka * angka}")

        hasil += angka * angka

        # Memberikan kesempatan kepada task lain
        await asyncio.sleep(0)

    return hasil


async def tugas_B(data):
    hasil = 0

    for angka in data:
        print(f"Tugas B {angka}*{angka} = {angka * angka}")

        hasil += angka * angka

        # Memberikan kesempatan kepada task lain
        await asyncio.sleep(0)

    return hasil


async def main():

    # Memisahkan data untuk Tugas A dan Tugas B
    data_A = angka[0:2]
    data_B = angka[2:4]

    # Membuat concurrent task
    task_A = asyncio.create_task(tugas_A(data_A))
    task_B = asyncio.create_task(tugas_B(data_B))

    # Menunggu kedua task selesai
    hasil_A, hasil_B = await asyncio.gather(
        task_A,
        task_B
    )

    # Menggabungkan hasil
    hasil = hasil_A + hasil_B

    print(f"Hasil = {hasil}")


# Menjalankan program
asyncio.run(main())
