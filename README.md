# TASK-REPOSITORY Cek Kabisat dan Hitung Hari


Program ini berfungsi untuk memvalidasi tanggal, menentukan apakah suatu tahun merupakan tahun kabisat , menghitung jumlah hari dalam bulan tertentu, serta menentukan nama hari dari sebuah tanggal menggunakan algoritma Zeller’s Congruence.
```
🔧 Fitur Utama:
    - Memvalidasi input tanggal, bulan, dan tahun.
    - Mengecek apakah suatu tahun adalah tahun kabisat.
    - Menghitung jumlah hari dalam bulan tertentu.
    - Menentukan nama hari dari tanggal yang dimasukkan.
    - Output akhir berupa informasi lengkap tentang:
        + Nama hari dari tanggal tersebut.
        + Apakah tahun tersebut kabisat.
        + Tanggal valid yang diinputkan.
```
## Alur Logika Program sebagai berikut: 
```
1. Fungsi is_kabisat(tahun) 
    Menentukan apakah suatu tahun merupakan tahun kabisat :
        - Jika tahun habis dibagi 4,
        - Dan tidak habis dibagi 100 , kecuali juga habis dibagi 400 → maka kabisat.
        Contoh:
            2020 → ✅ kabisat,
            1900 → ❌ bukan kabisat,
            2000 → ✅ kabisat
```
  ![image](https://github.com/user-attachments/assets/3630288e-4673-468d-9d91-7e68b7b67845)

```   
2. Fungsi jumlah_hari_dalam_bulan(bulan, tahun)
Mengembalikan jumlah hari dalam bulan tertentu:
    - Bulan Februari (2): 28 atau 29 hari tergantung hasil is_kabisat(),
    - Bulan April, Juni, September, November (4,6,9,11): 30 hari,
    - Bulan lainnya: 31 hari
```
   ![image](https://github.com/user-attachments/assets/527a324e-4968-4327-91ef-d8f1b94ee391)
```
3. Fungsi masukan_angka(pesan, min_val=None, max_val=None)
Meminta pengguna memasukkan angka dengan validasi:
    - Harus berupa angka (int),
    - Diantara rentang nilai yang diperbolehkan (min_val hingga max_val),
```
   ![image](https://github.com/user-attachments/assets/4ef1cc3e-a679-46ba-a0bf-5f2f06e0c211)
```
4. Fungsi validasi_input()
Menerima input tanggal, bulan, dan tahun dari pengguna, lalu memastikan bahwa:
    - Tanggal tidak melebihi jumlah hari dalam bulan dan tahun tertentu.
    - Jika melebihi akan diminta ulang sampai valid.
```
   ![image](https://github.com/user-attachments/assets/39db860e-ad1b-42fd-b1e4-0a93969e7bac)

```
5. Fungsi zeller_congruence(tanggal, bulan, tahun)
Menggunakan algoritma Zeller's Congruence untuk menentukan nama hari dari sebuah tanggal:
    - Jika bulan Januari/Februari (1/2), dihitung sebagai bulan 13 dan 14 dari tahun sebelumnya.,
    - Rumus matematis digunakan untuk menghitung indeks hari (0–6).,
    Hasil dimapping ke array nama hari sesuai urutan:
        hari_nama = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
```
   ![image](https://github.com/user-attachments/assets/cd80cf04-29e5-40c8-80a7-972614ff40b9)
```
Contoh ketika program dijalankan:
```
![image](https://github.com/user-attachments/assets/512b6201-23ab-4296-b1e7-8d18322319c2)

```

