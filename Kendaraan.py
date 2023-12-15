from datetime import date
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
            print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
            print(f"| {'No' :<3} | {'Merk Mobil' :<10} | {'Jumlah Kursi' :<18} | {'Harga Sewa' :<11} |")
            print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
            
            indeks_mobil = 0
            no = 1
            while indeks_mobil < len(self.__data_kendaraan):
                mob_merk = str.replace(self.__data_kendaraan[indeks_mobil], '\n', '')
                mob_jml_kursi = int(self.__data_kendaraan[indeks_mobil +1])
                mob_hrg_sewa = int(self.__data_kendaraan[indeks_mobil +2]) * 1000
                
                print(f"| {no :<3} | {mob_merk :<10} | {mob_jml_kursi} / {mob_jml_kursi + 1} {'Tanpa sopir' :<12} | Rp {mob_hrg_sewa :<8} |")
            
                print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
                indeks_mobil += 3
                no += 1

ken = Kendaraan('Mobil.txt', 'Mobil')
ken.tampilkan_kendaraan()