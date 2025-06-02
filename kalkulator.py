# Program Lengkap: Cek Kabisat dan Hitung Hari dengan Loop
def is_kabisat(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def jumlah_hari_dalam_bulan(bulan, tahun):
    if bulan == 2:
        return 29 if is_kabisat(tahun) else 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def masukan_angka(pesan, min_val=None, max_val=None):
    while True:
        try:
            angka = int(input(pesan))
            if min_val is not None and angka < min_val:
                print(f"Nilai minimal {min_val}.")
            elif max_val is not None and angka > max_val:
                print(f"Nilai maksimal {max_val}.")
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka.")

def validasi_input():
    tanggal = masukan_angka("Masukkan tanggal (1-31): ", 1, 31)
    bulan = masukan_angka("Masukkan bulan (1-12): ", 1, 12)
    tahun = masukan_angka("Masukkan tahun (positif): ", 1)

    max_hari = jumlah_hari_dalam_bulan(bulan, tahun)
    while tanggal > max_hari:
        print(f"Tanggal tidak valid! Bulan {bulan} tahun {tahun} hanya sampai {max_hari}.")
        tanggal = masukan_angka(f"Masukkan tanggal (1-{max_hari}): ", 1, max_hari)
    return tanggal, bulan, tahun

def zeller_congruence(tanggal, bulan, tahun):
    if bulan < 3:
        bulan += 12
        tahun -= 1
    k = tahun % 100
    j = tahun // 100
    h = (tanggal + (13 * (bulan + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return h

# Main program
if __name__ == "__main__":
    tanggal, bulan, tahun = validasi_input()
    hari = zeller_congruence(tanggal, bulan, tahun)
    hari_nama = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    print(f"Hari pada tanggal {tanggal}/{bulan}/{tahun} adalah {hari_nama[hari]}.")
    if is_kabisat(tahun):
        print(f"{tahun} adalah tahun kabisat.")
    else:
        print(f"{tahun} bukan tahun kabisat.")
    print(f"Input Valid : {tanggal}/{bulan}/{tahun}")
    





        