from datetime import datetime, date

try:
    str_tgl = "2023-12-19"
    tgl = datetime.strptime(str_tgl, "%Y-%m-%d").date()
    lama = (tgl - date.today()).days
    print(lama)
except:
    print("Format yang Anda masukkan salah")