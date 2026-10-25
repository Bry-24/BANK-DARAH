
NAMA_GOLONGAN = {
    1: "A",
    2: "B",
    3: "AB",
    4: "O"
}


def pilih_desa(m, data_donor, kode_golongan, kebutuhan):
    volume_desa = [0] * (m + 1)

    for desa, golongan, volume in data_donor:
        if golongan == kode_golongan:
            volume_desa[desa] += volume

    # Urutkan desa dari stok terbesar ke terkecil.
    daftar_desa = []

    for desa in range(1, m + 1):
        if volume_desa[desa] > 0:
            daftar_desa.append((desa, volume_desa[desa]))

    daftar_desa.sort(key=lambda item: (-item[1], item[0]))

    desa_terpilih = []
    total_volume = 0

    for desa, volume in daftar_desa:
        if total_volume >= kebutuhan:
            break

        desa_terpilih.append((desa, volume))
        total_volume += volume

    return desa_terpilih, total_volume


def tampilkan_hasil(desa_terpilih, total_volume, kebutuhan):
    print("\nHasil pemilihan desa:")

    if not desa_terpilih:
        print("Tidak ada desa yang perlu dipilih.")
    else:
        for desa, volume in desa_terpilih:
            print(f"Desa {desa}: {volume} ml")

    if total_volume >= kebutuhan:
        surplus = total_volume - kebutuhan
        print(
            f"Kebutuhan darah dipenuhi dengan surplus "
            f"{surplus} ml"
        )
    else:
        kurang = kebutuhan - total_volume
        print(
            f"Kebutuhan darah masih kurang "
            f"{kurang} ml"
        )
