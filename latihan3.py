# input nilai variable
a=input("input nilai variable a : ")
b=input("input nilai variable b : ")

# Cetak nilai variable
print("VAriable a = ",a)
print("VAriable b = ",b)

# Cetak hasil operasi kedua variable dengan String Format
print("Hasil penggabungan {1} & {0} = %s".format(a,b) %(a+b))

#Konversi Nilai Variable
a=int (a)
b=int (b)
print("Hasil penjumlahan {1} + {0} = %s".format(a,b) %(a+b)) 
print("Hasil pembagian {1} / {0} = %s".format(a,b) %(a/b))
