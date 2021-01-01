import sqlite3
import os

databaseName = 'myDb.db'
conn = sqlite3.connect(databaseName)
Id = None

###LOGIN/DAFTAR###
def login():
    conn.execute(
        "create table if not exists akunPengguna (id integer primary key , username text, password text, nohandphone number, TTL text, Pekerjaan text, Status text )"
    )
    class masuk:
        def __init__(self, username, password, id):
            self.__Username = username
            self.__Password = password
            self.__Id = id

        def set_username(self, username):
            self.__Username = username
        def get_username(self):
            return self.__Username

        def set_password(self, password):
            self.__Password = password
        def get_password(self):
            return self.__Password

        def set_id(self, id):
            self.__Id = id
        def get_id(self):
            return self.__Id

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
                    res = conn.execute("select * from akunPengguna where id = ?", (data.get_id(),))
                    if res.fetchone() is None:
                        print("ID salah")
                        login()
                    else:
                        global Id
                        Id = data.get_id()
                        print("Selamat Datang Di Aplikasi Manajemen Keuangan")
                        menu()

    class daftar(masuk):
        def __init__(self, username, password, id, nohandphone, ttl, pekerjaan, status):
            super().__init__(username, password, id)
            self.__Nohandphone = nohandphone
            self.__TTL = ttl
            self.__Pekerjaan = pekerjaan
            self.__Status = status

        def set_ttl(self, ttl):
            self.__TTL = ttl
        def get_ttl(self):
            return self.__TTL
        def set_pekerjaan(self, pekerjaan):
            self.__Pekerjaan = pekerjaan
        def get_pekerjaan(self):
            return self.__Pekerjaan
        def set_status(self, status):
            self.__Status = status
        def get_status(self):
            return self.__Status
        def set_nohandphone(self, nohandphone):
            self.__Nohandphone = nohandphone
        def get_nohandphone(self):
            return self.__Nohandphone

    print("[1] LOGIN \n[2] DAFTAR")
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        data = masuk(input("Masukkan Username : "), input("Masukkan Password : "), input("Masukkan ID : "))
        os.system('cls')
        user = masuk.cekakun()
    elif pilih == "2":
        id = 1
        data = daftar(input("Masukkan Username : "), input("Masukkan Password : "), id, input("Masukkan No. Handphone : "), input("Masukkan TTL : "), input("Masukkan Pekerjaan : "), input("Masukkan Status : "))
        while True:
            res = conn.execute("select * from akunPengguna where id = ?", (id,))
            if res.fetchone() is None:
                break
            else:
                id += 1
        res = conn.execute("select * from akunPengguna where username = ?", (data.get_username(),))
        if res.fetchone() is None:
            conn.execute("insert into akunPengguna values (?,?,?,?,?,?,?)",
                         (id, data.get_username(), data.get_password(), data.get_nohandphone(), data.get_ttl(), data.get_pekerjaan(), data.get_status()))
            conn.commit()
            print("Id kamu adalah : ", id)
            print("Perhatian!!! ID DIGUNAKAN UNTUK MASUK KE DALAM APLIKASI")

### MENU ###
def menu():
    cek = int(Id)
    class cetakan:
        def __init__(self, tanggal, jumlah, keterangan):
            self.__Jumlah = jumlah
            self.__Tanggal = tanggal
            self.__Keterangan = keterangan

        def set_jumlah(self, jumlah):
            self.__Jumlah = jumlah
        def get_jumlah(self):
            return self.__Jumlah

        def set_tanggal(self, tanggal):
            self.__Tanggal = tanggal
        def get_tanggal(self):
            return self.__Tanggal

        def set_keterangan(self, keterangan):
            self.__Keterangan = keterangan
        def get_keterangan(self):
            return self.__Keterangan

    class hutangpiutang(cetakan):
        def __init__(self, tanggal, jumlah, keterangan, jatuhtempo):
            super().__init__( tanggal, jumlah, keterangan)
            self.__JatuhTempo = jatuhtempo

        def set_jatuhtempo(self, jatuhtempo):
            self.__JatuhTempo = jatuhtempo

        def get_jatuhtempo(self):
            return self.__JatuhTempo

    def pendapatan():
        print(" >>>PENDAPATAN<<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_pendapatan = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_pendapatan == "1":
            conn.execute(
                "create table if not exists Pendapatan (idAkun integer, tanggal text, jumlah integer , keterangan text )"
            )

            data = cetakan(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "), input("Masukkan Keterangan : "))
            os.system('cls')
            conn.execute("insert into Pendapatan values (?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan()))
            conn.commit()
            print("Data Telah Disimpan")
            pendapatan()
        elif pilih_pendapatan == "2":
            res = conn.execute("select * from Pendapatan where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Pendapatan")
                pendapatan()
            else:
                cursor = conn.cursor().execute("select * from pendapatan")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                pendapatan()
        elif pilih_pendapatan == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            pendapatan()

    def pengeluaran():
        print(" >>>PENGELUARAN<<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_pengeluaran = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_pengeluaran == "1":
            conn.execute(
                "create table if not exists Pengeluaran (idAkun integer, tanggal text, jumlah integer , keterangan text )"
            )

            data = cetakan(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "), input("Masukkan Keterangan : "))
            os.system('cls')
            conn.execute("insert into Pengeluaran values (?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan()))
            conn.commit()
            print("Data Telah Disimpan")
            pengeluaran()
        elif pilih_pengeluaran == "2":
            res = conn.execute("select * from Pengeluaran where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Pendapatan")
                pengeluaran()
            else:
                cursor = conn.cursor().execute("select * from pengeluaran")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                pengeluaran()
        elif pilih_pengeluaran == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            pengeluaran()

    def budget():
        print(" >>>>>BUDGET<<<<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_budget = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_budget == "1":
            conn.execute(
                "create table if not exists Budget (idAkun integer, tanggal text, jumlah integer , keterangan text )"
            )

            data = cetakan(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "), input("Masukkan Keterangan : "))
            os.system('cls')
            conn.execute("insert into Budget values (?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan()))
            conn.commit()
            print("Data Telah Disimpan")
            budget()
        elif pilih_budget == "2":
            res = conn.execute("select * from Budget where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Budget")
                budget()
            else:
                cursor = conn.cursor().execute("select * from Budget")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                budget()
        elif pilih_budget == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            budget()

    def dana_darurat():
        print(" >>DANA DARURAT<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_danadarurat = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_danadarurat == "1":
            conn.execute(
                "create table if not exists DanaDarurat (idAkun integer, tanggal text, jumlah integer , keterangan text )"
            )

            data = cetakan(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "), input("Masukkan Keterangan : "))
            os.system('cls')
            conn.execute("insert into DanaDarurat values (?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan()))
            conn.commit()
            print("Data Telah Disimpan")
            dana_darurat()
        elif pilih_danadarurat == "2":
            res = conn.execute("select * from DanaDarurat where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Dana Darurat")
                dana_darurat()
            else:
                cursor = conn.cursor().execute("select * from DanaDarurat")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                dana_darurat()
        elif pilih_danadarurat == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            dana_darurat()

    def hutang():
        print(" >>>>HUTANG<<<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_hutang = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_hutang == "1":
            conn.execute(
                "create table if not exists Hutang (idAkun integer, tanggal text, jumlah integer , keterangan text, jatuhTempo text)"
            )

            data = hutangpiutang(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "), input("Masukkan Keterangan : "), input("Masukkan Jatuh Tempo : "))
            os.system('cls')
            conn.execute("insert into Hutang values (?,?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan(), data.get_jatuhtempo()))
            conn.commit()
            print("Data Telah Disimpan")
            hutang()
        elif pilih_hutang == "2":
            res = conn.execute("select * from Hutang where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Dana Hutang")
                hutang()
            else:
                cursor = conn.cursor().execute("select * from Hutang")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                hutang()
        elif pilih_hutang == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            hutang()

    def piutang():
        print(" >>>>PIUTANG<<<<\n [1] Tambah Data\n [2] Lihat Data\n [3] Kembali Ke Menu")
        pilih_piutang = input("Masukkan Pilihan : ")
        os.system('cls')

        if pilih_piutang == "1":
            conn.execute(
                "create table if not exists Piutang (idAkun integer, tanggal text, jumlah integer , keterangan text, jatuhTempo text)"
            )

            data = hutangpiutang(input("Masukkan Tanggal : "), input("Masukkan Jumlah : "),
                                 input("Masukkan Keterangan : "), input("Masukkan Jatuh Tempo : "))
            os.system('cls')
            conn.execute("insert into Piutang values (?,?,?,?,?)",
                         (Id, data.get_tanggal(), data.get_jumlah(), data.get_keterangan(), data.get_jatuhtempo()))
            conn.commit()
            print("Data Telah Disimpan")
            piutang()
        elif pilih_piutang == "2":
            res = conn.execute("select * from Piutang where idAkun = ?", (Id,))
            if res.fetchone() is None:
                print("Belum Ada Dana Piutang")
                piutang()
            else:
                cursor = conn.cursor().execute("select * from Piutang")
                for row in cursor:
                    if row[0] == cek:
                        print(f'{row[1]}, {row[2]}, {row[3]}')
                    else:
                        continue
                enter = input("TEKAN ENTER UNTUK KEMBALI")
                piutang()
        elif pilih_piutang == "3":
            menu()
        else:
            print("Inputan Salah, Silahkan Masukkan Ulang Pilihan!!!")
            piutang()

    def profil():
        un = None
        pw = None
        ID = None
        nh = None
        ttl = None
        pk = None
        status = None
        cursor = conn.cursor().execute("select * from akunPengguna")
        for row in cursor:
            if row[0] == cek:
                un = row[1]
                pw = row[2]
                ID = row[0]
                nh = row[3]
                ttl = row[4]
                pk = row[5]
                status = row[6]
        print("ID : ", ID, "\nUSERNAME : ", un, "\nPASSWORD : ", pw, "\nNO.HANDPHONE : ", nh, "\nTTL : ", ttl,
                  "\nPEKERJAAN : ", pk, "\nSTATUS : ", status)

    def laporan():
        print(" [1] Keuangan\n [2] Hutang\n [3] Piutang\n [4] Dana Darurat\n [5] Budget\n [6] Kembali")
        pilih = input("Masukkan Pilihan : ")
        if pilih == "1":
            dapat = 0
            luar = 0
            cursor = conn.cursor().execute("select * from Pendapatan")
            for row in cursor:
                if row[0] == cek:
                    dapat += row[2]
            cursor = conn.cursor().execute("select * from Pengeluaran")
            for row in cursor:
                if row[0] == cek:
                    luar += row[2]
            jumlah = dapat - luar
            print("Jumlah Keuangan : ", jumlah)
            laporan()

        elif pilih == "2":
            tang = 0
            cursor = conn.cursor().execute("select * from Hutang")
            for row in cursor:
                if row[0] == cek:
                    tang += row[2]
            print("Jumlah Hutang : ", tang)
            laporan()

        elif pilih == "3":
            piu = 0
            cursor = conn.cursor().execute("select * from Piutang")
            for row in cursor:
                if row[0] == cek:
                    piu += row[2]
            print("Jumlah Piutang : ", piu)
            laporan()

        elif pilih == "4":
            dar = 0
            cursor = conn.cursor().execute("select * from DanaDarurat")
            for row in cursor:
                if row[0] == cek:
                    dar += row[2]
            print("Jumlah Dana Darurat : ", dar)
            laporan()

        elif pilih == "5":
            bud = 0
            cursor = conn.cursor().execute("select * from Budget")
            for row in cursor:
                if row[0] == cek:
                    bud += row[2]
            print("Jumlah Budget : ", bud)
            laporan()

        else:
            menu()

######## PILIHAN MENU ######## PILIHAN MENU ######## PILIHAN MENU ######## PILIHAN MENU ######## PILIHAN MENU ########
    print(
        " >>>>>MENU<<<<<\n [1] Pendapatan\n [2] Pengeluaran\n [3] Hutang\n [4] Piutang\n [5] Budget\n [6] Dana Darurat\n [7] Laporan Keuangan\n [8] Profil\n [9] Keluar")
    pilihan = (input("Masukan Pilihan : "))
    os.system('cls')
    if pilihan == "1":
        pendapatan()
    elif pilihan == "2":
        pengeluaran()
    elif pilihan == "3":
        hutang()
    elif pilihan == "4":
        piutang()
    elif pilihan == "5":
        budget()
    elif pilihan == "6":
        dana_darurat()
    elif pilihan == "7":
        laporan()
    elif pilihan == "8":
        profil()
    elif pilihan == "9":
        login()
    else:
        print("Inputan Salah, Silahkan Menginputkan Ulang")
        menu()

while True:
    login()
conn.close()