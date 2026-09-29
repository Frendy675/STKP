#sequential computing

import time

angka = [1, 2, 3, 4]

hasil = 0

print("=== SEQUENTIAL PROCESSING ===")
print("CPU Core = 1")
print()

for i in angka:

    # Menentukan tugas berdasarkan angka
    if i <= 2:
        tugas = "Tugas A"
    else:
        tugas = "Tugas B"

    print(f"CPU Core -> {tugas} -> angka {i}")

    # Operator
    hasil_proses = i * i

    time.sleep(1)

    print(f"{tugas} selesai -> {i} * {i} = {hasil_proses}")

    hasil += hasil_proses

print(f"Hasil = {hasil}")

