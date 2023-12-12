from datetime import date
import os

class classConfig:
    """ini class config"""
    merk_mobil = open("merk.txt")
    merk = merk_mobil.readlines()
    
    jml_kursi_mobil = open("jml_kursi.txt")
    jml_kursi = jml_kursi_mobil.readlines()
    
    hrg_sewa_mobil = open("hrg_sewa.txt")
    hrg_sewa = hrg_sewa_mobil.readlines()
    
    indeks = 0
    
    def get_daftar_mobil(self):
        """ini digunakan untuk mencetak daftar harga sewa dengan detail merk, jumlah kursi, dan informasi sopir"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print('   Daftar Harga Sewa Mobil Automatic/Manual Harian')
        print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
        print(f"| {'No' :<3} | {'Merk Mobil' :<10} | {'Jumlah Kursi' :<18} | {'Harga Sewa' :<11} |")
        print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
        
        while self.indeks < len(self.merk):
            m_merk = str.replace(self.merk[self.indeks], '\n', '')
            m_jml_kursi = int(self.jml_kursi[self.indeks])
            m_hrg_sewa = str(int(self.hrg_sewa[self.indeks])) + '.000'
            
            print(f"| {self.indeks+1 :<3} | {m_merk :<10} | {m_jml_kursi} / {m_jml_kursi + 1} {'Tanpa sopir' :<12} | Rp {m_hrg_sewa :<8} |")
            
            self.indeks +=1
    
    def get_data_penyewaan(self):
        """ini digunakan untuk mengumpulkan informasi penyewa mobil dari pengguna, termasuk nama penyewa, alamat, pilihan mobil, tanggal ambil, dan tanggal kembali"""
        nama_lengkap_penyewa = input("Masukkan nama penyewa \n => ")
        alamat_lengkap_peyewa = input("Masukkan alamat lengkap penyewa \n => ")
        
        ulangi_pilih_mobil = True
        while ulangi_pilih_mobil:
            pilih_mobil = int(input("Pilihan mobil Anda? (1/2/3/...) \n => ")) - 1
            if pilih_mobil < 0 or pilih_mobil > self.indeks :
                print("Pilih nomor kendaraan yang tepat")
            else:
                ulangi_pilih_mobil = False
        
        ulangi_tanggal_ambil = True
        while ulangi_tanggal_ambil:
            tgl_ambil = input("Masukkan tanggal ambil (format: yyyy-mm-dd) \n => ")
            if len(tgl_ambil) != 10 or tgl_ambil[2] == '-':
                print("Format yang Anda masukkan salah")
            elif int(tgl_ambil[0:4]) < date.today().year or int(tgl_ambil[5:7]) < date.today().month or int(tgl_ambil[8:10]) < date.today().day:
                print(f"Tanggal pengambilan mobil minimal hari ini ({date.today().year} - {date.today().month} - {date.today().day})")
            else:
                ulangi_tanggal_ambil = False
                tgl_pinjam = date(int(tgl_ambil[0:4]) , int(tgl_ambil[5:7]) , int(tgl_ambil[8:10]))
        
        ulangi_tanggal_kembali = True
        while ulangi_tanggal_kembali:
            tgl_kembali = input("Masukkan tanggal kembali (format: yyyy-mm-dd) \n => ")
            if len(tgl_kembali) != 10 or tgl_kembali[2] == '-':
                print("Format yang Anda masukkan salah")
            elif int(tgl_kembali[0:4]) < tgl_pinjam.year or int(tgl_kembali[5:7]) < tgl_pinjam.month or int(tgl_kembali[8:10]) <= tgl_pinjam.day:
                print(f"Tanggal pengambilan mobil minimal sehari setelah pengambilan ({tgl_pinjam.year} - {tgl_pinjam.month} - {tgl_pinjam.day + 1})")
            else:
                ulangi_tanggal_kembali = False
                tgl_pengembalian = date(int(tgl_kembali[0:4]) , int(tgl_kembali[5:7]) , int(tgl_kembali[8:10]))
        
        lama_sewa = tgl_pengembalian - tgl_pinjam
        merk_mobil_sewa = str.replace(self.merk[pilih_mobil], '\n', '')
        harga_sewa = int(self.hrg_sewa[pilih_mobil])
        
        ulangi_sopir = True
        while ulangi_sopir:
            sopir = input("Apakah anda ingin menggunakan sopir pribadi (sewa perhari + Rp 75.000)? (Y/T) \n => ")
            if sopir == 'Y' or sopir == 'T':
                ulangi_sopir = False
                if sopir == 'Y':
                    total_biaya_sewa = lama_sewa.days * (harga_sewa + 75)
                    jumlah_kursi = int(self.jml_kursi[pilih_mobil])
                else:
                    total_biaya_sewa = lama_sewa.days * harga_sewa
                    jumlah_kursi = int(self.jml_kursi[pilih_mobil]) + 1
            else: 
                print("Jawab menggunakan Y untuk Ya dan T untuk Tidak")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{'Nama lengkap penyewa' :<40} : {nama_lengkap_penyewa}")
        print(f"{'Alamat lengkap penyewa' :<40} : {alamat_lengkap_peyewa}")
        print(f"{'Merk mobil (jumlah tempat duduk)' :<40} : {merk_mobil_sewa} ({jumlah_kursi} seat)" )
        print(f"{'Tarif sewa harian' :<40} : {harga_sewa}000")
        print(f"{'Tanggal ambil & kembali (durasi sewa)' :<40} : {tgl_pinjam} - {tgl_kembali} ({lama_sewa.days} hari)")
        print(f"{'Total biaya sewa' :<40} : Rp {total_biaya_sewa}000")
    
    merk_mobil.close()
    jml_kursi_mobil.close()
    hrg_sewa_mobil.close()