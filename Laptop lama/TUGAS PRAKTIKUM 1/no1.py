# Program Saham

print("## Program Saham ##")
print("===================")
print()

saham = int(input("Masukkan Harga Saham Kemarin : "))
saham_hari_ini = 105
persentase = (saham_hari_ini - saham)/saham * 100

Beli = (persentase > 5) * 1
Tahan = (-3 <= persentase < 5) * 1
Jual = (persentase <= -3) * 1

nilai_true = Beli * "Beli" + Tahan * "Tahan" + Jual * "Jual"

print(f"Persentase = {persentase:.2f}%")
print(f"Rekomendasi Investasi: {nilai_true}")