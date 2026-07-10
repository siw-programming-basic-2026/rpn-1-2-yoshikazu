# Cara Menerima Data dari File

## Tujuan

Dokumen ini menjelaskan cara membaca data dari file di Python dan memprosesnya baris demi baris.

Pada program kali ini, kita membaca ekspresi RPN (Reverse Polish Notation) dari file lalu menampilkan hasil perhitungannya.

---

## Input, Proses, dan Output

Secara umum, program berjalan dengan alur berikut.

```text
Input -> Proses -> Output
```

Poin utama kali ini adalah mengubah cara memasukkan input.

- Sebelumnya, ekspresi ditulis langsung di program atau dimasukkan dengan `input()`.
- Kali ini, ekspresi ditulis di file lalu dibaca oleh Python.

## File yang Digunakan

Sebagai contoh, gunakan struktur berikut.

```text
rpn_file_io/
├── run_rpn_file.py
├── rpn_calculator.py
├── expressions.txt
└── results.txt
```

Peran masing-masing file:

- `run_rpn_file.py`: Membaca file dan menjalankan perhitungan RPN
- `rpn_calculator.py`: Menyimpan fungsi untuk perhitungan RPN
- `expressions.txt`: File input untuk menulis ekspresi RPN
- `results.txt`: File output untuk menyimpan hasil perhitungan

### Contoh `expressions.txt`

```text
3 4 +
10 2 /
10 0 /
5 a +
3 4 5 +
```

Tulis satu ekspresi RPN di setiap baris.

`3 4 +` berarti `3 + 4` dalam notasi biasa.

## Bentuk Dasar Membuka File

Untuk membaca file di Python, gunakan `open()`.

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

Kode ini membuka `expressions.txt` lalu menampilkannya per baris.

### Arti `open()`

`open("expressions.txt", "r", encoding="utf-8")`

- `"expressions.txt"`: Nama file yang ingin dibuka
- `"r"`: Mode read (membaca)
- `encoding="utf-8"`: Pengaturan encoding karakter

### Mengapa Menggunakan `with`

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  ...
```

Dengan `with`, file akan tertutup otomatis setelah selesai digunakan.

Karena itu, umumnya file dibuka dengan `with open(...)`.

## Membaca Baris demi Baris

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

`for line in file:` akan mengambil isi file satu baris setiap iterasi.

Misalnya `expressions.txt` berisi:

```text
3 4 +
10 2 /
```

Maka `line` akan berisi nilai berikut secara berurutan.

- Iterasi 1: `"3 4 +\n"`
- Iterasi 2: `"10 2 /\n"`

## Menghapus Newline dengan `strip()`

Setiap baris yang dibaca dari file biasanya memiliki newline di akhir.

Karena itu, gunakan `strip()`.

```python
expression = line.strip()
```

Contoh:

```python
line = "3 4 +\n"
expression = line.strip()

print(expression)
```

Hasil:

```text
3 4 +
```

`strip()` menghapus spasi dan newline yang tidak diperlukan di awal/akhir teks.

## Menghitung Tiap Baris

Jika ada fungsi `calculate_rpn()`, ekspresi yang dibaca dari file bisa langsung diberikan ke fungsi tersebut.

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    expression = line.strip()

    if expression == "":
      continue

    result = calculate_rpn(expression)

    print(expression, "=>", result)
```

### Mengabaikan Baris Kosong

Jika file memiliki baris kosong, program bisa mencoba menghitung ekspresi kosong.

Karena itu tambahkan kondisi berikut.

```python
if expression == "":
  continue
```

Artinya: jika baris kosong, lewati dan lanjut ke baris berikutnya.

## Menulis Hasil ke File

Selain menampilkan di layar, hasil juga bisa disimpan ke file.

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as input_file:
  with open("results.txt", "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

### Perbedaan `print()` dan `write()`

```python
print(expression, "=>", result)
output_file.write(f"{expression} => {result}\n")
```

- `print()`: Menampilkan ke terminal
- `write()`: Menulis ke file

### Arti `\n`

`output_file.write(f"{expression} => {result}\n")`

`\n` di akhir berarti baris baru.

Jika tidak ditulis, semua hasil akan tersambung dalam satu baris.

## Mode Menulis

Saat menulis file, gunakan `"w"`.

```python
open("results.txt", "w", encoding="utf-8")
```

`"w"` berarti mode write.

Perhatian: `"w"` akan menimpa isi file setiap kali program dijalankan.

### Jika Ingin Menambahkan (Append)

Jika ingin mempertahankan hasil lama dan menambahkan di akhir, gunakan `"a"`.

```python
open("results.txt", "a", encoding="utf-8")
```

`"a"` berarti mode append.

Namun pada materi ini, kita memakai `"w"` agar hasil dibuat ulang setiap kali.

## Ringkasan

Poin penting pada materi ini:

- Membuka file dengan `open()`
- Gunakan `"r"` untuk mode baca
- Gunakan `"w"` untuk mode tulis
- Baca per baris dengan `for line in file:`
- Hapus newline dengan `strip()`
- Tulis ke file dengan `write()`
- Gunakan `\n` untuk pindah baris

## Contoh Lengkap

```python
from rpn_calculator import calculate_rpn

input_filename = "expressions.txt"
output_filename = "results.txt"

with open(input_filename, "r", encoding="utf-8") as input_file:
  with open(output_filename, "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

## Simpan Catatan di GitHub

Setelah perubahan pembacaan dari file selesai, simpan ke GitHub.

```bash
git status
git add .
git commit -m "Read RPN expressions from file"
git push
```

Jika ingin pesan commit dalam bahasa Jepang, ini juga boleh.

```bash
git commit -m "RPN式をファイルから読み込む"
```
