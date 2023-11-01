# Meminta pengguna memasukkan 3 bilangan
bilangan1 = float(input("Masukkan bilangan ke-1: "))
bilangan2 = float(input("Masukkan bilangan ke-2: "))
bilangan3 = float(input("Masukkan bilangan ke-3: "))


if bilangan1 <= bilangan2 <= bilangan3:
    urutan_bilangan = (bilangan1, bilangan2, bilangan3)
elif bilangan1 <= bilangan3 <= bilangan2:
    urutan_bilangan = (bilangan1, bilangan3, bilangan2)
elif bilangan2 <= bilangan1 <= bilangan3:
    urutan_bilangan = (bilangan2, bilangan1, bilangan3)
elif bilangan2 <= bilangan3 <= bilangan1:
    urutan_bilangan = (bilangan2, bilangan3, bilangan1)
elif bilangan3 <= bilangan1 <= bilangan2:
    urutan_bilangan = (bilangan3, bilangan1, bilangan2)
else:
    urutan_bilangan = (bilangan3, bilangan2, bilangan1)


print("Urutan bilangan:", urutan_bilangan)
