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
        nama_lengkap_penyewa = input("Masukkan nama penyewa \n => ")
        alamat_lengkap_peyewa = input("Masukkan alamat lengkap penyewa \n => ")
        
        ulangi_pilih_mobil = True
        while ulangi_pilih_mobil:
            pilih_mobil = int(input("Pilihan mobil Anda? (1/2/3/...) \n => "))
            if pilih_mobil < 1 or pilih_mobil > self.indeks :
                print("Pilih nomor kendaraan yang tepat")
            else:
                ulangi_pilih_mobil = False
        
        ulangi_bulan_ambil = True
        while ulangi_bulan_ambil:
            bulan_ambil = int(input("Masukkan bulan ambil mobil (1 - 12) \n => "))
            if len(str(bulan_ambil)) > 2 or bulan_ambil > 12 or bulan_ambil < 1:
                print("Bulan harus diantara 1 - 12")
            elif bulan_ambil < date.today().month:
                print("Bulan pengambilan minimal bulan ini")
            else:
                ulangi_bulan_ambil = False
        
        ulangi_tanggal_ambil = True
        while ulangi_tanggal_ambil:
            tanggal_ambil = int(input("Masukkan tanggal ambil mobil (1 - 31) \n => "))
            if len(str(tanggal_ambil)) > 2 or tanggal_ambil > 31 or tanggal_ambil < 1:
                print("Tanggal harus diantara 1 - 31")
            elif tanggal_ambil < date.today().day:
                print("Tanggal pengambilan minimal hari ini")
            else:
                ulangi_tanggal_ambil = False
        
        ulangi_bulan_kembali = True
        while ulangi_bulan_kembali:
            bulan_kembali = int(input("Masukkan bulan kembali mobil (1 - 12) \n => "))
            if len(str(bulan_kembali)) > 2 or bulan_kembali > 12 or bulan_kembali < 1:
                print("Bulan harus diantara 1 - 12")
            elif bulan_kembali < bulan_ambil:
                print("Bulan pengembalian minimal bulan ini")
            else:
                ulangi_bulan_kembali = False
        
        ulangi_tanggal_kembali = True
        while ulangi_tanggal_kembali:
            tanggal_kembali = int(input("Masukkan tanggal kembali mobil (1 - 31) \n => "))
            if len(str(tanggal_kembali)) > 2 or tanggal_kembali > 31 or tanggal_kembali < 1:
                print("Tanggal harus diantara 1 - 31")
            elif tanggal_kembali <= tanggal_ambil:
                print("Tanggal pengembalian minimal besok (1 hari)")
            else:
                ulangi_tanggal_kembali = False
                
        ulangi_sopir = True
        while ulangi_sopir:
            sopir = input("Apakah anda ingin menggunakan sopir pribadi (sewa perhari + Rp 75.000)? (Y/T) \n => ")
            if sopir == 'Y' or sopir == 'T':
                ulangi_sopir = False
            else: 
                print("Jawab menggunakan Y untuk Ya dan T untuk Tidak")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        merk_mobil_sewa = str.replace(self.merk[pilih_mobil], '\n', '')
        harga_sewa = int(self.hrg_sewa[pilih_mobil])
        tgl_bln_tahun_ambil = date(date.today().year, bulan_ambil, tanggal_ambil)
        tgl_bln_tahun_kembali = date(date.today().year, bulan_kembali, tanggal_kembali)
        total_penyewaan = tgl_bln_tahun_kembali - tgl_bln_tahun_ambil
        if sopir == 'Y':
            total_biaya_sewa = total_penyewaan.days * (harga_sewa + 75)
            jumlah_kursi = int(self.jml_kursi[pilih_mobil])
        else: 
            total_biaya_sewa = total_penyewaan.days * harga_sewa
            jumlah_kursi = int(self.jml_kursi[pilih_mobil]) + 1
        
        print(f"{'Nama lengkap penyewa' :<40} : {nama_lengkap_penyewa}")
        print(f"{'Alamat lengkap penyewa' :<40} : {alamat_lengkap_peyewa}")
        print(f"{'Merk mobil (jumlah tempat duduk)' :<40} : {merk_mobil_sewa} ({jumlah_kursi} seat)" )
        print(f"{'Tarif sewa harian' :<40} : {harga_sewa}")
        print(f"{'Tanggal ambil & kembali (durasi sewa)' :<40} : {tgl_bln_tahun_ambil} - {tgl_bln_tahun_kembali} ({total_penyewaan.days} hari)")
        print(f"{'Total biaya sewa' :<40} : Rp {total_biaya_sewa}.000")
    
    merk_mobil.close()
    jml_kursi_mobil.close()
    hrg_sewa_mobil.close()