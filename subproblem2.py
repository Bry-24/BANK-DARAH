
NAMA_GOLONGAN = {
    1: "A",
    2: "B",
    3: "AB",
    4: "O",
}

def hitung_stok(m, data_donor):
   jumlah = [[0] * 5 for _ in range(m + 1)]
   volume = [[0] * 5 for _ in range(m + 1)]

   for desa, golongan, ml in data_donor:
      jumlah[desa][golongan] += 1
      volume[desa][golongan] += ml

   return jumlah, volume

def tampilkan_stok(jumlah, volume, m):
    for desa in range (1, m + 1):
        print(f"Desa {desa}:")

        for kode in range(1, 5):
           NAMA = NAMA_GOLONGAN[kode]
           jml = jumlah[desa][kode]
           vol = volume[desa][kode]

           print(f"Golongan {NAMA}: {jml} pendonor, {vol} ml")
           