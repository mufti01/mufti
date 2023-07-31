
# Algoritma Ke-3

koefisien = float(input("Masukkan koefisienn polinomial :"))
n = 2*(koefisien)-1
x = float(input("Masukkan nilai x yang ingin dicari turunannay :"))

y = koefisien[1]
z = koefisien[1]
for j in range(n-1,0,-1):
    y = x*y + koefisien[j]
    z = x*z + y

y = x*y*z + koefisien[0]

print ("Hasil p(x) dan p'(x) adalah %.3f dan %.3f berturut-turut"%(y,z))