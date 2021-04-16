print("===== Laman Penggantian Username =====")
nama = input("Masukan Nama Panggilan Anda : ")
namaamu = nama.upper()
unamemu = input("Masukan Username sosial media Anda : ")
usernamee = "@"+unamemu
app = "instagram"
appp = app.capitalize()
print("HALLO,", namaamu, "!!",
      "\nSelamat Datang di", appp,
      "\nApakah Anda Yakin akan Mengganti Username Anda" ,usernamee, "? (Y/T)")
keputusan = input(">>")
if keputusan == 'Y' :
    new = input("Masukan Username Baru Anda :")
    print("Selamat Menikmati Fitur Baru Kami dengan Username Baru Anda,",usernamee.replace(unamemu, new), "!!")
else:
    print("Anda Telah Membatalkan Proses Penggantian Username"
          "\n===== Sampai Jumpa !! =====")