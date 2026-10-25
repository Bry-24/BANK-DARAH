

from pathlib import Path


def baca_data():
    lokasi_file = Path(__file__).with_name("input_contoh.txt")

    with open(lokasi_file, "r", encoding="utf-8") as file:
        n = int(file.readline())
        m = int(file.readline())

        data_donor = []

        for _ in range(n):
            desa, golongan, volume = map(
                int, file.readline().split()
            )
            data_donor.append((desa, golongan, volume))

    return n, m, data_donor
