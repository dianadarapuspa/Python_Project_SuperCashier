# Python_Project_SuperCashier

## Latar Belakang
Super Cashier adalah sebuah program yang dibuat untuk membantu operasi perhitungan belanja customer di supermarket. 
Customer dapat langsung memasukkan item yang ingin dibeli, mengubah item, menghapus item, maupun membatalkan transaksi.

## Objektif
Tujuan dari dibuatnya program Super Cashier untuk memudahkan pross perhitungan total belanja customer.
Program Super Cashier dibuat dengan alur sebagai berikut:
  1. Customer membuat ID Transaksi
  2. Customer memasukkan nama item, jumlah item, dan harga item dengan fungsi **add_item**
  3. Jika terdapat data dari daftar belanja yang ingin diubah, Customer dapat melakuan perubahan sebagai berikut:
     - Mengubah nama barang dengan fungsi **update_item_name**
     - Mengubah jumlah barang dengan fungsi  **update_item_qty**
     - Mengubah harga barang dengan fungsi **update_item_price**  
  4. Jika Customer sudah selesai berbelanja, Customer dapat menghapus item dengan fungsi **delete_item** atau membatalkan transaksi dengan fungsi **reset_transaction**
  5. Jika Customer masih ingin melakukan penambahan item barang, dapat kembali ke fungsi **add_item**
  6. Jika Customer sudah memasukkan semua item yang diinginkan, maka daftar belanja dapat diperiksa dengan metode **check_item**
  7. JIka hasil input daftar belanja sudah benar maka akan dilanjutkan ke metode menghitung **total_price**. Jika data daftar belanja belum benar, maka akan kembali ke metode update item yang sudah disebutkan di point 3
     - Untuk total belanja > Rp. 500,000 akan mendapat diskon sebesar 10$
     - Untuk total belanja > Rp. 300,000 akan mendapat diskon sebesar 8$
     - Untuk total belanja > Rp. 200,000 akan mendapat diskon sebesar 5$
  8. JIka sudah benar, maka program akan menampilkan total belanja dan diskon yang didapatkan (jika ada).

## Flow Chart atau Alur Kode
![Super Cashier - diagram dark](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/a509d41e-80a9-4e39-909b-9173f5f41577)

## Penjelasan Fungsi
Untuk fungsi terdapat di dalam script cashier_modul.py. Modul tersebut berisi fungsi-fungsi sebagai berikut:
1. **def__init__(self)**\
     Fungsi ini merupakan fungsi untuk meinisialisasi objek yang akan menjadi atribut dari suatu fungsi yang datanya akan disimpan dalam bentuk dictionary
2. **def add_item(self, name, qty, price)**\
     Fungsi ini merupakan fungsi untuk menambahkan item dalam daftar belanja. Dengan menginput nama barang, jumlah barang, dan harga barang
3. **def update_item_name(self, name, new_name)**\
     Fungsi ini merupakan fungsi untuk melakukan update nama item
4. **def update_item_qty(self, name, new_qty)**\
     Fungsi ini merupakan fungsi untuk melakukan update jumlah item
5. **def update_item_price(self, name, new_price)**\
     Fungsi ini merupakan fungsi untuk melakukan update harga item
6. **def delete_item(self, name)**\
     Fungsi ini merupakan fungsi untuk menghapus item dari daftar belanja
7. **def reset_transaction(self)**\
     Fungsi ini merupakan fungsi untuk membatalkan transaksi yang telah dibuat
8. **def print_order(self)**\
     Fungsi ini merupakan fungsi yang digunakan untuk mencetak daftar belanja
9. **def check_order(self)**\
     Fungsi ini merupakan fungsi yang digunakan untuk memeriksa daftar belanja apakah sudah benar nilainya
10. **def total_price(self)**
     Fungsi ini merupakan fungsi yang digunakan untuk menghitung total belanja dan diskon yang didapatkan customer (jika ada)

## Test Case 
### 1. Customer input Transaction ID
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/8de778e1-a798-4648-b43e-4ebe5f7dc118)

### 2. Add Item dengan fungsi **add_item**
Pada uji coba program kita akan memasukkan 3 item barang yaitu Sabun, Shampoo, dan Sikat
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/2aaabe69-8c5e-49c1-86f6-46b64d4859a9)

### 3. Update Nama Item dengan fungsi **update_item_name**
Pada contoh kali ini kita mengubah nama item dari "Sabun" menjadi "Soap"
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/ccbb02ef-b1ec-4300-95ef-074454465b65)

### 4. Update Jumlah Item dengan fungsi **update_item_qty**
Pada contoh kali ini kita mengubah jumlah item shampoo dari 4 item menjadi 5 item
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/57e230c5-37ac-4cb2-b5ea-374b3688d956)

### 5. Update Harga Item dengan fungsi **update_item_price**
Pada contoh kali ini kita mengubah harga shampoo dari Rp. 65,000 menjadi Rp. 45,000
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/a0f5d66c-329a-4ef3-a870-a0ac2b99c414)

### 6. Menghapus item dari daftar belanja dengan fungsi **delete_item**
Pada contoh kali ini kita akan menghapus item sikat\
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/db600ea2-5c10-4226-a14f-7873ac7d7bf7)

### 7. Membatalkan transaksi yang sudah berjalan dengan fungsi **reset_transaction**
Pada contoh kali ini kita akan membatalkan transaksi yang sudah diproses.\
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/dd84d3fb-234f-4042-93e8-35715612278a)

### 8. Mencetak daftar belanja yang sudah diinput menggunakan fungsi **print_order**
Untuk mencoba fungsi berikut, kita akan menginput ulang hasil dari test-case  point 1-6 dan melewati test-case point 7. Sehingga item yang tersisa merupakan Soap dan Shampoo.
Cetakan daftar belanja merupakan dalam bentuk tabel\
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/20276774-e5f6-45b9-b6f1-7131cab821cd)

### 9. Memeriksa kebenaran nilai yang diinput ke daftar belanja dengan fungsi **check_order** dan Menghitung total belanja dengan fungsi **total_price**
Jika nilai dari data yang diinput sudah benar, maka akan menampilkan data dalam bentuk seperti print_order dan akan tertulis "Pemesanan sudah benar"\
![image](https://github.com/dianadarapuspa/Python_Project_SuperCashier/assets/138368022/adaba6a3-6b72-42dc-a9b3-f1dc0e79b0b9)

## Kesimpulan
Program super cashier sudah dapat digunakan dengan baik

  
