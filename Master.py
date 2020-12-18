import sqlite3
import time

databaseName = 'myDb.db'
conn = sqlite3.connect(databaseName)

# PEMBUATAN MASING-MASING TABEL SETIAP CLASS


### MENU ###
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



### PENDAPATAN ###
conn.execute(
    "create table if not exists pendapatan (id_pendapatan integer primary key, tanggal date, jumlah int, keterangan text)"
)

def pendapatan():
    class pendapatan:
        def __init__(self, Id, Tanggal, Jumlah, Keterangan):
            self.__id = Id
            self.__tanggal = Tanggal
            self.__jumlah = Jumlah
            self.__keterangan = Keterangan



    pen = conn.execute("select max(id_pendapatan) from pendapatan")
    nomer = pen
    int(nomer)
    if nomer == 0:
        return
    else:
        nomer = nomer + 1

    localtime = time.asctime(time.localtime(time.time()))

    income = pendapatan(nomer,localtime, input("Masukkan Nominal : "), input("Masukkan Keterangan"))

    conn.execute("insert into pendapatan values (?,?,?,?)",(self.__id(), self.__tanggal(), self.__jumlah(), self.__keterangan()))
    conn.commit()
    cursor = conn.cursor().execute("select * from mahasiswa")
    for row in cursor:
        print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')


### START ###
while True:
    pilih = menu(int(input("Masukkan Pilihan : ")))
    pilih.pilih_menu()

conn.close()