import asyncio

angka = [1, 2, 3, 4]


async def tugas_a():
    hasil = 0

    for n in angka:
        kuadrat = n * n
        print(f"Tugas A Kuadrat {n}*{n} = {kuadrat}")
        hasil += kuadrat

        # Memberikan kesempatan task lain berjalan
        await asyncio.sleep(0)

    return hasil


async def tugas_b():
    hasil = 0

    for n in angka:
        kubik = n * n * n
        print(f"Tugas B Kubik {n}*{n}*{n} = {kubik}")
        hasil += kubik

        # Memberikan kesempatan task lain berjalan
        await asyncio.sleep(0)

    return hasil


async def main():
    # Membuat kedua tugas sebagai task concurrent
    task_a = asyncio.create_task(tugas_a())
    task_b = asyncio.create_task(tugas_b())

    # Menunggu kedua task selesai
    hasil_a, hasil_b = await asyncio.gather(task_a, task_b)

    print("\n=== HASIL AKHIR ===")
    print(f"Hasil Tugas A kuadrat : {hasil_a}")
    print(f"Hasil Tugas B kubik   : {hasil_b}")


# Menjalankan event loop
asyncio.run(main()) 
