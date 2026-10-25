
from pathlib import Path
import random
import time

from subproblem4 import pilih_desa_dari_file

N =  1_000_000
M = 10_000
INPUT_FILE = Path(__file__).with_name("input.txt")


def buat_data_uji():
    random.seed(42)

    with INPUT_FILE.open(
        "w", encoding="utf-8", buffering=1024 * 1024
    ) as file:
        file.write(f"{N}\n{M}\n")

        for _ in range(N):
            desa = random.randint(1, M)
            golongan = random.randint(1, 4)
            volume = random.randint(100, 500)
            file.write(f"{desa} {golongan} {volume}\n")


def main():
    print(f"Membuat {N:,} data DDS...")
    buat_data_uji()

    print("Mulai pengujian...")
    mulai = time.perf_counter()

    hasil, total = pilih_desa_dari_file(1, 100_000)

    durasi = time.perf_counter() - mulai

    print("\n--- HASIL BENCHMARK ---")
    print(f"Jumlah DDS    : {N:,}")
    print(f"Jumlah desa   : {M:,}")
    print(f"Waktu proses  : {durasi:.3f} detik")
    print(f"Desa terpilih : {len(hasil)}")
    print(f"Total volume  : {total} ml")
    print(
        f"Ukuran input  : "
        f"{INPUT_FILE.stat().st_size / (1024 * 1024):.2f} MiB"
    )


if __name__ == "__main__":
    main()
