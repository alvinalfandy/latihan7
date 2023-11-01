modal_awal = 100_000_000  # Modal awal sebesar 100 juta
labas = []  # Daftar laba bulanan

# Loop dari bulan 1 hingga bulan 12
for bulan in range(1, 13):
    if bulan <= 2:
        laba = 0  # Bulan pertama dan kedua belum mendapatkan laba
    elif bulan == 3:
        laba = modal_awal * 0.01  # Bulan ketiga mendapatkan laba 1%
    elif bulan == 5:
        laba = modal_awal * 0.06  # Bulan kelima mendapatkan laba 5%
    elif bulan == 8:
        laba = modal_awal * 0.06 * 0.98  # Bulan kedelapan mengalami penurunan 2%
    else:
        laba = labas[bulan - 2]  # Laba bulan sebelumnya

    labas.append(laba)

# Print hasil laba bulanan
for bulan, laba in enumerate(labas, start=1):
    print(f"Bulan {bulan}: Laba {laba:.2f}")
