import sqlite3

databaseName = 'myDb.db'
conn = sqlite3.connect(databaseName)

###LOGIN/DAFTAR###
def login():
    conn.execute(
        "create table if not exists akunPengguna (id integer primary key , username text, password text, nohandphone number )"
    )
    class masuk:
        def __init__(self, username, password, id=None):
            self.__Username = username
            self.__Password = password
            self.__id = id

        def set_username(self, username):
            self.__Username = username
        def get_username(self):
            return self.__Username

        def set_password(self, password):
            self.__Password = password
        def get_password(self):
            return self.__Password

        def cekakun():
            res = conn.execute("select * from akunPengguna where username = ?", (data.get_username(),))
            if res.fetchone() is None:
                print("Username Salah ")
                login()
            else:
                res = conn.execute("select * from akunPengguna where password = ?", (data.get_password(),))
                if res.fetchone() is None:
                    print("Password Salah")
                    login()
                else:
                    print("Selamat Datang Di Aplikasi Manajemen Keuangan")

    class daftar(masuk):
        def __init__(self, username, password, nohandphone):
            super().__init__(username, password)
            self.__Nohandphone = nohandphone

        def set_nohandphone(self, nohandphone):
            self.__Nohandphone = nohandphone
        def get_nohandphone(self):
            return self.__Nohandphone


    print("[1] LOGIN \n[2] DAFTAR")
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        data = masuk(input("Masukkan Username : "), input("Masukkan Password : "))
        user = masuk.cekakun()
    elif pilih == "2":
        data = daftar(input("Masukkan Username : "), input("Masukkan Password : "), input("Masukkan No. Handphone : "))
        id = 1
        while True:
            res = conn.execute("select * from akunPengguna where id = ?", (id,))
            if res.fetchone() is None:
                break
            else:
                id += 1
        res = conn.execute("select * from akunPengguna where username = ?", (data.get_username(),))
        if res.fetchone() is None:
            conn.execute("insert into akunPengguna values (?,?,?,?)",
                         (id, data.get_username(), data.get_password(), data.get_nohandphone()))
            conn.commit()


### MENU ###
def menu():
    class menu:
        def __init__(self, Pilihan):
            self.__pilihan = Pilihan

        def pilih_menu(self):
            global pilih

            if self.__pilihan == 1:
                pendapatan()
            elif self.__pilihan == 2:
                pengeluaran()
            elif self.__pilihan == 3:
                hutang()
            elif self.__pilihan == 4:
                piutang()
            elif self.__pilihan == 5:
                budget()
            elif self.__pilihan == 6:
                dana_darurat()
            elif self.__pilihan == 7:
                laporan()
            elif self.__pilihan == 8:
                profil()
            else:
                print("Inputan Salah, Silahkan Menginputkan Ulang")

        print(" >>>>>MENU<<<<<\n [1] Pendapatan\n [2] Pengeluaran\n [3] Hutang\n [4] Piutang\n [5] Budget\n [6] Dana Darurat\n [7] Laporan Keuangan\n [8] Profil")

while True:
    login()
conn.close()