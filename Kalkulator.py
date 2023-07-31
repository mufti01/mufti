import streamlit as st
print("========KALKULATOR SEDERHANA=======")
print(10*"$")

angka_1 = float(input("Masukan angka 1 = ")) #float biar bisa ada koma2
operator = input("Operator (+,-,x,/) = ") #harus string/text
angka_2 = float(input("Masukan angka 2 = "))

#percabangannya

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah  {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Belum ada operatornya masukin yang benar dongggg!")


print("========TERIMAKASIH=======")
