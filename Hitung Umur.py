
print("======= Hitung Umur Loooo ========")
import datetime as dt

print("Silahkan masukan tanggal, bulan dan tahun lahir anda = ")
tanggal = int(input("Tanggal = "))
bulan   = int(input("Bulan = "))
tahun   = int(input("Tahun = "))

tanggal_lahir = dt.date(tanggal,bulan,tahun)
print(f"tanggal lahir anda adalah  {tanggal_lahir}")