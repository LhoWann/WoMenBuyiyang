# Survei Praktikum (draf untuk Google Form)

Target: mahasiswa di dua kelas praktikum yang diasisteni Ridwan dan Dani (mata kuliah dan angkatan yang sama). Satu form yang sama untuk kedua kelas. Durasi sekitar 4 menit. Buka 23 Nov, tutup 26 Nov 2026 pukul 23:59.

## Pengaturan Google Form

- Collect email addresses: **Off**. Jangan ada pertanyaan nama, NIM, atau kelas.
- "Limit to 1 response" boleh dinyalakan. Responden harus login Google, tapi email mereka tidak terlihat oleh pemilik form.
- Kirim lewat ketua kelas atau grup kelas, bukan lewat chat pribadi dari asprak.
- Catat jumlah mahasiswa di kedua kelas yang menerima link, supaya response rate bisa dilaporkan (misalnya 41 dari 64).

## Teks pembuka

> Survei ini dibuat oleh tim mahasiswa untuk lomba STACK 2026. Tujuannya memahami pengalaman kamu di kuliah dan praktikum. Survei ini anonim: kami tidak mencatat nama, NIM, atau email. Survei ini sukarela dan **tidak memengaruhi nilai** apa pun. Hasilnya hanya dilaporkan sebagai angka gabungan. Waktu pengisian sekitar 4 menit.

## A. Latar

**A1.** Apakah kamu mengikuti praktikum mata kuliah ini semester ini? *(Ya / Tidak; jawaban Tidak langsung ke akhir form)*

**A2.** Dalam bentuk apa kamu biasanya mengumpulkan kode praktikum? *(boleh pilih lebih dari satu)*
- Screenshot kode di laporan
- Link Google Colab
- File notebook (.ipynb)
- Lainnya: ___

## B. Memahami kode sendiri

**B1.** Dalam 4 minggu terakhir, seberapa sering kamu mengumpulkan kode praktikum yang belum bisa kamu jelaskan baris demi baris?
- Tidak pernah
- 1 kali
- 2-3 kali
- Hampir setiap minggu

**B2.** Bayangkan asprak menunjuk satu baris acak di kode praktikum terakhirmu dan memintamu menjelaskan apa yang dilakukan baris itu. Seberapa yakin kamu bisa menjelaskannya?
*(Skala 1-5: 1 = sama sekali tidak yakin, 5 = sangat yakin)*

**B3.** Dari mana biasanya kode praktikummu berasal? *(boleh pilih lebih dari satu)*
- Saya tulis sendiri dari awal
- Saya ubah dari contoh di modul
- Bantuan atau contoh dari teman
- Dibuat atau dibantu AI (ChatGPT, Gemini, dll.)
- Dari internet (StackOverflow, blog, dll.)
- Lainnya: ___

## C. Bertanya saat kuliah

**C1.** Dalam 4 minggu terakhir, berapa kali kamu bingung saat kuliah tetapi tidak bertanya?
- Tidak pernah
- 1-2 kali
- 3-5 kali
- Lebih dari 5 kali

**C2.** Kalau kamu pernah tidak bertanya, apa alasannya? *(boleh pilih lebih dari satu)*
- Malu atau takut dianggap tidak paham
- Bingung cara merumuskan pertanyaan
- Tidak mau mengganggu jalannya kelas
- Menunggu bertanya ke teman setelah kelas
- Materinya terlalu cepat
- Lainnya: ___

**C3.** Kalau kamu bisa bertanya tanpa nama kamu terlihat oleh teman sekelas, seberapa mungkin kamu akan lebih sering bertanya?
*(Skala 1-5: 1 = sangat tidak mungkin, 5 = sangat mungkin)*

## D. Bantuan saat praktikum

**D1.** Saat butuh bantuan asprak, apa yang biasanya kamu lakukan? *(boleh pilih lebih dari satu)*
- Bertanya langsung saat praktikum
- Chat asprak lewat WhatsApp
- Bertanya ke teman saja
- Tidak meminta bantuan
- Lainnya: ___

**D2.** Terakhir kali kamu meminta bantuan saat praktikum, kira-kira berapa lama kamu menunggu sebelum dibantu?
- Kurang dari 5 menit
- 5-10 menit
- 10-20 menit
- Lebih dari 20 menit
- Saya belum pernah meminta bantuan

**D3.** Kalau ada jadwal asistensi yang bisa kamu pesan (online atau offline) di luar jam praktikum, seberapa mungkin kamu memakainya?
*(Skala 1-5)*

## E. Pendapat tentang ide

**E1.** Setelah praktikum, seberapa mungkin kamu mengerjakan kuis singkat (sekitar 5 soal, 5 menit) tentang kode yang kamu tulis sendiri, jika hasilnya hanya untuk poin partisipasi dan kamu langsung melihat jawaban yang benar?
*(Skala 1-5)*

**E2.** Apakah kamu keberatan mengunggah file notebook (.ipynb) sebagai pengganti screenshot kode?
- Tidak keberatan
- Agak keberatan
- Keberatan

**E3.** *(opsional)* Kalau keberatan, apa alasannya? ___

**E4.** *(opsional)* Apa yang paling menyulitkan kamu di kuliah atau praktikum mata kuliah ini? ___

## Pemetaan ke proposal

| Pertanyaan | Bagian proposal | Angka yang dilaporkan |
| --- | --- | --- |
| A2 | 2.3 Evidence | Persentase yang mengumpulkan kode hanya sebagai screenshot |
| B1, B2 | 2.3 Evidence, 6.1 Baseline | Persentase yang pernah mengumpulkan kode yang tidak bisa dijelaskan; rata-rata keyakinan |
| B3 | 2.1 Problem context | Sumber kode, terutama bantuan teman dan AI |
| C1, C2 | 2.3 Evidence | Persentase yang bingung tapi tidak bertanya, dan alasan teratas |
| C3 | 3.4 Features | Minat pada pertanyaan anonim |
| D1, D2, D3 | 2.3 Evidence, 3.2 Assist | Cara meminta bantuan, waktu tunggu, minat pada jadwal asistensi |
| E1, E2, E3 | 6.3 Risks | Kesediaan ikut kuis dan mengunggah notebook, beserta alasan keberatan |

## Cara melaporkan

- Tulis n (jumlah responden) dan response rate, misalnya "24 of 32 students (75%)".
- Laporkan semua hasil, termasuk yang tidak mendukung ide kita. Misalnya, kalau banyak yang keberatan upload notebook, masukkan ke tabel Risks.
- Jawaban terbuka hanya dikutip tanpa informasi yang bisa mengenali orangnya.