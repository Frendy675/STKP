import time
import random
from multiprocessing import Pool
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