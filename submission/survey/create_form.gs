function createSurvey() {
  const form = FormApp.create('Survei Pengalaman Kuliah dan Praktikum');
  form.setDescription(
    'Survei ini dibuat oleh tim mahasiswa untuk lomba STACK 2026. Tujuannya memahami pengalaman kamu di kuliah dan praktikum.\n\n' +
    'Survei ini anonim: kami tidak mencatat nama, NIM, atau email. Survei ini sukarela dan TIDAK memengaruhi nilai apa pun. ' +
    'Hasilnya hanya dilaporkan sebagai angka gabungan. Waktu pengisian sekitar 4 menit.'
  );
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setPublishingSummary(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Terima kasih sudah mengisi survei ini.');

  const scale = (title, low, high) =>
    form.addScaleItem().setTitle(title).setBounds(1, 5).setLabels(low, high).setRequired(true);
  const unsure = ['Sama sekali tidak yakin', 'Sangat yakin'];
  const likely = ['Sangat tidak mungkin', 'Sangat mungkin'];

  const a1 = form.addMultipleChoiceItem()
    .setTitle('A1. Apakah kamu mengikuti praktikum mata kuliah ini semester ini?')
    .setRequired(true);
  const latar = form.addPageBreakItem().setTitle('A. Latar');
  a1.setChoices([
    a1.createChoice('Ya', latar),
    a1.createChoice('Tidak', FormApp.PageNavigationType.SUBMIT),
  ]);

  form.addCheckboxItem()
    .setTitle('A2. Dalam bentuk apa kamu biasanya mengumpulkan kode praktikum?')
    .setHelpText('Boleh pilih lebih dari satu.')
    .setChoiceValues(['Screenshot kode di laporan', 'Link Google Colab', 'File notebook (.ipynb)'])
    .showOtherOption(true)
    .setRequired(true);

  form.addPageBreakItem().setTitle('B. Memahami kode sendiri');
  form.addMultipleChoiceItem()
    .setTitle('B1. Dalam 4 minggu terakhir, seberapa sering kamu mengumpulkan kode praktikum yang belum bisa kamu jelaskan baris demi baris?')
    .setChoiceValues(['Tidak pernah', '1 kali', '2-3 kali', 'Hampir setiap minggu'])
    .setRequired(true);
  scale('B2. Bayangkan asprak menunjuk satu baris acak di kode praktikum terakhirmu dan memintamu menjelaskan apa yang dilakukan baris itu. Seberapa yakin kamu bisa menjelaskannya?', ...unsure);
  form.addCheckboxItem()
    .setTitle('B3. Dari mana biasanya kode praktikummu berasal?')
    .setHelpText('Boleh pilih lebih dari satu.')
    .setChoiceValues([
      'Saya tulis sendiri dari awal',
      'Saya ubah dari contoh di modul',
      'Bantuan atau contoh dari teman',
      'Dibuat atau dibantu AI (ChatGPT, Gemini, dll.)',
      'Dari internet (StackOverflow, blog, dll.)',
    ])
    .showOtherOption(true);

  form.addPageBreakItem().setTitle('C. Bertanya saat kuliah');
  form.addMultipleChoiceItem()
    .setTitle('C1. Dalam 4 minggu terakhir, berapa kali kamu bingung saat kuliah tetapi tidak bertanya?')
    .setChoiceValues(['Tidak pernah', '1-2 kali', '3-5 kali', 'Lebih dari 5 kali'])
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('C2. Kalau kamu pernah tidak bertanya, apa alasannya?')
    .setHelpText('Boleh pilih lebih dari satu. Lewati jika tidak pernah.')
    .setChoiceValues([
      'Malu atau takut dianggap tidak paham',
      'Bingung cara merumuskan pertanyaan',
      'Tidak mau mengganggu jalannya kelas',
      'Menunggu bertanya ke teman setelah kelas',
      'Materinya terlalu cepat',
    ])
    .showOtherOption(true);
  scale('C3. Kalau kamu bisa bertanya tanpa nama kamu terlihat oleh teman sekelas, seberapa mungkin kamu akan lebih sering bertanya?', ...likely);

  form.addPageBreakItem().setTitle('D. Bantuan saat praktikum');
  form.addCheckboxItem()
    .setTitle('D1. Saat butuh bantuan asprak, apa yang biasanya kamu lakukan?')
    .setHelpText('Boleh pilih lebih dari satu.')
    .setChoiceValues([
      'Bertanya langsung saat praktikum',
      'Chat asprak lewat WhatsApp',
      'Bertanya ke teman saja',
      'Tidak meminta bantuan',
    ])
    .showOtherOption(true)
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('D2. Terakhir kali kamu meminta bantuan saat praktikum, kira-kira berapa lama kamu menunggu sebelum dibantu?')
    .setChoiceValues(['Kurang dari 5 menit', '5-10 menit', '10-20 menit', 'Lebih dari 20 menit', 'Saya belum pernah meminta bantuan'])
    .setRequired(true);
  scale('D3. Kalau ada jadwal asistensi yang bisa kamu pesan (online atau offline) di luar jam praktikum, seberapa mungkin kamu memakainya?', ...likely);

  form.addPageBreakItem().setTitle('E. Pendapat tentang ide');
  scale('E1. Setelah praktikum, seberapa mungkin kamu mengerjakan kuis singkat (sekitar 5 soal, 5 menit) tentang kode yang kamu tulis sendiri, jika hasilnya hanya untuk poin partisipasi dan kamu langsung melihat jawaban yang benar?', ...likely);
  form.addMultipleChoiceItem()
    .setTitle('E2. Apakah kamu keberatan mengunggah file notebook (.ipynb) sebagai pengganti screenshot kode?')
    .setChoiceValues(['Tidak keberatan', 'Agak keberatan', 'Keberatan'])
    .setRequired(true);
  form.addParagraphTextItem().setTitle('E3. (Opsional) Kalau keberatan, apa alasannya?');
  form.addParagraphTextItem().setTitle('E4. (Opsional) Apa yang paling menyulitkan kamu di kuliah atau praktikum mata kuliah ini?');

  Logger.log('Edit link: ' + form.getEditUrl());
  Logger.log('Link untuk disebar: ' + form.getPublishedUrl());
}