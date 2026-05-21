# Bagaimana Cara Agar Akun Kalian Muncul sebagai Kontributor?

Misalkan satu kelompok terdiri dari tiga mahasiswa: A, B dan C. Mahasiswa A berperan melakukan fork pada Repository yang sudah saya siapkan ini. Kemudian mahasiswa B dan C melakukan fork pada Repository mahasiswa A tersebut. 

## Langkah yang dilakukan oleh mahasiswa B dan C 
---

### Bagian 0: Melakukan *Fork* Repositori (Di Situs Web GitHub)

1. **Buka Halaman Repositori Mahasiswa A:** Akses proyek sumber.
Mahasiswa B harus masuk (*log in*) ke akun GitHub mereka, kemudian membuka tautan repositori milik Mahasiswa A yang ingin disalin.
*(Pastikan di pojok kiri atas halaman web tertulis `NamaAkunMahasiswaA / nama-repositori`)*.


2. **Klik Tombol Fork:** Inisiasi penyalinan.
Perhatikan pojok kanan atas halaman repositori tersebut. Di sebelah tombol *Star*, terdapat tombol bertuliskan **Fork**. Klik tombol **Fork** tersebut.


3. **Atur Opsi dan Buat Fork:** Konfirmasi kepemilikan.
GitHub akan mengarahkan Mahasiswa B ke halaman konfigurasi singkat (*Create a new fork*):

* **Owner:** Pastikan bagian ini otomatis terisi dengan nama akun GitHub milik Mahasiswa B sendiri.
* **Repository name:** Biarkan nama repositori tetap sama agar memudahkan pelacakan tugas.
* **Copy the main branch only:** Pastikan opsi ini dalam kondisi **tercentang** (secara default sudah tercentang).

Setelah itu, klik tombol hijau bertuliskan **Create fork** di bagian bawah.


---

> **Tanda Keberhasilan:**
> GitHub akan memproses penyalinan selama beberapa detik. Setelah selesai, halaman web akan otomatis dialihkan ke repositori baru. Mahasiswa B kini resmi memiliki ruang kerja sendiri jika di pojok kiri atas halaman telah berubah menjadi:
> `NamaAkunMahasiswaB / nama-repositori`
> *(disertai keterangan kecil di bawahnya: forked from NamaAkunMahasiswaA/nama-repositori)*.

Lanjutkan ke **Bagian 1**, yaitu memodifikasi file.

Jika Mahasiswa B menggunakan GitHub berbasis web secara penuh (tanpa menggunakan terminal di laptop), maka proses modifikasi file dilakukan langsung melalui peramban (*browser*).

Berikut adalah langkah-langkah terstruktur yang perlu dilakukan oleh Mahasiswa B di situs web GitHub sebelum mengajukan *Pull Request*:

---

### Bagian 1: Memodifikasi File dan Menyimpan Perubahan (Di Situs Web GitHub)

Mahasiswa B harus memperbarui isi repositori hasil *fork*-nya terlebih dahulu agar memiliki perbedaan materi yang akan diajukan ke Mahasiswa A.

1. **Buka Repositori Hasil Fork:** Navigasi ke proyek.
Mahasiswa B masuk ke akun GitHub miliknya, lalu membuka repositori yang merupakan hasil *fork* dari Mahasiswa A (pastikan nama repositori di pojok kiri atas tertulis `NamaAkunMahasiswaB/nama-repositori`).


2. **Edit atau Tambah File Baru:** Modifikasi materi.
* **Jika mengedit file yang sudah ada:** Klik pada file yang ingin diubah, lalu klik ikon **pensil (Edit this file)** di pojok kanan atas area teks.
* **Jika menambah file baru:** Klik tombol **Add file** di bagian kanan atas struktur direktori, lalu pilih **Create new file** (atau **Upload files** jika ingin mengunggah file dari komputer).


3. **Lakukan Commit Changes:** Menyimpan perubahan.
Setelah selesai menulis atau mengubah kode/teks, klik tombol **Commit changes...** di pojok kanan atas.

* Isi kotak **Commit message** dengan deskripsi singkat mengenai perubahan yang dilakukan (misalnya: *“Menyelesaikan tugas kalkulasi modul 2”*).
* Pastikan opsi yang terpilih adalah **Commit directly to the main branch**.
* Klik tombol **Commit changes** yang berwarna hijau.



---

Setelah Mahasiswa B menyelesaikan langkah **Commit changes** di atas, perubahan tersebut telah resmi tersimpan di akun GitHub miliknya secara daring. Langkah berikutnya bagi Mahasiswa B adalah melanjutkan ke proses **"4. Ajukan Pull Request"** seperti yang telah dijelaskan sebelumnya.


**4. Ajukan *Pull Request* (Di Situs Web GitHub)**

Sekarang, Mahasiswa B harus meminta secara eksplisit kepada Mahasiswa A untuk menerima hasil pekerjaannya:

* Mahasiswa B membuka halaman repositori miliknya sendiri di situs web GitHub.
* Mereka akan melihat *banner* di bagian atas yang menampilkan perubahan terbaru mereka. Kemudian, mereka mengklik tombol **Compare & pull request** yang berwarna hijau.
* Mereka memastikan bahwa *base repository* telah mengarah ke repositori milik Mahasiswa A, menulis catatan yang menjelaskan pengajuan mereka, lalu mengklik **Create pull request**.

### Bagian 2: Apa yang Harus Dilakukan oleh Mahasiswa A (Di Situs Web GitHub)

Pada saat ini, Mahasiswa B masih belum menjadi kontributor. Otoritas penuh kini beralih sepenuhnya kepada Mahasiswa A.

* Mahasiswa A membuka halaman repositorinya di GitHub dan mengklik tab **Pull requests**.
* Mereka mengklik *pull request* yang diajukan oleh Mahasiswa B untuk meninjau perubahan kode tersebut.
* Jika pekerjaan tersebut dinilai sudah baik, Mahasiswa A mengklik tombol **Merge pull request** yang berwarna hijau dan melakukan konfirmasi.

**Hasil Akhir**

Tepat pada saat Mahasiswa A mengklik tombol *Merge* tersebut, dua hal akan terjadi secara otomatis:

1. Kode dari Mahasiswa B langsung terintegrasi ke dalam riwayat proyek Mahasiswa A.
2. Profil Mahasiswa B secara otomatis muncul pada daftar "Contributors" di sisi kanan halaman utama repositori Mahasiswa A.

---

# Computational Physics: Applied Fast Fourier Transform (FFT)

Welcome to the comprehensive case study assignment on the Discrete Fourier Transform. In this assignment, you will apply the FFT algorithm to three distinct physical datasets to extract meaningful frequency-domain information.

## Objective
Your task is to complete the mathematical and computational analysis within the provided Jupyter Notebooks and publish your findings as a public web portfolio using GitHub Pages.

## Step-by-Step Instructions

### Step 1: Fork and Clone the Repository
1. Click the **Fork** button at the top right of this repository to create a copy under your own GitHub account.
2. Clone your forked repository to your local computational environment:
   `git clone https://github.com/YOUR-USERNAME/fft-case-studies-template.git`
3. Navigate into the directory:
   `cd fft-case-studies-template`

### Step 2: Set Up the Environment
Ensure you have the required Python libraries installed. It is highly recommended to use a virtual environment.
`pip install -r requirements.txt`

### Step 3: Conduct the Analysis
Navigate to the `notebooks/` directory. You will find three case studies. For each notebook, you must:
* Import the provided raw data from the `data/` folder.
* Compute the FFT using `numpy.fft` or `scipy.fft`.
* Plot the time-domain signal and the frequency-domain power spectrum.
* Provide written physical interpretations of your mathematical results using Markdown cells.

### Step 4: Compile to HTML
Once your analysis is complete and your notebooks are fully executed (ensure all plots are visible), you must compile them into static HTML files for web deployment. Run the following commands in your terminal:

`jupyter nbconvert --to html notebooks/Case_1_Astrophysics.ipynb --output-dir docs/`
`jupyter nbconvert --to html notebooks/Case_2_Climatology.ipynb --output-dir docs/`
`jupyter nbconvert --to html notebooks/Case_3_Acoustics.ipynb --output-dir docs/`

*Note: The `docs/index.html` file acts as your homepage and already contains links to these generated files.*

### Step 5: Deploy via GitHub Pages
1. Commit and push your changes back to your GitHub repository:
   `git add .`
   `git commit -m "Completed FFT analysis and compiled HTML"`
   `git push origin main`
2. On your GitHub repository page, navigate to **Settings** > **Pages**.
3. Under **Build and deployment**, set the Source to **Deploy from a branch**.
4. Select the **main** branch, and change the folder from `/(root)` to `/docs`.
5. Click **Save**. Within a few minutes, your computational portfolio will be live!

## Evaluation Criteria
Your submission will be evaluated on the following:
1. **Mathematical Accuracy:** Correct implementation of the FFT, proper normalization, and accurate formulation of the frequency bins (Nyquist limits).
2. **Computational Efficiency:** Clean, well-commented Python code without redundant loops.
3. **Scientific Communication:** The clarity of your data visualizations (labeled axes, correct units) and the depth of your written physical interpretations.

## Data Sources
*https://github.com/datasets/co2-ppm-daily/blob/main/data/co2-ppm-daily.csv*
*https://github.com/ThinamXx/TimeSeries_Sunspots/blob/master/sunspots.csv*
## Penggunaan Ai
Pada pengerjaan *case-based* ini, kami menggunakan:
1. **Gemini 3.1 Pro** untuk *generate* kode Python;
2. **Claude Sonnet 4.6** untuk mengidentifikasi referensi;

## Penggunaan Aplikasi Lain
1. **Jupyter Software** untuk ...
2. **Miniconda** untuk ....
