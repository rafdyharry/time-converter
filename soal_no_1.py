import math                                 #import math untuk menggunakan floor pada fungsi
detik=input("Masuk detik: ")                #bikin perintah input untuk memasukan variabel yang di butuhkan
def timeconverter(second):                  #membikin fungsi untuk menjawab saol
                                   
    if int(detik) > 359999:                 #membikin kondisi batas yang bisa di compile oleh fungsi
        print("Melebihi Batas")
    else:                                               #jika memenuhi perintah yang di minta fungsi akan menjalankan rumus oleh soal yang di minta
        hh=math.floor(int(detik)/3600)          #ini adalah rumus untuk mengkonversikan dektik ke menit dan jam
        mm=math.floor((int(detik)%3600)/60)
        ss=math.floor((int(detik)%3600)%60)
        jam="konversi: {one}:{two}:{three}".format(one=hh,two=mm,three=ss)      #membuat format print untuk membagi waktu yang diinginkan
        return jam

print(timeconverter(detik))