# list_vs_tuple.py

# ====================================================================
# 1. Definisi List dan Tuple
# ====================================================================

# List (Mutable - Bisa diubah)
daftar_belanja_list = ["Apel", "Susu", "Roti"]
print(f"List Awal: {daftar_belanja_list}")

# Tuple (Immutable - Tidak bisa diubah)
koordinat_tuple = (10, 20)
print(f"Tuple Awal: {koordinat_tuple}")

print("-" * 50)

# ====================================================================
# 2. Demonstrasi Mutability (List)
# ====================================================================

print(">>> List: Mencoba mengubah elemen...")
try:
    # Mengubah elemen ke-2 (indeks 1) dari "Susu" menjadi "Telur"
    daftar_belanja_list[1] = "Telur"
    print(f"List Setelah Perubahan: {daftar_belanja_list}")
    print("HASIL: List berhasil diubah (Mutable).")
except TypeError as e:
    print(f"List GAGAL diubah: {e}")

print("-" * 50)

# ====================================================================
# 3. Demonstrasi Immutability (Tuple)
# ====================================================================

print(">>> Tuple: Mencoba mengubah elemen...")
try:
    # Mencoba mengubah elemen ke-2 (indeks 1) dari 20 menjadi 30
    koordinat_tuple[1] = 30
    print(f"Tuple Setelah Perubahan: {koordinat_tuple}")
except TypeError as e:
    print(f"Tuple GAGAL diubah: {e}")
    print("HASIL: Tuple tidak bisa diubah (Immutable).")

print("-" * 50)

# ====================================================================
# 4. Demonstrasi Operasi Lain
# ====================================================================

# List: Menambah elemen baru (berhasil)
daftar_belanja_list.append("Keju")
print(f"List Setelah Append: {daftar_belanja_list}")

# Tuple: Mencoba menambah elemen baru (akan error)
print(">>> Tuple: Mencoba menambah elemen baru (append)...")
try:
    koordinat_tuple.append(40)
except AttributeError as e:
    print(f"Tuple GAGAL Append: {e}")
    print("HASIL: Tuple tidak memiliki metode 'append' karena sifatnya Immutable.")
