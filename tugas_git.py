data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
} 

#1. Tampilkan seluruh data dari data panen termasuk nama lokasi dan hasil panen masing-masing.
for i,j in data_panen.items() :
    print(f"Lokasi : {i}")
    print(f"Tempat : {j["nama_lokasi"]}")
    print(f"Hasil Panen : {j["hasil_panen"]}")

#2. Tampilkan jumlah hasil panen jagung dari lokasi2.
print(data_panen['lokasi2']["hasil_panen"]["jagung"])

#3. Tampilkan nama lokasi dari lokasi3.
print(data_panen['lokasi3']["nama_lokasi"])

#4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda:
#5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
panen_padi = []
panen_kedelai = []
for i in data_panen.values() :
   panen_padi.append(i["hasil_panen"]["padi"])
   panen_kedelai.append(i["hasil_panen"]["kedelai"])

print(panen_padi)
print(panen_kedelai)

#6 Buat Percabangan jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perh
for i,j in data_panen.items() :
    if(j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800) :
        print(f"{i} yaitu di {j['nama_lokasi']}, memerlukan perhatian khusus")
    else :
        print(f"{i} yaitu di {j['nama_lokasi']}, kondisi baik")

#7 Baris Baru
print("Hello World")