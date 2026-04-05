print("=== KALKULATOR SEDERHANA ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("1. +")
print("2. -")
print("3. *")
print("4. /")

pilihan = input("Pilih operasi: ")

if pilihan == "1":
    print(f"{angka1} + {angka2} = {angka1 + angka2}")
elif pilihan == "2":
    print(f"{angka1} - {angka2} = {angka1 - angka2}")
elif pilihan == "3":
    print(f"{angka1} * {angka2} = {angka1 * angka2}")
elif pilihan == "4":
    if angka2 != 0:
        print(f"{angka1} / {angka2} = {angka1 / angka2}")
    else:
        print("Tidak bisa dibagi nol!")
else:
    print("Pilihan salah!")
