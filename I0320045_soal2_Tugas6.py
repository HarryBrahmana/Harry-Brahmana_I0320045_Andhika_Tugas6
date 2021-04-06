# Soal 2 Tugas 6
# Membuat program menghitung nilai rata rata dari nilai yang diinput oleh user
print("Mesin Penghitung Nilai Rata Rata")
print("---------------------------------")
print("")
print("Ingin mencari nilai rata rata?")
print("Silahkan baca terlebih dahulu keterangan dibawah ini untuk memulai")
print("")
print("Ket : Jika sudah selesai menginput angka klik ENTER, jika belum lanjutkan menginput nilai")
print("")
input("Klik ENTER untuk memulai")
print("")
nilai = [ ]
x = int(input("Silahkan masukkan nilai yang mau di rata rata : "))
while x != '' :
    nilai.append(int(x))
    x = input("Masukkan nilai berikutnya :")
avg = sum(nilai) / len(nilai)
print("Hasil dari nilai rata rata adalah : ", avg)
print("")
print("------------------------------------")
input("Klik ENTER untuk kembali")
print("")
print("Terima Kasih")