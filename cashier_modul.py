import pandas as pd
from tabulate import tabulate


class Transaction:
    def __init__(self):
        """
        Fungsi inisialisasi untuk class Transaction.
        untuk mendefinisikan atribut data yang dimiliki.
        """
        self.item = dict()
        self.item_cek = True

    def add_item(self, name, qty, price):
        """Fungsi untuk menambahkan item yang akan dimasukkan ke dalam dictionary"""
        #memeriksa tipe data integer
        if type(qty) != int:
            print("Tipe data salah, jumlah barang harus berupa angka")

        elif type(price) != int:
            print("Tipe data salah, jumlah barang harus berupa angka")

        else:
            #memasukkan data ke dalam dictionary
            dict_add = {name: [qty, price, qty*price]}
            self.item.update(dict_add)
            print(f"Menambahkan ke dalam pesanan:{name}, jumlah {qty}, dengan harga Rp. {price}.")


    def update_item_name(self, name, new_name):
        temp = self.item[name]
        self.item.pop(name)
        self.item.update({new_name: temp})

        #menampilkan nama yang sudah diubah
        self.print_order()
        print(f"Mengubah nama item {name} menjadi {new_name}.")

    def update_item_qty(self, name, new_qty):
        #memeriksa tipe data integer
        if type(new_qty) != int:
            print("Tipe data salah, jumlah barang harus berupa angka")
        else:
            #memasukkan data ke dalam dictionary
            self.item[name][0] = new_qty
            self.item[name][2] = new_qty*self.item[name][1]

            #menampilkan data pesanan setelah dilakukan perubahan
            self.print_order()
            print(f"Mengubah jumlah item {name} menjadi {new_qty}")


    def update_item_price(self, name, new_price):
        """Fungsi untuk mengupdate item dalam dictionary"""

        if type(new_price)!=int:
            print("Tipe data salah, jumlah barang harus berupa angka")
        else:
            #memasukkan data ke dalam dictionary
            self.item[name][1] = new_price
            self.item[name][2] = new_price*self.item[name][0]

            #menampilkan data pesanan setelah dilakukan perubahan
            self.print_order()
            print(f"Mengubah harga item {name} menjadi Rp. {new_price}")

    def delete_item(self, name):
        """Fungsi untuk menghapus item dalam dictionary"""

        try:
            self.item.pop(name)
            print(f"Menghapus pesanan {name}.")
            print("")
            self.print_order()

        except KeyError:
            print(f"{name} tidak ada di dalamm daftar pesanan")

    def reset_transaction(self):
        """Fungsi untuk menghapus semua pesanan"""

        self.item = self.item.clear
        print("Item berhasil dihapus")

    def print_order(self):
        try:
            table_item = pd.DataFrame(self.item).T
            headers = ["Nama Item", "Jumlah Item", "Harga Item", "Total Harga"]
            print(tabulate(table_item, headers, tablefmt="github"))

            #menambahkan info total belanja sementara
            total_belanja = 0
            for item in self.item:
                total_belanja += self.item[item][2]
            print(f"Total Belanja Anda {total_belanja}")

        except:
            print("Belum Ada Pesanan")

    def check_order(self):

        try:
            #menampilkan pesanan
            table_item = pd.DataFrame(self.item).T
            headers = ["Nama Item", "Jumlah Item", "Harga Item", "Total Harga"]
            print(tabulate(table_item, headers, tablefmt="github"))

            #menambahkan info total belanja sementara
            total_belanja = 0
            for item in self.item:
                total_belanja += self.item[item][2]
            print(f"Total Belanja Anda {total_belanja}")

            #memeriksa kebenaran inputan jumlah/harga item
            kolom=0
            while kolom<2:
                for data in table_item[kolom]:
                    if data <=0:
                        self.item_cek = False
                kolom +=1

            if self.item_cek:
                print("Pemesanan sudah benar")
            else:
                print("Terdapat Kesalahan Input. Mohon periksa kembali")

        except ValueError:
            print("Belum ada pemesanan tercatat")

    def total_price(self):
        self.check_order()

        if self.item_cek:

            #menghitung total belanja
            total_belanja = 0
            for item in self.item:
                total_belanja += self.item[item][2]

            #menghitung diskon

            if total_belanja > 500_000:
                diskon_10 = 0.1
                total_belanja_akhir = int(total_belanja - (diskon_10*total_belanja))
                print(f"Anda mendapat diskon 10%, maka total belanja Anda adalah Rp.{total_belanja_akhir}")

            elif total_belanja > 300_000:
                diskon_8 = 0.08
                total_belanja_akhir = int(total_belanja - (diskon_8*total_belanja))
                print(f"Anda mendapat diskon 8%, maka total belanja Anda adalah Rp. {total_belanja_akhir}")

            elif total_belanja > 200_000:
                diskon_5 = 0.05
                total_belanja_akhir = int(total_belanja - (diskon_5*total_belanja))
                print(f"Anda mendapat diskon 5%, maka total belanja Anda adalah Rp. {total_belanja_akhir}")

            else:
                print(f"Total belanja Anda adalah Rp.{total_belanja}")

        else:
            print("Total belanja belum bisa dihitung")
