
import datetime as dt

print("Pilih rumus dibawah ini : ")
print("1. Rumus luas Lingkaran")
print("2. Program Konversi Suhu")
print("3. Rumus luas persegi panjang")
print("4. Rumus luas hitung umur")
print("5. Rumus hitung umur")
rumus = input("Silahkan input nomor yang ingin dipakai : ")
if rumus == "1":    
    print("======RUMUS LUAS LINGKARAN======")
#rumus luas lingkaran phi r^2
    jari = float(input("Masukan nilai alas dalam cm = "))
    luas = (22/7) * jari * jari
    print("Luas lingkaran adalah",luas,"cm^2")
    print(f"Luas lingkaran adalah {luas} cm^2")

elif rumus == "2":
    print("=====PROGRAM KONVERSI SUHU SEDERHANA=====")
    celcius = float(input("Masukan suhu dalam Celcius : "))
    print("Suhu adalah ",celcius,"Celcius")
    #Reamur
    Reamur = (4/5) * celcius
    print("Suhu adalah ",Reamur,"Reamur")
    #kelvin
    Kelvin = celcius + 273
    print("Suhu adalah ",Kelvin,"Kelvin")
    #fahreinhet
    fahreinhet = ((9/5) * celcius) + 32
    print("Suhu adalah ",fahreinhet,"fahreinhet")
elif rumus == "3":
    print("======RUMUS LUAS PERSEGI PANJANG======")
    #rumus luas persegi panjang P X L
   
    panjang = float(input("Masukan panjang = "))
    lebar = float(input("Masukan lebar = "))
    Luas = panjang * lebar
   
    print("Luas persegi panjang adalah", Luas, "cm^2")
    print("======TERIMKASIH======")
elif rumus == "4":
    print("Silahkan masukan tanggal, bulan dan tahun lahir anda dibawah ini :")
    Tanggal = int(input("Tanggal \t: "))
    Bulan = int(input("Bulan \t\t: "))
    Tahun = int(input("Tahun \t\t: "))

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

elif rumus == "5":
    print("Silahkan isi data yang ingin dilihat tipe datanya : ")
    data = input("Masukan data : ")
    print("Tipe data ", data, "adalah", type(data))
else:    
    print("======TOLONG MASUKAN ANGKA YANG BENAR======")
