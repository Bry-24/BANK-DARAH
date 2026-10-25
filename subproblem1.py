
def hitung_pendonor(m, data_donor):
    jumlah = [0] * (m + 1)

    for desa, golongan, volume in data_donor:
        jumlah[desa] += 1

    return jumlah


def tampilkan_hasil(jumlah, m):
    for desa in range(1, m + 1):
        print(f"Desa {desa}: {jumlah[desa]}")
