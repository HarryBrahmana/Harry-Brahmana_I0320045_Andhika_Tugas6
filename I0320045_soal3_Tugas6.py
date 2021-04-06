# Soal 3 Tugas 6
# Membuat program perintah dengan ketentuan pengulangan dan fungsi range() dengan hasil program seperti digambar pada pdf
print("Mesin Bilangan Prima")
print("---------------------------------")
print("")
print("Silahkan baca terlebih dahulu keterangan dibawah ini untuk memulai")
print("")
print("Ket : Jika sudah selesai menginput angka klik ENTER, jika belum lanjutkan menginput nilai")
print("")
input("Klik ENTER untuk memulai")
print("")
nilai = [ ]
x = int(input("Silahkan masukkan angka : "))
while x != '' :
    nilai.append(int(x))
    x = input("Masukkan angka berikutnya :")
for a in nilai :
    for x in range(2, a):
        if a % x == 0:
            print(a, "bukan bilangan prima")
            break
    else:
        print(a, "adalah prima")
print("")
print("------------------------------------")
input("Klik ENTER untuk kembali")
print("")
print("Terima Kasih")
