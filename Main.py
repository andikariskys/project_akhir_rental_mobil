import Config

class ClassMain():
    config = Config.classConfig

    print("Selamat Datang di Rental Mobil Algopro")
    print()
    print("Silakan login terlebih dahulu")
    ulangi_login = True
    while ulangi_login:
        username = input("Masukkan username anda (tekan CRTL + C untuk keluar) \n => ")
        password = input("Masukkan password anda \n => ")
        if username == "Admin" and password == "Admin":
            config.get_daftar_mobil(config)
            config.get_data_penyewaan(config)
            ulangi_login = False
        else:
            print()
            print("Username dan atau password yang anda masukkan salah, silakan coba lagi")