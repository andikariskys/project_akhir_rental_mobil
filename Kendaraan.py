from datetime import datetime, date
import os

class Kendaraan:
    # Membuat variabel private (hanya dapat diakses oleh class ini)
    __jenis = ''
    __data_kendaraan = []
    
    def __init__(self, file, jenis):
        self.__jenis = jenis
        
        ambil_kendaraan = open(file)
        self.__data_kendaraan = ambil_kendaraan.readlines()
    
    def tampilkan_kendaraan(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if self.__jenis == 'Mobil':
            print()
            print('   Daftar Harga Sewa Mobil Automatic/Manual Harian')
            print(f"| {'-'*3} | {'-'*10} | {'-'*10} | {'-'*11} |")
            print(f"| {'No' :<3} | {'Merk Mobil' :<10} | {'Jml Kursi' :<10} | {'Harga Sewa' :<11} |")
            print(f"| {'-'*3} | {'-'*10} | {'-'*10} | {'-'*11} |")
            
            indeks_mobil = 0
            no = 1
            while indeks_mobil < len(self.__data_kendaraan):
                mob_merk = str.replace(self.__data_kendaraan[indeks_mobil], '\n', '')
                mob_jml_kursi = int(self.__data_kendaraan[indeks_mobil +1])
                mob_hrg_sewa = int(self.__data_kendaraan[indeks_mobil +2]) * 1000
                
                print(f"| {no :<3} | {mob_merk :<10} | {mob_jml_kursi :<10} | Rp {mob_hrg_sewa :<8} |")
            
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
            while indeks_motor < len(self.__data_kendaraan):
                mot_merk = str.replace(self.__data_kendaraan[indeks_motor], '\n', '')
                mot_transmisi = str.replace(self.__data_kendaraan[indeks_motor +1], '\n', '')
                mot_hrg_sewa = int(self.__data_kendaraan[indeks_motor +2]) * 1000
                
                print(f"| {no :<3} | {mot_merk :<21} | {mot_transmisi :<15} | Rp {mot_hrg_sewa :<8} |")
            
                print(f"| {'-'*3} | {'-'*21} | {'-'*15} | {'-'*11} |")
                indeks_motor += 3
                no += 1
    
    def sewa_kendaraan(self):
        nama_lengkap_penyewa = input("Masukkan nama penyewa \n => ")
        alamat_lengkap_peyewa = input("Masukkan alamat lengkap penyewa \n => ")
        
        while True:
            pilih_kendaraan = int(input("Pilihan mobil Anda? (1/2/3/...) \n => ")) - 1
            if pilih_kendaraan < 0 or pilih_kendaraan > len(self.__data_kendaraan) / 3 :
                print("Pilih nomor kendaraan yang tepat")
            else:
                pilih_kendaraan = pilih_kendaraan * 3
                break
        
        while True:
            try:
                input_tgl = input("Masukkan tanggal pengambilan mobil (format: yyyy-mm-dd) \n => ")
                tgl_ambil = datetime.strptime(input_tgl, "%Y-%m-%d").date()
                if tgl_ambil < date.today():
                    print("Tanggal ambil kendaraan minimal hari ini")
                else:
                    break
            except:
                print("Format yang anda masukkan salah")
        
        while True:
            try:
                input_tgl = input("Masukkan tanggal pengembalian mobil (format: yyyy-mm-dd) \n => ")
                tgl_kembali = datetime.strptime(input_tgl, "%Y-%m-%d").date()
                if tgl_kembali <= tgl_ambil:
                    print("Tanggal pengembalian kendaraan minimal sehari setelah pengambilan")
                else:
                    break
            except:
                print("Format yang anda masukkan salah")
        
        lama_sewa = (tgl_kembali - tgl_ambil).days
        merk_kendaraan = str.replace(self.__data_kendaraan[pilih_kendaraan], '\n', '')
        if self.__jenis == 'Mobil':
            jumlah_kursi = int(self.__data_kendaraan[pilih_kendaraan + 1])
        else:
            transmisi = str.replace(self.__data_kendaraan[pilih_kendaraan + 1], '\n', '')
        harga_sewa = int(self.__data_kendaraan[pilih_kendaraan + 2]) *1000
        total_biaya_sewa = harga_sewa * lama_sewa
        
        os.system('cls' if os.name == 'nt' else 'clear')
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
    username = input("Masukkan username anda \n => ")
    password = input("Masukkan password anda \n => ")
    
    if username == "Admin" and password == "Admin":
        # jika ingin menyewa motor, maka ubah 'Mobil.txt' menjadi 'Motor.txt' dan 'Mobil' menjadi 'Motor'
        ken = Kendaraan('Mobil.txt', 'Mobil')
        ken.tampilkan_kendaraan()
        ken.sewa_kendaraan()
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Username dan atau password yang anda masukkan salah ")