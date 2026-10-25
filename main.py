
from data import baca_data
from subproblem1 import hitung_pendonor, tampilkan_hasil
from subproblem2 import hitung_stok, tampilkan_stok
from subproblem3 import (
    pilih_desa,
    tampilkan_hasil as tampilkan_hasil_subproblem3
)
from subproblem4 import pilih_desa_dari_file

def main():
    _, m, data_donor = baca_data()

    print("Pilih subproblem:")
    print("1. Jumlah pendonor per desa")
    print("2. Jumlah pendonor dan volume darah")
    print("3. Pemenuhan kebutuhan darah")
    print("4. Pemenuhan kebutuhan darah (optimasi)")

    pilihan = input("Pilihan (1/2/3/4): ")

    if pilihan == "1":
        jumlah = hitung_pendonor(m, data_donor)
        tampilkan_hasil(jumlah, m)

    elif pilihan == "2":
        jumlah, volume = hitung_stok(m, data_donor)
        tampilkan_stok(jumlah, volume, m)

    
    elif pilihan == "3":
        kode_golongan = int(
            input("Kode golongan darah (1=A, 2=B, 3=AB, 4=O): ")
        )
        kebutuhan = int(input("Volume kebutuhan (ml): "))

        if kode_golongan not in (1, 2, 3, 4) or kebutuhan < 0:
            print("Input tidak valid.")
        else:
            desa_terpilih, total_volume = pilih_desa(
                m, data_donor, kode_golongan, kebutuhan
            )
            tampilkan_hasil_subproblem3(
                desa_terpilih, total_volume, kebutuhan
            )

    elif pilihan == "4":
        kode_golongan = int(
            input("Kode golongan darah (1=A, 2=B, 3=AB, 4=O): ")
        )
        kebutuhan = int(input("Volume kebutuhan (ml): "))

        if kode_golongan not in (1, 2, 3, 4) or kebutuhan < 0:
            print("Input tidak valid.")
        else:
            desa_terpilih, total_volume = pilih_desa_dari_file(
                kode_golongan, kebutuhan
            )
            tampilkan_hasil_subproblem3(
                desa_terpilih, total_volume, kebutuhan
            )

    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
