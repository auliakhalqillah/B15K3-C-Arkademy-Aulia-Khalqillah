# B15K3-C-Arkademy-Aulia-Khalqillah
Jawaban tes arkademy B15K3
# Dibutuhkan
- Python 3.6.5
- Library json untuk Python 3.6.5

JSON merupakan suatu format data sederhana yang digunakan untuk perturakan dan penyimpanan data. JSON dapat dibaca melalui beberapa bahasa pemrograman, seperti C,C++, Java, Javascript maupun Python. JSON terkadang juga diterapkan pada REST API (_Application Programming Interface_) yang digunakan untuk menerjemah komunikasi antara klien dengan server dengan lebih mudah ketika pertukaran dan penyimpanan data terjadi. 
# Instalasi JSON
Jika tidak terdapat _library_ JSON, anda dapat menginstallnya melalui terminal dengan mengetik perintah:
```
pip install simplejson
```
Jika tidak terdapat perintah _pip_, anda dapat menginstallnya dengan mengikuti tahap dari halaman berikut:
```
https://pip.pypa.io/en/stable/installing/
```
# Isi Repositori
Di dalam repositori ini terdapat lima file Python dan satu file JSON. Masing-masing file Python mewakili masing-masing jawaban dari soal-saoal yang diberikan. Sedangkan file JSON merupakan file keluaran dari file Python pada soal pertama (1.py). Kelima file Python tersebut adalah:
- 1.py
- 2.py
- 3.py
- 4.py
- 5.py

# Cara Menjalankan Program
### File 1.py
File 1.py merupakan program mengisi biodata yang kemudian hasilnya disimpan dalam format JSON. Untuk menjalankan file 1.py dapat dilakukan dengan perintah di bawah ini melalui terminal:
```
python3 1.py
```
kemudian tekan enter, maka akan muncul _input user_ melalui terminal seperti:
```
Name                            :jack
Age                             :24
Address                         :
....
....
```
hingga muncul hasil akhir dalam format JSON sebagai berikut:
```
{'name': 'jack', 'age': 24, 'address': 'Indonesia', 'hobbies': ['read'], 'married': 'NO', 'list_school': {'school': 'Indah Jaya', 'year_in': 2017, 'year_out': 2020, 'major': 'IPA'}, 'skills': [{'Matlab': 'Adva
nce'}], 'interest in coding': 'YES'}
```

### File 2.py
File 2.py merupakan program untuk memvalidasi _username_ dan _password_ yang diberikan melalui _input user_ dari terminal. Untuk menjalankan file ini dapat dilalukan dengan mengetik perintah berikut pada terminal:
```
python3 2.py
```
maka akan muncul perintah untuk memasukan _username_ dan _password_:
```
Username        :jok3r
Password        :T3pungB#3r4s!’
```
tekan enter maka akan muncul keterangan berupa:
```
Warning!!! The number is not allowed in username ['3']
Success! Password is good
```
Jika terdapat _Warning!_ maka _username_ atau _password_ harus diganti sesuai keterangan yang diberikan

### File 3.py
File 3.py merupaka program untuk menghitung banyak karakter yang diberikan. Untuk menjalankan file ini dapat dilakukan dengan mengetik perintah berikut pada terminal:
```
python3 3.py
```
tekan enter, maka akan muncul perintah:
```
Type the string                         :Victoria
What char do you want to find?          :i
```
tekan enter, maka akan muncul hasilnya berupa:
```
String          : Victoria
Char            : i
output          : 2
```
artinya _char i_ terdapat sebanyak 2 buah pada _string_ dari _Victoria_

### File 4.py
File 4.py merupakan program untuk memvalidasi kode warna melalui Hex Code. Untuk menjalankan file ini dapat dilakukan dengan mengetik perintah berikut pada terminal:
```
python3 4.py
```
tekan enter, maka akan muncul perintah untuk mengisi kode warna (format Hex Code):
```
Input Hex Number                :#F3F3F3
```
tekan enter, maka akan muncul keterangan:
```
Hex code is correct
```
Jika diberikan kode warna (Hex Code) yang salah, seperti #ezff8d maka akan muncul keterangan:
```
Input Hex Number                :#ezff8d
Hex code is not correct
```
Hal ini dikarenakan pada kode warna dibatasi kombinasi huruf dari A-F dan angka 0-9

### File 5.py
File 5.py merupakan program untuk menghitung profit dari harga saham sebuah PT.X setiap harinya. Dimana harga saham pertama misalnya `(10, 2, 11, 20, 3, 5)` untuk enam hari dan kedua `(33, 29, 11, 3)` untuk empat hari. Jika PT.X mendapatkan profit maka akan menghasilkan suatu nilai diatas 0 dan jika tidak mendapatkan profit maka profitnya sama dengan 0. Untuk menjalankan file ini dapat dilakukan dengan mengetik perintah berikut pada terminal (menggunakan saham pertama):
```
python3 5.py
```
tekan entar, maka akan menghasilkan profit sebesar `18`. Ketika dirubah menggunakan saham kedua, maka akan menghasilkan profit sama dengan `0` atau `Tidak bisa mendapatkan profit pada hari-hari ini`

# Catatan
Semua program yang dibuat dijalankan menggunakan Python 3.6.5 pada Mac OS El Capitan

# Sumber
- https://www.codepolitan.com/forum/thread/detail/115/hubungan-api-dengan-json-atau-serialize-di-php-dan-cara-penggunaannya-siapa-yang-lebih-unggul-dalam-penggunaannya
- https://id.wikipedia.org/wiki/Antarmuka_pemrograman_aplikasi
- https://stackoverflow.com/questions/1389141/how-to-add-json-library
- https://pip.pypa.io/en/stable/installing/


