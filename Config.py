from datetime import date

class Config():
    merk_mobil = open("merk.txt")
    merk = merk_mobil.readlines()
    
    jml_kursi_mobil = open("jml_kursi.txt")
    jml_kursi = jml_kursi_mobil.readlines()
    
    hrg_sewa_mobil = open("hrg_sewa.txt")
    hrg_sewa = hrg_sewa_mobil.readlines()
    
    def get_data_penyewaan():
        indek_mobil = int(input("Pilihan mobil Anda? (1/2/3/...) \n => "))
        
        ulangi_bulan_ambil = True
        while ulangi_bulan_ambil:
            bulan_ambil = int(input("Masukkan bulan ambil mobil (1 - 12) \n => "))
            if len(str(bulan_ambil)) > 2 or bulan_ambil > 12 or bulan_ambil < 1:
                print("Bulan harus diantara 1 - 12")
            elif bulan_ambil >= date.today().month:
                print("Bulan pengambilan minimal bulan ini")
            else:
                ulangi_bulan_ambil = False
        
        ulangi_tanggal_ambil = True
        while ulangi_tanggal_ambil:
            tanggal_ambil = int(input("Masukkan tanggal ambil mobil (1 - 31) \n => "))
            if len(str(tanggal_ambil)) > 2 or tanggal_ambil > 31 or tanggal_ambil < 1:
                print("Tanggal harus diantara 1 - 31")
            elif tanggal_ambil >= date.today().day:
                print("Tanggal pengambilan minimal hari ini")
            else:
                ulangi_tanggal_ambil = False
        
        ulangi_bulan_kembali = True
        while ulangi_bulan_kembali:
            bulan_kembali = int(input("Masukkan bulan kembali mobil (1 - 12) \n => "))
            if len(str(bulan_kembali)) > 2 or bulan_kembali > 12 or bulan_kembali < 1:
                print("Bulan harus diantara 1 - 12")
            elif bulan_kembali >= date.today().month:
                print("Bulan pengembalian minimal bulan ini")
            else:
                ulangi_bulan_kembali = False
        
        ulangi_tanggal_kembali = True
        while ulangi_tanggal_kembali:
            tanggal_kembali = int(input("Masukkan tanggal kembali mobil (1 - 31) \n => "))
            if len(str(tanggal_kembali)) > 2 or tanggal_kembali > 31 or tanggal_kembali < 1:
                print("Tanggal harus diantara 1 - 31")
            elif tanggal_kembali >= date.today().day:
                print("Tanggal pengembalian minimal besok (1 hari)")
            else:
                ulangi_tanggal_kembali = False
        
        berkas_penyewaan = input("Apakah berkas penyewaan sudah lengkap? Cth. KTP/NPWP/SIM/... (Ya/Y atau Tidak/T) \n =>")
    
    def get_daftar_mobil():
        i = 0
        
        print()
        print('   Daftar Harga Sewa Mobil Automatic/Manual Harian')
        print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
        print(f"| {'No' :<3} | {'Merk Mobil' :<10} | {'Jumlah Kursi' :<18} | {'Harga Sewa' :<11} |")
        print(f"| {'-'*3} | {'-'*10} | {'-'*18} | {'-'*11} |")
        
        while i < len(Config.merk):
            m_merk = str.replace(Config.merk[i], '\n', '')
            m_jml_kursi = int(Config.jml_kursi[i])
            m_hrg_sewa = str(int(Config.hrg_sewa[i])) + '.000'
            
            print(f"| {i+1 :<3} | {m_merk :<10} | {m_jml_kursi} / {m_jml_kursi + 1} {'Tanpa sopir' :<12} | Rp {m_hrg_sewa :<8} |")
            
            i +=1
    
    merk_mobil.close()
    jml_kursi_mobil.close()
    hrg_sewa_mobil.close()
    
# Config.get_daftar_mobil()
Config.get_data_penyewaan()