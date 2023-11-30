class Config():
    merk_mobil = open("merk.txt")
    merk = merk_mobil.readlines()
    
    jml_kursi_mobil = open("jml_kursi.txt")
    jml_kursi = jml_kursi_mobil.readlines()
    
    hrg_sewa_mobil = open("hrg_sewa.txt")
    hrg_sewa = hrg_sewa_mobil.readlines()
    
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

Config.get_daftar_mobil()