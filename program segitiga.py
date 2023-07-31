#Perulangan membuat segitiga

#print("*")
#print("**")

sisi = 7
#1. Menggunakan for
print("awal for")
for i in range(4):
    print("*")

#dummy variabel
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("akhir for")
#2. Menggunakan while
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir while")