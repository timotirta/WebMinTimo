import random
punyaku = "ada,biasanya,hampir,kita,nanti,sekarang,terhadap,adalah,bisa,hanya,kurang,oleh,sekarang,terjadi,agak,boleh,harus,lagi,pada,sekitar,terlebih,agar,bolehkah,ikut,lain,pantas,selain,terus,akan,bukan,ingin,lalu,pasti,selalu,terutama,akhir,bukankah,ini,lebih,penting,selama,tetapi,aku,bukannya,itu,lima,per,selanjutnya,tidak,amat,cara,jadi,luar,perlu,seluruh,tiga,anda,cukup,jangan,maka,pernah,semasa,toh,antara,dahulu,jauh,malah,pertama,sementara,tunjuk,apa,dalam,jelas,malahan,pula,semua,turut,apakah,dan,jelaslah,mampu,pun,semuanya,untuk,apalagi,dapat,jika,mana,punya,sendiri,waktu,atas,dari,juga,masih,saat,sepanjang,walau,atau,daripada,kalau,masing-masing,saja,seperlunya,walaupun,bagaimana,datang,kami,mau,sama,seperti,yakin,bagaimanakah,dekat,kamu,melainkan,sambil,sering,yang,bagaimanapun,demikian,kapan,melakukan,sampai,serta,bagian,dengan,kapankah,melalui,sangat,seseorang,bahwa,di,kapanpun,melihat,satu,sesuatu,baik,dia,karena,memberi,saya,sesudah,bakal,diantara,kata,menanyakan,sebab,setelah,banyak,diantaranya,katanya,mendapat,sebagai,setiap,baru,diberi,ke,mendapatkan,sebagian,setidaknya,bawah,diberikan,kecil,mengapa,sebelum,siapa,beberapa,didapat,kedua,mengenai,sebelumnya,siapakah,belakang,digunakan,keduanya,mengetahui,sebenarnya,siapapun,belakangan,dijelaskan,keinginan,menggunakan,sebetulnya,sudah,benar,diketahui,kelihatan,menjadi,sebuah,tahu,berbagai,dilakukan,kelihatannya,menuju,sebut,tambah,beri,dilihat,kelima,menunjukkan,secara,tampak,berikut,diri,keluar,menurut,sedang,tanpa,berikutnya,disebut,kembali,menyatakan,sedikit,tanya,bermacam,disebutkan,kemudian,menyebutkan,sedikitnya,tapi,bermacam-macam,disini,kemungkinan,mereka,segera,telah,bersama,ditunjukkan,kenapa,meski,seharusnya,tempat,bertanya,dua,keseluruhan,meskipun,sejak,tentang,besar,dulu,ketika,minta,sejauh,tentu,betul,empat,khususnya,mungkin,sekali,tepat,biasa,guna,kira-kira,namun,sekalipun,terakhir"
punyaku = punyaku.split(',')
punyakubaru = []
for x in punyaku:
	punyakubaru.append(x)

stop1 = "abad , acara , aceh , ada , adalah , adanya , adapun , agak , agaknya , agama , agar , agustus , air , akan , akankah , akhir , akhiri , akhirnya , akibat , aku , akulah , alam , album , amat , amatlah , amerika , anak , and , anda , andalah , anggota , antar , antara , antarabangsa , antaranya , apa , apaan , apabila , apakah , apalagi , apatah , api , april , artikel , artinya , as , asal , asalkan , asas , asia , asing , atas , atau , ataukah , ataupun , australia , awal , awalnya , awam , b , badan , bagai , bagaikan , bagaimana , bagaimanakah , bagaimanapun , bagainamakah , bagi , bagian , bahagian , bahan , baharu , bahasa , bahawa , bahkan , bahwa , bahwasannya , bahwasanya , baik , baiknya , bakal , bakalan , balik , bandar , bangsa , bank , banyak , bapak , barang , barangan , barat , baru , baru-baru , bawah , beberapa , begini , beginian , beginikah , beginilah , begitu , begitukah , begitulah , begitupun , bekas , bekerja , belakang , belakangan , belanda , beli , beliau , belum , belumlah , benar , benarkah , benarlah , bentuk , berada , berakhir , berakhirlah , berakhirnya , berapa , berapakah , berapalah , berapapun , berarti , berasal , berat , berawal , berbagai , berbanding , berbeda , berdasarkan , berdatangan , berharap , berhasil , beri , berikan , berikut , berikutan , berikutnya , berita , berjalan , berjaya , berjumlah , berkaitan , berkali , berkali-kali , berkata , berkehendak , berkeinginan , berkenaan , berlainan , berlaku , berlalu , berlangsung , berlebihan , bermacam , bermacam-macam , bermain , bermaksud , bermula , bernama , bernilai , bersama , bersama-sama , bersiap , bertanya , bertemu , berturut , bertutur , berubah , berujar , berupa , besar , besok , betul , betulkah , bhd , biasa , biasanya , bidang , bila , bilakah , bilion , bintang , bisa , bisakah , blog , bn , bola , boleh , bolehkah , bolehlah , buat , bukan , bukankah , bukanlah , bukannya , buku , bulan , bumi , bung , bursa , cadangan , cara , caranya , catch , china , click , code , copyright , cukup , cukupkah , cukuplah , cuma , daerah , dagangan , dahulu , dalam , dan , dana , dapat , dari , daripada , dasar , data , datang , datuk , dekat , demi , demikian , demikianlah , dengan , depan , derivatives , desa , desember , detik , dewan , di , dia , diadakan , diakhiri , diakhirinya , dialah , dianggap , diantara , diantaranya , diberi , diberikan , diberikannya , dibuat , dibuatnya , dibuka , dicatatkan , didapat , didatangkan , didirikan , diduga , digunakan , diibaratkan , diibaratkannya , diingat , diingatkan , diinginkan , dijangka , dijawab , dijelaskan , dijelaskannya , dikarenakan , dikatakan , dikatakannya , dikenal , dikerjakan , diketahui , diketahuinya , dikira , dilakukan , dilalui , dilihat , dimaksud , dimaksudkan , dimaksudkannya , dimaksudnya , dimana , diminta , dimintai , dimisalkan , dimulai , dimulailah , dimulainya , dimungkinkan , dini , diniagakan , dipastikan , diperbuat , diperbuatnya , dipergunakan , diperkirakan , diperlihatkan , diperlukan , diperlukannya , dipersoalkan , dipertanyakan , dipunyai , diri , dirilis , dirinya , dis , disampaikan , disebut , disebutkan , disebutkannya , disember , disini , disinilah , distrik , ditambahkan , ditandaskan , ditanya , ditanyai , ditanyakan , ditegaskan , ditemukan , ditujukan , ditunjuk , ditunjuki , ditunjukkan , ditunjukkannya , ditunjuknya , ditutup , dituturkan , dituturkannya , diucapkan , diucapkannya , diungkapkan , document.write , dolar , dong , dr , dua , dulu , dunia , effective , ekonomi , eksekutif , eksport , empat , enam , enggak , enggaknya , entah , entahlah , era , eropa , err , faedah , feb , film , gat , gedung , gelar , gettracker , global , grup , guna , gunakan , gunung , hadap , hadapan , hal , hampir , hanya , hanyalah , harga , hari , harian , harus , haruslah , harusnya , hasil , hendak , hendaklah , hendaknya , hidup , hingga , https , hubungan , hukum , hutan , i , ia , iaitu , ialah , ibarat , ibaratkan , ibaratnya , ibu , ii , iklan , ikut , ilmu , indeks , india , indonesia , industri , informasi , ingat , inggris , ingin , inginkah , inginkan , ini , inikah , inilah , internasional , islam , isnin , isu , italia , itu , itukah , itulah , jabatan , jadi , jadilah , jadinya , jakarta , jalan , jalur , jaman , jan , jangan , jangankan , janganlah , januari , jauh , jawa , jawab , jawaban , jawabnya , jawatan , jawatankuasa , jelas , jelaskan , jelaslah , jelasnya , jenis , jepang , jepun , jerman , jika , jikalau , jiwa , jual , jualan , juga , julai , jumaat , jumat , jumlah , jumlahnya , jun , juni , justru , juta , kabar , kabupaten , kadar , kala , kalangan , kalau , kalaulah , kalaupun , kali , kalian , kalimantan , kami , kamilah , kamis , kamu , kamulah , kan , kantor , kapal , kapan , kapankah , kapanpun , karena , karenanya , karya , kasus , kata , katakan , katakanlah , katanya , kaunter , kawasan , ke , keadaan , kebetulan , kebutuhan , kecamatan , kecil , kedua , kedua-dua , keduanya , kedudukan , kegiatan , kehidupan , keinginan , kejadian , kekal , kelamaan , kelihatan , kelihatannya , kelima , kelompok , keluar , keluarga , kelurahan , kembali , kementerian , kemudahan , kemudian , kemungkinan , kemungkinannya , kenaikan , kenapa , kenyataan , kepada , kepadanya , kepala , kepentingan , keputusan , kerajaan , kerana , kereta , kerja , kerjasama , kes , kesampaian , keselamatan , keseluruhan , keseluruhannya , kesempatan , kesihatan , keterangan , keterlaluan , ketiga , ketika , ketua , keuntungan , kewangan , khamis , khusus , khususnya , kini , kinilah , kira , kira-kira , kiranya , kita , kitalah , klci , klibor , klik , km , kok , komentar , kompas , komposit , kondisi , kontrak , korban , korea , kos , kota , kuala , kuasa , kukuh , kumpulan , kurang , kurangnya , lagi , lagian , lagu , lah , lain , lainnya , laku , lalu , lama , lamanya , langkah , langsung , lanjut , lanjutnya , laporan , laut , lebih , lembaga , lepas , lewat , lima , lingkungan , login , lokasi , lot , luar , luas , lumpur , mac , macam , mahkamah , mahu , majlis , maka , makanan , makanya , makin , maklumat , malah , malahan , malam , malaysia , mampu , mampukah , mana , manakala , manalagi , mantan , manusia , masa , masalah , masalahnya , masih , masihkah , masing , masing-masing , masuk , masyarakat , mata , mau , maupun , measure , media , mei , melainkan , melakukan , melalui , melawan , melihat , melihatnya , memandangkan , memang , memastikan , membantu , membawa , memberi , memberikan , membolehkan , membuat , memerlukan , memihak , memiliki , meminta , memintakan , memisalkan , memperbuat , mempergunakan , memperkirakan , memperlihatkan , mempersiapkan , mempersoalkan , mempertanyakan , mempunyai , memulai , memungkinkan , menaiki , menambah , menambahkan , menandaskan , menanti , menantikan , menanya , menanyai , menanyakan , menarik , menawarkan , mencapai , mencari , mencatatkan , mendapat , mendapatkan , mendatang , mendatangi , mendatangkan , menegaskan , menerima , menerusi , mengadakan , mengakhiri , mengaku , mengalami , mengambil , mengapa , mengatakan , mengatakannya , mengenai , mengerjakan , mengetahui , menggalakkan , menggunakan , menghadapi , menghendaki , mengibaratkan , mengibaratkannya , mengikut , mengingat , mengingatkan , menginginkan , mengira , mengucapkan , mengucapkannya , mengumumkan , mengungkapkan , mengurangkan , meninggal , meningkat , meningkatkan , menjadi , menjalani , menjawab , menjelang , menjelaskan , menokok , menteri , menuju , menunjuk , menunjuki , menunjukkan , menunjuknya , menurut , menuturkan , menyaksikan , menyampaikan , menyangkut , menyatakan , menyebabkan , menyebutkan , menyediakan , menyeluruh , menyiapkan , merasa , mereka , merekalah , merosot , merupakan , meski , meskipun , mesyuarat , metrotv , meyakini , meyakinkan , milik , militer , minat , minggu , minta , minyak , mirip , misal , misalkan , misalnya , mobil , modal , mohd , mudah , mula , mulai , mulailah , mulanya , muncul , mungkin , mungkinkah , musik , musim , nah , naik , nama , namun , nanti , nantinya , nasional , negara , negara-negara , negeri , new , niaga , nilai , nomor , noun , nov , november , numeral , numeralia , nya , nyaris , nyatanya , of , ogos , okt , oktober , olah , oleh , olehnya , operasi , orang , organisasi , pada , padahal , padanya , pagetracker , pagi , pak , paling , pameran , panjang , pantas , papan , para , paras , parlimen , partai , parti , particle , pasar , pasaran , password , pasti , pastilah , pasukan , paticle , pegawai , pejabat , pekan , pekerja , pelabur , pelaburan , pelancongan , pelanggan , pelbagai , peluang , pemain , pembangunan , pemberita , pembinaan , pemerintah , pemerintahan , pemimpin , pendapatan , pendidikan , penduduk , penerbangan , pengarah , pengeluaran , pengerusi , pengguna , penggunaan , pengurusan , peniaga , peningkatan , penting , pentingnya , per , perancis , perang , peratus , percuma , perdagangan , perdana , peringkat , perjanjian , perkara , perkhidmatan , perladangan , perlu , perlukah , perlunya , permintaan , pernah , perniagaan , persekutuan , persen , persidangan , persoalan , pertama , pertandingan , pertanyaan , pertanyakan , pertubuhan , pertumbuhan , perubahan , perusahaan , pesawat , peserta , petang , pihak , pihaknya , pilihan , pinjaman , polis , polisi , politik , pos , posisi , presiden , prestasi , produk , program , projek , pronomia , pronoun , proses , proton , provinsi , pt , pubdate , pukul , pula , pulau , pun , punya , pusat , rabu , radio , raja , rakan , rakyat , ramai , rantau , rasa , rasanya , rata , raya , rendah , republik , resmi , ribu , ringgit , root , ruang , rumah , rupa , rupanya , saat , saatnya , sabah , sabtu , sahaja , saham , saja , sajalah , sakit , salah , saling , sama , sama-sama , sambil , sampai , sampaikan , sana , sangat , sangatlah , sarawak , satu , sawit , saya , sayalah , sdn , se , sebab , sebabnya , sebagai , sebagaimana , sebagainya , sebagian , sebahagian , sebaik , sebaiknya , sebaliknya , sebanyak , sebarang , sebegini , sebegitu , sebelah , sebelum , sebelumnya , sebenarnya , seberapa , sebesar , sebetulnya , sebisanya , sebuah , sebut , sebutlah , sebutnya , secara , secukupnya , sedang , sedangkan , sedemikian , sedikit , sedikitnya , seenaknya , segala , segalanya , segera , segi , seharusnya , sehingga , seingat , sejak , sejarah , sejauh , sejenak , sejumlah , sekadar , sekadarnya , sekali , sekali-kali , sekalian , sekaligus , sekalipun , sekarang , sekaranglah , sekecil , seketika , sekiranya , sekitar , sekitarnya , sekolah , sektor , sekurang , sekurangnya , sekuriti , sela , selagi , selain , selaku , selalu , selama , selama-lamanya , selamanya , selanjutnya , selasa , selatan , selepas , seluruh , seluruhnya , semacam , semakin , semalam , semampu , semampunya , semasa , semasih , semata , semaunya , sementara , semisal , semisalnya , sempat , semua , semuanya , semula , sen , sendiri , sendirian , sendirinya , senin , seolah , seolah-olah , seorang , sepak , sepanjang , sepantasnya , sepantasnyalah , seperlunya , seperti , sepertinya , sepihak , sept , september , serangan , serantau , seri , serikat , sering , seringnya , serta , serupa , sesaat , sesama , sesampai , sesegera , sesekali , seseorang , sesi , sesuai , sesuatu , sesuatunya , sesudah , sesudahnya , setelah , setempat , setengah , seterusnya , setiap , setiausaha , setiba , setibanya , setidak , setidaknya , setinggi , seusai , sewaktu , siap , siapa , siapakah , siapapun , siaran , sidang , singapura , sini , sinilah , sistem , soal , soalnya , sokongan , sri , stasiun , suara , suatu , sudah , sudahkah , sudahlah , sukan , suku , sumber , sungai , supaya , surat , susut , syarikat , syed , tadi , tadinya , tahap , tahu , tahun , tak , tama , tambah , tambahnya , tampak , tampaknya , tampil , tan , tanah , tandas , tandasnya , tanggal , tanpa , tanya , tanyakan , tanyanya , tapi , tawaran , tegas , tegasnya , teknologi , telah , televisi , teman , tempat , tempatan , tempo , tempoh , tenaga , tengah , tentang , tentara , tentu , tentulah , tentunya , tepat , terakhir , terasa , terbaik , terbang , terbanyak , terbesar , terbuka , terdahulu , terdapat , terdiri , terhadap , terhadapnya , teringat , terjadi , terjadilah , terjadinya , terkait , terkenal , terkira , terlalu , terlebih , terletak , terlihat , termasuk , ternyata , tersampaikan , tersebut , tersebutlah , tertentu , tertuju , terus , terutama , testimoni , testimony , tetap , tetapi , the , tiada , tiap , tiba , tidak , tidakkah , tidaklah , tidaknya , tiga , tim , timbalan , timur , tindakan , tinggal , tinggi , tingkat , toh , tokoh , try , tun , tunai , tunjuk , turun , turut , tutur , tuturnya , tv , uang , ucap , ucapnya , udara , ujar , ujarnya , umum , umumnya , unescape , ungkap , ungkapnya , unit , universitas , untuk , untung , upaya , urus , usah , usaha , usai , user , utama , utara , var , versi , waduh , wah , wahai , wakil , waktu , waktunya , walau , walaupun , wang , wanita , warga , warta , wib , wilayah , wong , word , ya , yaitu , yakin , yakni , yang , zaman"
stop1 = stop1.split(' , ')
stop2 = "acuh , ada , adalah , adil , agak , agar , akal , akan , akhir , akhir-akhir , akibat , akibatnya , aku , amat , ambil , anda , antara , antri , anu , apa , apakah , apalagi , apapun , asumsinya , atas , atau , ayo , ayolah , bagaimana , bagaimanakah , bagaimanapun , bagian , bagus , bahwa , baik , bakal , banyak , baru , bawah , beberapa , beda , bekas , belakang , belakangan , benar , berbagai , berbeda , bergaul , berguna , berharga , berhubungan , beri , berikut , berikutnya , berlawanan , bermacam , bermacam-macam , berpikir , bersama , berserta , bertanya , bertentangan , berturut-turut , besar , betul , biar , biarkan , biarlah , biarpun , biasa , biasanya , bilang , bisa , boleh , bolehkah , bukan , bukankah , bukannya , cara , cenderung , coba , cocok , com , contoh , contohnya , cukup , cv , dahulu , dalam , dan , dapat , dapatkah , dari , darimana , daripada , data , datang , dekat , delapan , demikian , dengan , deskripsi , deskripsinya , detik , di , dia , diacuhkan , diambil , diambilnya , diantara , diantaranya , diasosiasikan , diatas , dibawah , dibelakang , dibelakangnya , diberi , diberikan , dibolehkan , dicoba , didalam , didapat , didapati , dideskripsikan , digunakan , dihargai , diikuti , diindikasikan , dijelaskan , dikenal , diketahui , dikirim , dilain , dilakukan , dilihat , diluar , dimana , dimanakah , dimanapun , dinyatakan , diperbolehkan , diperoleh , dipertimbangkan , diri , diriku , dirimu , disamping , disebabkan , disebelah , disebut , disebutkan , disekitarnya , disenangi , disimpan , disimpannya , disini , disukai , ditaruh , ditempat , ditengah , ditengah-tengah , ditolong , ditunjukkan , diusulkan , dll , dsb , dua , dulu , dulunya , edu , eks , empat , enam , ganti , guna , hai , hak , halo , hampir , hanya , harap , harga , hargai , harus , hello , heran , hirau , hormat , ikut , indikasi , ingin , ini , itu , jadi , jahat , jalan , jangan , jarang , jauh , jelas , jelaslah , jelek , jeleknya , jika , juga , kadang-kadang , kalau , kalau-kalau , kali , kami , kamu , kanan , kandungan , kapan , kapankah , kapanpun , karena , kasih , kata , katanya , kau , kayak , ke , kebanyakan , kecil , kecuali , kedalam , kedua , keduanya , keempat , keinginan , kelihatan , kelihatannya , kelima , keluar , kemana , kemari , kembali , kemudian , kemungkinan , kenal , kenapa , kepentingan , kepercayaan , keperluan , kepunyaan , kepunyaannya , kesana-kemari , kesana-sini , keseluruhan , kesini , ketiga , ketika , khusus , khususnya , kira-kira , kiri , kirim , kita , konsekuensi , konsekuensinya , kosong , kuat , kurang , lagi , lain , lain-lain , lalu , lantaran , lawan , lebih , lihat , lima , lintas , luar , maaf , maka , makhluk , malah , malahan , mampu , mana , manakah , mari , marilah , masih , masing-masing , masuk , mati , mau , melainkan , melakukan , melalui , melawan , melebihi , melihat , memadai , memberi , membolehkan , memikir , memiliki , memperbolehkan , memperhatikan , mempertimbangkan , menanyakan , mencoba , mendapat , mendapatkan , mengambil , mengandung , mengapa , mengapakah , mengenai , mengenal , mengetahui , menggunakan , menghargai , menghiraukan , mengikuti , mengirim , mengizinkan , mengusulkan , menjadi , menolong , menuju , menunjukkan , menurut , menyatakan , menyebabkan , menyebutkan , menyediakan , menyenangi , menyenangkan , menyimpan , menyukai , mereka , meski , meskipun , milik , milikku , milikmu , miliknya , minta , moga-moga , mudah-mudahan , mungkin , nama , nampak , namun , nanti , nggak , nol , normalnya , novel , oh , ok , okay , oke , oleh , orang , p , p.t. , pada , padam , pantas , pasti , peduli , pengetahuan , penting , penyebab , per , perbedaan , percaya , pergantian , pergi , perkataan , perlu , permintaan , pernah , persis , pertama , perubahan , pikir , plus , pribadi , pt , pula , pun , punya , relatif , rubah , saat , sadis , saja , salam , sama , sambil , sampai , samping , sangat , satu , saya , sayang , sayangnya , sebab , sebagai , sebagian , sebelah , sebelum , sebelumnya , sebenarnya , sebetulnya , sebiji , sebongkah , sebuah , sebungkus , sebut , sebutir , secara , secepatnya , sedang , sedia , sedikit , sedikitnya , seekor , segera , seharusnya , sehelai , sejak , sejauh , sejujurnya , sekali , sekalipun , sekarang , sekeliling , sekitar , selain , selalu , selama , selamat , selanjutnya , selembar , seluruh , semasa , sembilan , semenjak , sementara , semoga , semua , semuanya , senang , senantiasa , sendiri , sepanjang , seperlunya , seperti , sepiring , sering , serius , serta , seseorang , sesuai , sesuatu , sesudah , sesunguhnya , setelah , setiap , setidaknya , sewajarnya , sewaktu-waktu , sial , sialnya , siapa , siapakah , siapapun , simpan , singkat , spesifik , sub , sudah , suka , sungguh , sungguh-sungguh , sungguhpun , tahu , tambah , tampak , tanpa , tanya , tapi , telah , teliti , tempat , tentang , tentu , tepat , terakhir , terbaik , terhadap , terima , terjadi , terkenal , terlebih , terlepas , tersedia , tertulis , terus , terutama , tetapi , tidak , tiga , timbang , toh , tolong , tua , tujuh , tunjuk , turun , turut , untuk , utama , wajar , waktu , walau , walaupun , ya , yakin , yang"
stop2 = stop2.split(' , ')
stop3 = "ada,begini,berujar,diibaratkan,ditujukan,jangankan,kesampaian,adalah,beginian,berupa,diibaratkannya,ditunjuk,janganlah,keseluruhan,adanya,beginikah,besar,diingat,ditunjuki,jauh,keseluruhannya,adapun,beginilah,betul,diingatkan,ditunjukkan,jawab,keterlaluan,agak,begitu,betulkah,diinginkan,ditunjukkannya,jawaban,ketika,agaknya,begitukah,biasa,dijawab,ditunjuknya,jawabnya,khususnya,agar,begitulah,biasanya,dijelaskan,dituturkan,jelas,kini,akan,begitupun,bila,dijelaskannya,dituturkannya,jelaskan,kinilah,akankah,bekerja,bilakah,dikarenakan,diucapkan,jelaslah,kira,akhir,belakang,bisa,dikatakan,diucapkannya,jelasnya,kira-kira,akhiri,belakangan,bisakah,dikatakannya,diungkapkan,jika,kiranya,akhirnya,belum,boleh,dikerjakan,dong,jikalau,kita,aku,belumlah,bolehkah,diketahui,dua,juga,kitalah,akulah,benar,bolehlah,diketahuinya,dulu,jumlah,kok,amat,benarkah,buat,dikira,empat,jumlahnya,kurang,amatlah,benarlah,bukan,dilakukan,enggak,justru,lagi,anda,berada,bukankah,dilalui,enggaknya,kala,lagian,andalah,berakhir,bukanlah,dilihat,entah,kalau,lah,antar,berakhirlah,bukannya,dimaksud,entahlah,kalaulah,lain,antara,berakhirnya,bulan,dimaksudkan,guna,kalaupun,lainnya,antaranya,berapa,bung,dimaksudkannya,gunakan,kalian,lalu,apa,berapakah,cara,dimaksudnya,hal,kami,lama,apaan,berapalah,caranya,diminta,hampir,kamilah,lamanya,apabila,berapapun,cukup,dimintai,hanya,kamu,lanjut,apakah,berarti,cukupkah,dimisalkan,hanyalah,kamulah,lanjutnya,apalagi,berawal,cukuplah,dimulai,hari,kan,lebih,apatah,berbagai,cuma,dimulailah,harus,kapan,lewat,artinya,berdatangan,dahulu,dimulainya,haruslah,kapankah,lima,asal,beri,dalam,dimungkinkan,harusnya,kapanpun,luar,asalkan,berikan,dan,dini,hendak,karena,macam,atas,berikut,dapat,dipastikan,hendaklah,karenanya,maka,atau,berikutnya,dari,diperbuat,hendaknya,kasus,makanya,ataukah,berjumlah,daripada,diperbuatnya,hingga,kata,makin,ataupun,berkali-kali,datang,dipergunakan,ia,katakan,malah,awal,berkata,dekat,diperkirakan,ialah,katakanlah,malahan,awalnya,berkehendak,demi,diperlihatkan,ibarat,katanya,mampu,bagai,berkeinginan,demikian,diperlukan,ibaratkan,ke,mampukah,bagaikan,berkenaan,demikianlah,diperlukannya,ibaratnya,keadaan,mana,bagaimana,berlainan,dengan,dipersoalkan,ibu,kebetulan,manakala,bagaimanakah,berlalu,depan,dipertanyakan,ikut,kecil,manalagi,bagaimanapun,berlangsung,di,dipunyai,ingat,kedua,masa,bagi,berlebihan,dia,diri,ingat-ingat,keduanya,masalah,bagian,bermacam,diakhiri,dirinya,ingin,keinginan,masalahnya,bahkan,bermacam-macam,diakhirinya,disampaikan,inginkah,kelamaan,masih,bahwa,bermaksud,dialah,disebut,inginkan,kelihatan,masihkah,bahwasanya,bermula,diantara,disebutkan,ini,kelihatannya,masing,baik,bersama,diantaranya,disebutkannya,inikah,kelima,masing-masing,bakal,bersama-sama,diberi,disini,inilah,keluar,mau,bakalan,bersiap,diberikan,disinilah,itu,kembali,maupun,balik,bersiap-siap,diberikannya,ditambahkan,itukah,kemudian,melainkan,banyak,bertanya,dibuat,ditandaskan,itulah,kemungkinan,melakukan,bapak,bertanya-tanya,dibuatnya,ditanya,jadi,kemungkinannya,melalui,baru,berturut,didapat,ditanyai,jadilah,kenapa,melihat,bawah,berturut-turut,didatangkan,ditanyakan,jadinya,kepada,melihatnya,beberapa,bertutur,digunakan,ditegaskan,jangan,kepadanya,memang,memastikan,menuju,perlu,sebetulnya,semasih,sinilah,tersebutlah,memberi,menunjuk,perlukah,sebisanya,semata,soal,tertentu,memberikan,menunjuki,perlunya,sebuah,semata-mata,soalnya,tertuju,membuat,menunjukkan,pernah,sebut,semaunya,suatu,terus,memerlukan,menunjuknya,persoalan,sebutlah,sementara,sudah,terutama,memihak,menurut,pertama,sebutnya,semisal,sudahkah,tetap,meminta,menuturkan,pertama-tama,secara,semisalnya,sudahlah,tetapi,memintakan,menyampaikan,pertanyaan,secukupnya,sempat,supaya,tiap,memisalkan,menyangkut,pertanyakan,sedang,semua,tadi,tiba,memperbuat,menyatakan,pihak,sedangkan,semuanya,tadinya,tiba-tiba,mempergunakan,menyebutkan,pihaknya,sedemikian,semula,tahu,tidak,memperkirakan,menyeluruh,pukul,sedikit,sendiri,tahun,tidakkah,memperlihatkan,menyiapkan,pula,sedikitnya,sendirian,tak,tidaklah,mempersiapkan,merasa,pun,seenaknya,sendirinya,tambah,tiga,mempersoalkan,mereka,punya,segala,seolah,tambahnya,tinggi,mempertanyakan,merekalah,rasa,segalanya,seolah-olah,tampak,toh,mempunyai,merupakan,rasanya,segera,seorang,tampaknya,tunjuk,memulai,meski,rata,seharusnya,sepanjang,tandas,turut,memungkinkan,meskipun,rupanya,sehingga,sepantasnya,tandasnya,tutur,menaiki,meyakini,saat,seingat,sepantasnyalah,tanpa,tuturnya,menambahkan,meyakinkan,saatnya,sejak,seperlunya,tanya,ucap,menandaskan,minta,saja,sejauh,seperti,tanyakan,ucapnya,menanti,mirip,sajalah,sejenak,sepertinya,tanyanya,ujar,menanti-nanti,misal,saling,sejumlah,sepihak,tapi,ujarnya,menantikan,misalkan,sama,sekadar,sering,tegas,umum,menanya,misalnya,sama-sama,sekadarnya,seringnya,tegasnya,umumnya,menanyai,mula,sambil,sekali,serta,telah,ungkap,menanyakan,mulai,sampai,sekali-kali,serupa,tempat,ungkapnya,mendapat,mulailah,sampai-sampai,sekalian,sesaat,tengah,untuk,mendapatkan,mulanya,sampaikan,sekaligus,sesama,tentang,usah,mendatang,mungkin,sana,sekalipun,sesampai,tentu,usai,mendatangi,mungkinkah,sangat,sekarang,sesegera,tentulah,waduh,mendatangkan,nah,sangatlah,sekarang,sesekali,tentunya,wah,menegaskan,naik,satu,sekecil,seseorang,tepat,wahai,mengakhiri,namun,saya,seketika,sesuatu,terakhir,waktu,mengapa,nanti,sayalah,sekiranya,sesuatunya,terasa,waktunya,mengatakan,nantinya,se,sekitar,sesudah,terbanyak,walau,mengatakannya,nyaris,sebab,sekitarnya,sesudahnya,terdahulu,walaupun,mengenai,nyatanya,sebabnya,sekurang-kurangnya,setelah,terdapat,wong,mengerjakan,oleh,sebagai,sekurangnya,setempat,terdiri,yaitu,mengetahui,olehnya,sebagaimana,sela,setengah,terhadap,yakin,menggunakan,pada,sebagainya,selain,seterusnya,terhadapnya,yakni,menghendaki,padahal,sebagian,selaku,setiap,teringat,yang,mengibaratkan,padanya,sebaik,selalu,setiba,teringat-ingat,mengibaratkannya,pak,sebaik-baiknya,selama,setibanya,terjadi,mengingat,paling,sebaiknya,selama-lamanya,setidak-tidaknya,terjadilah,mengingatkan,panjang,sebaliknya,selamanya,setidaknya,terjadinya,menginginkan,pantas,sebanyak,selanjutnya,setinggi,terkira,mengira,para,sebegini,seluruh,seusai,terlalu,mengucapkan,pasti,sebegitu,seluruhnya,sewaktu,terlebih,mengucapkannya,pastilah,sebelum,semacam,siap,terlihat,mengungkapkan,penting,sebelumnya,semakin,siapa,termasuk,menjadi,pentingnya,sebenarnya,semampu,siapakah,ternyata,menjawab,per,seberapa,semampunya,siapapun,tersampaikan,menjelaskan,percuma,sebesar,semasa,sini,tersebut"
stop3 = stop3.split(',')
for x in stop1:
	if x not in punyaku:
		if x in stop2 and x in stop3:
			punyaku.append(x)
		elif x in stop2 or x in stop3:
			a = random.randint(1, 10)
			if a < 3:
				punyaku.append(x)

for x in stop2:
	if x not in punyaku:
		if x in stop1 and x in stop3:
			punyaku.append(x)
		elif x in stop1 or x in stop3:
			a = random.randint(1, 10)
			if a < 3:
				punyaku.append(x)

for x in stop3:
	if x not in punyaku:
		if x in stop2 and x in stop1:
			punyaku.append(x)
		elif x in stop2 or x in stop1:
			a = random.randint(1, 10)
			if a < 3:
				punyaku.append(x)

for x in punyaku:
	if(x not in punyakubaru):
		print (x)

print (punyaku)
