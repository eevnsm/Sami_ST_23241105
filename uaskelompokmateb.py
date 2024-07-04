# Meminta input dari pengguna
n = int(input("Masukkan angka maksimum: "))

# Inisialisasi variabel untuk menghitung jumlah angka genap
jumlah_genap = 0

# Pengulangan dari 1 sampai n
for i in range(1, n+1):
    # Percabangan untuk memeriksa apakah angka genap
    if i % 2 == 0:
        jumlah_genap += 1

# Menampilkan hasil
print(f"Jumlah angka genap dari 1 sampai {n} adalah: {jumlah_genap}")
