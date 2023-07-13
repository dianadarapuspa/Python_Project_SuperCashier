
import pandas as pd
from tabulate import tabulate
import cashier_modul as c

transaksi = c.Transaction()

id_transaksi = int(input("Masukkan nomor ID anda: "))
message = f"Welcome to Super Cashier {id_transaksi}"
print("*"* len(message))
print(message)
print("*"* len(message))

confirm1 = input("Apakah Anda akan berbelanja? y/n: ")
while confirm1 == "y":
    print('\nKetik 1 untuk add item. \nKetik 2 untuk ubah item. \nKetik 3 untuk delete item. \nKetik 0 untuk membatalkan belanja')
    belanja = int(input('Masukkan pilihan anda: '))
    
    if belanja == 1:
        nama_item = input('Masukkan nama item: ')
        jumlah_item = int(input('Masukkan jumlah item: '))
        harga_item = int(input('Masukkan harga item: '))
        transaksi.add_item(nama_item, jumlah_item, harga_item)
        transaksi.print_order()
        confirm1 = input('Apakah anda ingin berbelanja(1), mengubah (2), menghapus (3), membatalkan transaksi(0)? (y/n) : ')
        
    elif belanja == 2:
        print("\n Ketik A untuk ubah item name \n ketik B untuk ubah item qty \n Ketik C untuk ubah price")
        ubah = input("Masukkan pilihan Anda: ")
        
        if ubah == "a":
            nama_item = input('Masukkan nama item: ')
            nama_item_baru = input('Masukkan nama item baru: ')
            transaksi.update_item_name(nama_item, nama_item_baru)
            transaksi.print_order()
            confirm1 = input('Apakah anda ingin berbelanja lagi? (y/n) : ')    

        elif ubah == "b":
            nama_item = nama_item = input('Masukkan nama item: ')
            jumlah_item = int(input('Masukkan jumlah item: '))
            transaksi.update_item_qty(nama_item, jumlah_item)
            transaksi.print_order()
            confirm1 = input('Apakah anda ingin berbelanja lagi? (y/n) : ')

        elif ubah == "c":
            nama_item = nama_item = input('Masukkan nama item: ')
            harga_item = int(input('Masukkan harga item: '))
            transaksi.update_item_price(nama_item, harga_item)
            transaksi.print_order()
            confirm1 = input('Apakah anda ingin berbelanja lagi? (y/n) : ')

    elif belanja == 3:
        nama_item = nama_item = input('Masukkan nama item: ')
        transaksi.delete_item(nama_item)
        transaksi.print_order()
        confirm1 = input('Apakah anda ingin berbelanja lagi? (y/n) : ')

    elif belanja == 0:
        transaksi.reset_transaction()
        confirm1 = input('Apakah anda ingin berbelanja lagi? (y/n) : ')

else:
    print("\nTerimakasih")

transaksi.total_price()
