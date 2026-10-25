
from pathlib import Path


def pilih_desa_dari_file(kode_golongan, kebutuhan):
    lokasi_file = Path(__file__).with_name("input_contoh.txt")

    with open(lokasi_file, "r", encoding="utf-8") as file:
        n = int(file.readline().strip())
        m = int(file.readline().strip())

        volume_desa = [0] * (m + 1)

        for _ in range(n):
            desa, golongan, volume = map(
                int, file.readline().split()
            )

            if golongan == kode_golongan:
                volume_desa[desa] += volume

    daftar_desa = [
        (volume_desa[desa], desa)
        for desa in range(1, m + 1)
        if volume_desa[desa] > 0
    ]

    daftar_desa.sort(reverse=True)

    desa_terpilih = []
    total_volume = 0

    for volume, desa in daftar_desa:
        if total_volume >= kebutuhan:
            break

        desa_terpilih.append((desa, volume))
        total_volume += volume

    return desa_terpilih, total_volume



def pilih_desa_cepat(m, data_donor, kode_golongan, kebutuhan):
    volume_desa = [0] * (m + 1)

    for desa, golongan, volume in data_donor:
        if golongan == kode_golongan:
            volume_desa[desa] += volume

    # Simpan desa yang memiliki stok positif.
    daftar_desa = [
        (volume_desa[desa], desa)
        for desa in range(1, m + 1)
        if volume_desa[desa] > 0
    ]

    # Stok terbesar terlebih dahulu.
    daftar_desa.sort(reverse=True)

    desa_terpilih = []
    total_volume = 0

    for volume, desa in daftar_desa:
        if total_volume >= kebutuhan:
            break

        desa_terpilih.append((desa, volume))
        total_volume += volume

    return desa_terpilih, total_volume
