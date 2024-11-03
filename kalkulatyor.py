# Program Kalkulator Sederhana
print("=== Program Kalkulator Sederhana ===")
print("Operator yang tersedia:")
print("+ : Penjumlahan")
print("- : Pengurangan")
print("* : Perkalian")
print("/ : Pembagian")

try:
    # Input angka pertama
    angka1 = float(input("\nMasukkan angka pertama: "))
    
    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")
    
    # Input angka kedua
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Proses perhitungan menggunakan if elif else
    if operator == '+':
        hasil = angka1 + angka2
        operasi = "Penjumlahan"
    elif operator == '-':
        hasil = angka1 - angka2
        operasi = "Pengurangan"
    elif operator == '*':
        hasil = angka1 * angka2
        operasi = "Perkalian"
    elif operator == '/':
        if angka2 == 0:
            raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan!")
        hasil = angka1 / angka2
        operasi = "Pembagian"
    else:
        raise ValueError("Operator tidak valid!")
    
    # Tampilkan hasil
    print("\n=== Hasil Perhitungan ===")
    print(f"Operasi: {operasi}")
    print(f"{angka1} {operator} {angka2} = {hasil}")

except ValueError as e:
    if str(e) == "Operator tidak valid!":
        print("\nError: Operator yang dimasukkan tidak valid!")
    else:
        print("\nError: Mohon masukkan angka yang valid!")
except ZeroDivisionError as e:
    print(f"\nError: {e}")
except Exception as e:
    print(f"\nTerjadi kesalahan: {e}")