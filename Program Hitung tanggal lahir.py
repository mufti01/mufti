#date and time

print("=======PROGRAM HITUNG UMUR SEDERHANA=======")

import datetime as dt

print("Silahkan masukan tanggal, bulan dan tahun lahir anda dibawah ini :")
Tanggal = int(input("Tanggal \t: "))
Bulan = int(input("Bulan \t\t:"))
Tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(Tahun,Bulan,Tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365 #.days agar ambil data angkanya aja
umur_bulan_sisa = (umur_hari.days % 365)//30
print(f"Umur anda adalah: {umur_hari}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

print("=======TERIMAKASIH=======")