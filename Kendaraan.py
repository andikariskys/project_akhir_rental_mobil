from datetime import datetime, date
import os

class Kendaraan:
    # Membuat variabel private (hanya dapat diakses oleh class ini)
    __jenis = ''
    __data_kendaraan = []
    
    #ini adalah definisi dari metode, ini akan dijalankan saat object dari kelas dibuat
    def __init__(self, file, jenis): 
        #diguanakan untuk menyimpan jenis kendaraan mobil dan motor
        self.__jenis = jenis 
        
        #membuka file dan menyimpan kedalam variabel
        ambil_kendaraan = open(file) 
        #membaca seluruh isi file yang telah dibuat
        self.__data_kendaraan = ambil_kendaraan.readlines() 
    
    def tampilkan_kendaraan(self):
        #ini digunakan untuk membersihkan tampilan konsole
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        #memeriksa jenis kendaraan, jika mobil maka menampilkan harga sewa mobil
        if self.__jenis == 'Mobil': 
            print()
            print('   Daftar Harga Sewa Mobil Automatic/Manual Harian')
            print(f"| {'-'*3} | {'-'*10} | {'-'*10} | {'-'*11} |")
            print(f"| {'No' :<3} | {'Merk Mobil' :<10} | {'Jml Kursi' :<10} | {'Harga Sewa' :<11} |")
            print(f"| {'-'*3} | {'-'*10} | {'-'*10} | {'-'*11} |")
            
            indeks_mobil = 0
            no = 1
            #memulai data untuk menampilkan informasi mobil
            while indeks_mobil < len(self.__data_kendaraan): 
                mob_merk = str.replace(self.__data_kendaraan[indeks_mobil], '\n', '')
                #mengambil jumlah kursi dan mengonversinya ke integer
                mob_jml_kursi = int(self.__data_kendaraan[indeks_mobil +1]) 
                #mengambil harga sewa kemudian mengonversi ke integer, kemudian mengalikannya dengan 1000 menyatakan harga dalam ribu rupiah
                mob_hrg_sewa = int(self.__data_kendaraan[indeks_mobil +2]) * 1000 
                
                print(f"| {no :<3} | {mob_merk :<10} | {mob_jml_kursi :<10} | Rp {mob_hrg_sewa :<8} |") 
            
                #menambahkan baris pembatas tabel
                print(f"| {'-'*3} | {'-'*10} | {'-'*10} | {'-'*11} |") 
                indeks_mobil += 3
                no += 1
        else:
            print()
            print('   Daftar Harga Sewa Motor Automatic/Manual Harian')
            print(f"| {'-'*3} | {'-'*21} | {'-'*15} | {'-'*11} |")
            print(f"| {'No' :<3} | {'Merk Motor' :<21} | {'Transmisi' :<15} | {'Harga Sewa' :<11} |")
            print(f"| {'-'*3} | {'-'*21} | {'-'*15} | {'-'*11} |")
            
            indeks_motor = 0
            no = 1
            #memulai data kendaraan untuk menampilkan informasi motor
            while indeks_motor < len(self.__data_kendaraan): 
                #menghapus karakter newline dari nama merk motor
                mot_merk = str.replace(self.__data_kendaraan[indeks_motor], '\n', '') 
                #untuk mengambil informasi transmisi motor 
                mot_transmisi = str.replace(self.__data_kendaraan[indeks_motor +1], '\n', '') 
                #mengambil harga sewa kemudian mengonversi ke integer, kemudian mengalikannya dengan 1000 menyatakan harga dalam ribu rupiah
                mot_hrg_sewa = int(self.__data_kendaraan[indeks_motor +2]) * 1000 
                
                print(f"| {no :<3} | {mot_merk :<21} | {mot_transmisi :<15} | Rp {mot_hrg_sewa :<8} |")
            
                print(f"| {'-'*3} | {'-'*21} | {'-'*15} | {'-'*11} |")
                indeks_motor += 3
                no += 1
    
    def sewa_kendaraan(self):
        #ini digunakan untuk meminta dan menyimpan nama penyewa dari inputan pengguna
        nama_lengkap_penyewa = input("Masukkan nama penyewa \n => ") 
        #ini digunakan untuk meminta dan menyimpan alamat lengkap dari inputan pengguna
        alamat_lengkap_peyewa = input("Masukkan alamat lengkap penyewa \n => ") 
        
        while True:
            #meminta inputan pengguna untuk memilih kendaraan
            pilih_kendaraan = int(input("Pilihan mobil Anda? (1/2/3/...) \n => ")) - 1 
            #memeriksa apakah pilihan valid
            if pilih_kendaraan < 0 or pilih_kendaraan > len(self.__data_kendaraan) / 3 : 
                print("Pilih nomor kendaraan yang tepat")
            else:
                pilih_kendaraan = pilih_kendaraan * 3 
                break #keluar dari loop setelah mendapatkan pilihan valid
        
        while True:
            try:
                #digunakan untuk memasukkan tanggal pengambilan kendaraan
                input_tgl = input("Masukkan tanggal pengambilan mobil (format: yyyy-mm-dd) \n => ") 
                #mengonversi inputan tanggal menjadi objek 'date'
                tgl_ambil = datetime.strptime(input_tgl, "%Y-%m-%d").date() 
                #memeriksa tanggal pengambilan kendaraan setidaknya hari ini
                if tgl_ambil < date.today(): 
                    print("Tanggal ambil kendaraan minimal hari ini")
                else:
                    break
            except:
                #ini yang akan ditampilkan jika inputan salah atau tidak sesuai
                print("Format yang anda masukkan salah") 
        
        while True:
            try:
                #meminta pengguna memasukkan tanggal pengembalian kendaraan
                input_tgl = input("Masukkan tanggal pengembalian mobil (format: yyyy-mm-dd) \n => ") 
                tgl_kembali = datetime.strptime(input_tgl, "%Y-%m-%d").date()
                if tgl_kembali <= tgl_ambil:
                    print("Tanggal pengembalian kendaraan minimal sehari setelah pengambilan")
                else:
                    break
            except:
                print("Format yang anda masukkan salah")
        
        #menghitung durasi sewa dalam jumlah hari berdasarkan selisih antara tanggal pengambilan dan pengembalian
        lama_sewa = (tgl_kembali - tgl_ambil).days 
        #mengambil nama merk kendaraan
        merk_kendaraan = str.replace(self.__data_kendaraan[pilih_kendaraan], '\n', '') 
        #memeriksa jenis kendaraan jika mobil
        if self.__jenis == 'Mobil': 
            #mengambil jumlah mobil dari data kendaraan
            jumlah_kursi = int(self.__data_kendaraan[pilih_kendaraan + 1]) 
        else: 
            #jika jenis kendaraan bukan mobil(motor)
            transmisi = str.replace(self.__data_kendaraan[pilih_kendaraan + 1], '\n', '') #mengambil insformasi transmisi motor
        harga_sewa = int(self.__data_kendaraan[pilih_kendaraan + 2]) *1000 #mengambil harga sewa kendaraan dari data kendaraan dan harga diubah menjadi ribu rupiah
        total_biaya_sewa = harga_sewa * lama_sewa #menghitung total biaya sewa berdasarkan harga sewa harian dan durasi sewa
        
        os.system('cls' if os.name == 'nt' else 'clear') 
        """Mencetak informasi penyewa dan detail penyewaan"""
        print(f"{'Nama lengkap penyewa' :<40} : {nama_lengkap_penyewa}")
        print(f"{'Alamat lengkap penyewa' :<40} : {alamat_lengkap_peyewa}")
        if self.__jenis == 'Mobil':
            print(f"{'Merk mobil (Jumlah tempat duduk)' :<40} : {merk_kendaraan} ({jumlah_kursi} kursi)" )
        else:
            print(f"{'Merk Motor (Transmisi)' :<40} : {merk_kendaraan} (Transmisi {transmisi})")
        print(f"{'Tarif sewa harian' :<40} : {harga_sewa}")
        print(f"{'Tanggal ambil & kembali (durasi sewa)' :<40} : {tgl_ambil} - {tgl_kembali} ({lama_sewa} hari)")
        print(f"{'Total biaya sewa' :<40} : Rp {total_biaya_sewa}")

# jalankan program 
while True:
    #meminta inputan username dari pengguna
    username = input("Masukkan username anda \n => ") 
    #meminta inputan password dari pengguna
    password = input("Masukkan password anda \n => ") 
    
    #memeriksa apakah inputan sesuai
    if username == "Admin" and password == "Admin": 
        #membuat objek dari kelas 'Kendaraan', dengan parameter file 'Mobil.txt' dan jenis kendaraan 'Mobil'
        ken = Kendaraan('Mobil.txt', 'Mobil') # jika ingin menyewa motor, maka ubah 'Mobil.txt' menjadi 'Motor.txt' dan 'Mobil' menjadi 'Motor'
        ken.tampilkan_kendaraan() #memanggil method untuk menampilkan program
        ken.sewa_kendaraan() #memanggil method untuk meminta data penyewaan
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear') 
        #jika username dan password salah maka akan menampilkan pesan berikut
        print("Username dan atau password yang anda masukkan salah ")