def davriy_jadval():
    """Bu funksiyada D.I.Mendeleyev davriy sistemasidagi barcha elementlar haqida malumot joylangan. """
    faollashtiruvchi = True
    while faollashtiruvchi:
        belgi = input("Davriy sistemadagi hohlagan elementinggizni belgisini kiriting:")
        if belgi == "exit":
           break
        if belgi.lower() == "h":
          print("""🧪 Element: Vodorod (H)

▪️Atom raqami: 1
▪️Atom massasi: 1.008
▪️Eng yengil element: Vodorod koinotdagi barcha moddalar massasining   75% ini tashkil qiladi va u eng yengil elementdir.
▪️Koinotning "quvvati": Vodorod Quyosh va boshqa yulduzlar ichidagi yadro sintezida energiya manbai bo‘lib xizmat qiladi.
▪️Hayot uchun muhim: Suv (H₂O) tarkibida bo‘lgan vodorod Yer yuzidagi barcha tirik organizmlar uchun zarurdir.
▪️Yonuvchi gaz: Vodorod o‘zining yuqori yonuvchanligi bilan tanilgan. Kislorod bilan birlashganda, u portlash bilan energiya hosil qiladi. Shuning uchun u yoqilg‘i sifatida kelajakda katta istiqbolga ega.
▪️Ekologik toza yoqilg‘i: Vodorod avtomobillar va boshqa energiya manbalari uchun ekologik toza yoqilg‘i sifatida ishlatilishi kutilmoqda. Yonish jarayonida faqat suv bug‘i hosil qiladi, bu esa uni toza energiya manbai qiladi.
▪️"Gindeburg" halokati: 1937 yilda "Hindenburg" havo kemasi vodorod gazining portlashi natijasida halokatga uchragan, bu esa havo kemalarida vodoroddan foydalanishga bo‘lgan ishonchni pasaytirgan.
▪️Izotoplari: Vodorodning uchta asosiy izotopi mavjud: protiy (¹H), deyteriy (²H), va tritiy (³H). Protiy eng keng tarqalgan izotop bo‘lib, atom massasi 1 ga teng.
▪️Kichik, lekin qudratli: Vodorod atomlari o‘ta kichik va yengil bo‘lsa-da, ulardan olinadigan energiya miqdori juda katta. Ayniqsa, yadro sintezi jarayonida bu ko‘zga yaqqol tashlanadi.""")

        elif belgi.lower() == "he":
           print("""🧪 Element: Geliy (He)

▪️Atom raqami: 2
▪️Atom massasi: 4.0026
▪️Yengil gaz: Geliy, vodoroddan keyin eng yengil gaz bo‘lib, koinotdagi eng ko‘p tarqalgan ikkinchi elementdir.
▪️Inert gaz: Geliy inert gazlar guruhiga kiradi va kimyoviy reaksiya qilmaydi, bu uni boshqa elementlar bilan osonlikcha birlashishdan saqlaydi.
▪️Quyoshning tarkibi: Geliy Quyoshning yadro sintezi jarayonida vodoroddan hosil bo‘ladi, bu esa Quyoshning energiya manbai hisoblanadi.
▪️Ovoz o‘zgartiruvchi xususiyat: Geliy gazini inhalatsiya qilish ovozning ohangini o‘zgartiradi, shuning uchun ko‘pincha karnaval va partiyalarda ishlatiladi.
▪️Kriogenik qo‘llanilishi: Geliy juda past haroratlarda suyuqlanadi va kriogenik sovutish tizimlarida ishlatiladi, chunki u suyuq holatda kam haroratda qoladi.
▪️Buzilishdan saqlovchi: Geliy, shuningdek, supero‘ta past haroratlarda suyuqliklar o‘rtasidagi reaksiya uchun muhim rol o‘ynaydi va bu uni ilmiy tadqiqotlarda qo‘llaniladigan eng muhim gazlardan biriga aylantiradi.""")

        elif belgi.lower() == "li":
           print("""🧪 Litiy (Li)

▪️Atom raqami: 3
▪️Kashf etilgan yili: 1817-yilda Yohan Arfvedson tomonidan.

🔋 Qiziqarli faktlar:
▪️Litiy dunyodagi eng yengil metall bo‘lib, suvda suzadi va juda reaktiv.
▪️Litiy asosan akkumulyatorlar va batareyalar uchun ishlatiladi, ayniqsa telefonlar va elektromobillar uchun.
▪️Litiy inson kayfiyatini barqarorlashtiruvchi dori sifatida ham qo‘llaniladi.
▪️Litiy ionlari xotira va o‘rganish jarayonlariga ham ijobiy ta’sir ko‘rsatishi mumkin.

🔥 Kimyoviy xususiyatlari:
▪️Havo bilan tez oksidlanadi, suv bilan esa kuchli reaksiya hosil qiladi.
▪️Suvga tushganda qizg‘in reaksiyaga kirishib, vodorod gazini ajratadi.""")

        elif belgi.lower() == "be":
            print("""🧪 Berilliy (Be)

▪️Atom raqami: 4
▪️Kashf etilgan yili: 1798-yilda Nikola-Louis Voklen tomonidan.

🔍 Qiziqarli faktlar:
▪️Berilliy juda yengil metall bo'lib, uni chaynash ham inson uchun qiyin! Shunga qaramay, u yuqori mustahkamlik va qattiqlikka ega.
▪️Bu metall radiatsiyaga nisbatan shaffof bo'lib, uni yadro sanoatida rentgen nurlari uchun ekranlar yaratishda ishlatishadi.
▪️Berilliyning bir necha milligramini ham nafas olish o‘pka kasalliklariga olib kelishi mumkin, bu uni xavfli moddaga aylantiradi.
▪️U juda yuqori haroratlarga chidamli bo‘lgani uchun kosmik kema va sun'iy yo'ldosh komponentlarida ham qo'llaniladi.
▪️Berilliy mis qotishmalarini hosil qilganda, ular elektr o‘tkazuvchanlik va mustahkamlikda juda yuqori ko‘rsatkichlarga ega bo‘ladi, bu qotishmalar elektronika sanoatida muhim ahamiyatga ega.
▪️Berilliy boshqa elementlar bilan aralashganda, ajoyib mexanik xususiyatlarga ega materiallar hosil qiladi. Shu sababli uni yuqori tezlikda ishlaydigan asbob-uskunalarda ishlatishadi.

⚙️ Kimyoviy xususiyatlari:
Juda yuqori haroratga chidamli bo‘lib, erish nuqtasi 1287°C ga teng.
Havo va suv bilan kamdan-kam reaksiyaga kirishadi, bu esa uni yadro reaktorlarida, ayniqsa, neytronlarni boshqarish uchun ishlatiladigan material sifatida qo'llanilishiga sabab bo‘ladi.
Berilliy juda kam uchraydigan elementlardan biri bo‘lib, yer po‘stining atigi 0.0002% qismini tashkil etadi.""")

        elif belgi.lower() == "b":
           print("""🧪 Bor (B)

▪️Atom raqami: 5
▪️Kashf etilgan yili: 1808-yilda Gay-Lyussak va Tenar tomonidan.

🔍 Qiziqarli faktlar:
▪️Bor tabiatda sof holatda kamdan-kam uchraydi va ko‘pincha birikmalar shaklida mavjud. Bunga eng yaxshi misol – borat tuzlari, ular kosmetika va shisha ishlab chiqarishda qo‘llaniladi.
▪️Bordan tayyorlangan "bor karbid" dunyodagi eng qattiq materiallardan biri hisoblanadi, u zirhli materiallar va mustahkam asbob-uskunalar uchun ishlatiladi.
▪️Bor qotishmalari samolyotlar va kosmik kemalarda juda yengil va mustahkam bo‘lgani uchun qo‘llaniladi.
▪️Odam tanasida bor mikroelement sifatida mavjud bo‘lib, suyak sog‘lig‘ini yaxshilash va kalsiy miqdorini boshqarishda yordam beradi.
▪️Borni o‘z ichiga olgan shishalar juda yuqori haroratlarga chidamli bo‘lib, laboratoriya idishlari va o'choq oynalarida ishlatiladi.
▪️Bor termoyadro reaksiyalarida neytronlarni tutib qolish xususiyatiga ega bo'lib, yadro sanoatida xavfsizlik tizimlarida qo'llaniladi.
▪️Bor 1933-yildan beri pirotexnika va favqulodda yoritish moslamalarida yashil olov yaratish uchun ishlatiladi, chunki u olovga o'ziga xos yashil rang beradi.

⚙️ Kimyoviy xususiyatlari:
Bor yuqori erish nuqtasiga ega bo‘lib, harorat 2076°C ga yetganda eriydi.
Havo va suv bilan reaksiyaga kam kirishadi, ammo yuqori haroratda kislorod bilan osonlikcha oksidlanadi.
Bor o‘ta issiqlikka chidamli bo‘lgani sababli, kosmik kema issiqlik qalqonlarida qo‘llaniladi.""")

        elif belgi.lower() == "c":
           print("""Uglerod (C)
Uglerod Yerda eng ko‘p tarqalgan elementlardan biri bo‘lib, hayot uchun muhim hisoblanadi. Quyidagi faktlar sizni hayratga solishi mumkin:

▪️Hayot asosi: Uglerod barcha organik birikmalarning asosini tashkil qiladi, shuning uchun u tirik organizmlarning "tuzilishi"ni belgilaydi.
▪️Allotrop shakllari: Uglerod tabiatda bir nechta allotrop shakllarda mavjud: olmos, grafit, grafen va fulerenlar. Olmos dunyodagi eng qattiq moddadir, grafit esa qog‘ozga yozish uchun ishlatiladi.
▪️Grafen: Grafen faqat bitta atom qalinlikdagi uglerod qatlami bo‘lib, uni kuchli va elektr o'tkazuvchan qiladi. Uning kashfiyoti zamonaviy texnologiyalarga yangi eshiklar ochdi.
▪️Uglerodning izotoplari: Uglerodning uchta tabiiy izotopi mavjud: C-12, C-13 va C-14. C-14 tarixiy yoshi 50 ming yildan oshmagan obyektlarni aniqlashda radiokarbon usuli yordamida ishlatiladi.
▪️Uglerod sikli: Uglerod tabiiy siklda doimiy aylanib yuradi – u atmosferada, tuproqda va tirik organizmlarda kislorod bilan birikib aylanishda davom etadi. Bu tabiiy jarayon sayyoramizning iqlim va hayotiy muvozanatini ta’minlaydi.
▪️Uglerodning qimmatli qo‘llanilishi: Nefrit uglerodning olov bardoshli qotishmasi bo‘lib, kosmik sanoatda, shuningdek, yuqori haroratli jarayonlar uchun ishlatiladi.
▪️Uglevodorodlar: Uglerod va vodorodning birikmalari bo‘lgan uglevodorodlar neft va gaz shaklida yirik energiya manbaidir. Ular zamonaviy iqtisodiyotning asosiy yoqilg‘isi hisoblanadi.""")

        elif belgi.lower() == "n":
           print("""Azot (N)
▪️Azot - Yer atmosferasining asosiy tarkibiy qismi bo‘lib, bizning kundalik hayotimizda va tabiatda katta ahamiyatga ega. Quyidagi faktlar azot haqida sizni qiziqtirishi mumkin:

▪️Atmosferaning asosiy qismi: Yer atmosferasining 78% azotdan tashkil topgan. Ammo biz oddiy nafas olayotganimizda bu gazdan bevosita foydalana olmaymiz.
▪️Azotli o'g'itlar: Azot o‘simliklar uchun muhim ozuqa manbai hisoblanadi. Azotli o‘g‘itlar qishloq xo‘jaligida unumdorlikni oshirishda keng qo‘llaniladi.
▪️Suyuq azot: Suyuq azot -196°C haroratda qaynar bo‘lib, u kriogenika sohasida keng qo‘llaniladi, ayniqsa, tibbiyotda organlarni saqlash va oziq-ovqat mahsulotlarini tez muzlatish uchun ishlatiladi.
▪️DNK va oqsillarning tarkibiy qismi: Azot DNK, RNK va oqsillarning asosiy tarkibiy qismi bo‘lib, hayotning molekulyar asoslarini tashkil qiladi.
▪️Azot sikli: Azot yer va atmosfera o‘rtasida doimiy ravishda aylanib turadi. Bakteriyalar va ildiz me'dalar azotni o‘simliklar o‘zlashtira oladigan shaklga aylantirishda muhim rol o‘ynaydi.
▪️Portlovchi moddalar: Azot nitratlari va nitritlari portlovchi moddalar tarkibiga kiradi. Masalan, TNT va ammoniy nitrat kabi moddalar azotli birikmalarni o‘z ichiga oladi.
▪️Azot dioksidi: Atmosferada azot dioksidi NO₂ havoning ifloslanishiga sabab bo‘ladigan asosiy gazlardan biri bo‘lib, inson salomatligiga salbiy ta'sir ko‘rsatadi.""")

        elif belgi.lower() == "o":
           print("""Kislorod (O)
▪️Kislorod – bu hayot uchun zarur bo‘lgan muhim element bo‘lib, u nafaqat nafas olish uchun, balki tabiat va texnologiya sohasida ham katta ahamiyatga ega. Quyidagi faktlar sizni qiziqtirishi mumkin:
▪️Atmosferaning muhim qismi: Yer atmosferasining taxminan 21% kisloroddan iborat. Bu gaz barcha aerob organizmlar uchun nafas olishda asosiy manba hisoblanadi. 
▪️Nafas olish va fotosintez: Insonlar va hayvonlar nafas olayotganda kislorodni o‘zlashtiradi, o‘simliklar esa fotosintez jarayonida kislorod chiqaradi. 
▪️Suyuq kislorod: Kislorod juda past haroratda (-183°C) suyuq holatga o‘tadi. Suyuq kislorod raketa yoqilg‘isi sifatida ishlatiladi, shuningdek, sanoatda va tibbiyotda ham keng qo‘llaniladi. 
▪️Tirik organizmlarda kislorod: Inson tanasi va hayvonlarning to‘qimalari uchun kislorod zarur bo‘lib, u hujayralardagi metabolik jarayonlarda ishtirok etadi va energiya ishlab chiqarishda muhim ahamiyatga ega. 
▪️Kislorodli moddalar: Suv (H₂O) va karbonat angidrid (CO₂) kabi kislorodli birikmalar hayot uchun zarur hisoblanadi. Suv barcha tirik mavjudotlar uchun muhim bo‘lsa, karbonat angidrid o‘simliklar uchun asosiy ozuqa manbai. 
▪️Ozon qatlami: Ozon (O₃) kislorodning bir shakli bo‘lib, u Yer atmosferasining yuqori qatlamida joylashgan va sayyorani zararli ultrabinafsha nurlardan himoya qiladi. 
▪️Zanglash va oksidlanish: Kislorod metallarga ta’sir qilganda zang hosil bo‘ladi. Oksidlanish jarayoni ko‘plab kimyoviy reaksiyalarda muhim rol o‘ynaydi.""")

        elif belgi.lower() == "f":
           print("""Ftor (F)
▪️Ftor – kimyoviy jihatdan juda faol va kuchli oksidlovchi xususiyatlarga ega element bo‘lib, sanoat va kundalik hayotda muhim o‘rin tutadi. Quyidagi faktlar sizni qiziqtirishi mumkin:
▪️Eng faol element: Ftor eng faol galogen hisoblanadi va boshqa elementlar bilan oson birikmalar hosil qiladi. Bu uni kimyoviy jarayonlarda juda samarali oksidlovchi vositaga aylantiradi. 
▪️Tish emalini himoya qiladi: Ftor tish pastalarida keng qo‘llaniladi, chunki u tish emalini mustahkamlaydi va kariyesni oldini olishda yordam beradi. 
▪️Ftoroplastlar: Ftor polimerlari (masalan, teflon) yuqori issiqlikka chidamliligi va sirpanish xususiyatlari bilan ajralib turadi. Bu materiallar idish-tovoq qoplamalari va sanoat uskunalarida keng qo‘llaniladi. 
▪️Suyuq ftor: Ftor suyuq holatda kuchli reaktiv gaz bo‘lib, u qattiq, suyuq yoki gazsimon moddalar bilan tezda reaksiyaga kirishadi. Uni suyuqlantirish -188°C da amalga oshadi. 
▪️Ftorli sovitish agentlari: Ftor birikmalari sovitish agentlari (freonlar) sifatida ishlatiladi, ammo ba’zi freonlarning atmosferaga zararli ta’siri sababli ular bosqichma-bosqich kamaytirib borilmoqda. 
▪️Uran boyitishda ishlatiladi: Ftor uran boyitish jarayonida UF₆ (uran ftorid) birikmasini hosil qilish uchun ishlatiladi. Bu yadro yoqilg‘isini tayyorlashda muhim ahamiyatga ega. 
▪️Zaharli gaz: Ftor gazining yuqori reaktivligi sababli u juda zaharli bo‘lib, inson salomatligiga jiddiy xavf tug‘dirishi mumkin.""")

        elif belgi.lower() == "ne":
           print("""Neon (Ne)
▪️Neon – gazsimon element bo‘lib, uning yorqin va rangli xususiyatlari uni yorug‘lik va dekorativ maqsadlarda keng qo‘llanilishiga olib kelgan. Quyidagi faktlar neon haqida sizni qiziqtirishi mumkin:
▪️Inert gaz: Neon kimyoviy jihatdan inert bo‘lib, boshqa elementlar bilan reaksiyaga kirishmaydi. Bu uni gazlar orasida eng barqaror elementlardan biriga aylantiradi. 
▪️Neon chiroqlari: Neon o‘zining yorqin qizil-nurli spektri bilan mashhur. U reklama chiroqlarida va displeylarda keng qo‘llaniladi. Boshqa gazlar bilan birgalikda ishlatilganda, turli ranglar hosil qiladi. 
▪️Atmosferada kam uchraydi: Yer atmosferasida neonning miqdori juda oz, taxminan 0.0018%. Bu gazni sanoatda ajratib olish juda murakkab jarayon bo‘lishiga qaramay, u yirik gaz ballondan olinadi. 
▪️Sovutish tizimlarida qo‘llaniladi: Neon suyuqlik shaklida kriogenik sovutgich sifatida ishlatiladi. U juda past haroratlarda ishlay oladi, bu esa uni maxsus sovutish tizimlarida samarali qiladi. 
▪️Plazma ekranlarda qo‘llaniladi: Neon ba’zi plazma ekranlari va displey texnologiyalarida ham ishlatiladi, chunki u elektr maydon ta'sirida yorqin nur hosil qilishi mumkin. 
▪️Radioaktiv emas: Neon tabiiy holatda radioaktiv emas, bu uni turli sohalarda xavfsiz ishlatilishiga imkon beradi. 
▪️Neon gazining ochilishi: Neon 1898 yilda ingliz kimyogarlari Uilyam Ramsay va Morris Travers tomonidan kashf etilgan bo‘lib, bu gaz nomini qadimgi yunoncha "neos" so‘zidan olgan, ya’ni "yangi" degan ma’noni anglatadi.""")

        elif belgi.lower() == "na":
           print("""Natriy (Na)
▪️Natriy – yumshoq, metall bo‘lib, uning biologik va sanoat ahamiyati katta. Quyidagi faktlar natriy haqida sizni qiziqtirishi mumkin:
▪️Yuqori reaktivlik: Natriy juda reaktiv metall bo‘lib, suv bilan tez reaksiyaga kirishadi va vodorod gazi ajralib chiqishi bilan portlashga olib kelishi mumkin. Shu sababli, u odatda neft yoki boshqa inert moddalar ostida saqlanadi. 
▪️Osh tuzi tarkibida: Natriy kationlari (Na⁺) odamlar iste'mol qiladigan osh tuzining asosiy tarkibiy qismini tashkil qiladi. Natriy xlorid (NaCl) tanadagi suv muvozanatini saqlashda va nerv impulslarini o‘tkazishda muhim rol o‘ynaydi. 
▪️Kuchli metall: Natriy yumshoq metall bo‘lsa ham, u kuchli gidroksid (NaOH) va ko‘plab boshqa kimyoviy birikmalarni hosil qilishda ishtirok etadi. Bu birikmalar sanoatda keng qo‘llaniladi. 
▪️Sariq rangli olov: Natriy metalli kuyganida yoki ionlari olovda bo‘lganda, u o‘ziga xos yorqin sariq rang chiqaradi. Bu xususiyat natriy lampalari va pirotexnika mahsulotlarida ishlatiladi. 
▪️Biologik ahamiyati: Natriy organizmning hujayra faoliyatida muhim rol o‘ynaydi, ayniqsa nerv hujayralari orqali signallarni uzatishda. Shu sababli, natriy yetishmovchiligi sog‘liq uchun xavfli bo‘lishi mumkin. 
▪️Natriy lampalari: Natriy bug‘lari lampalarida sariq yorug‘lik chiqaradi, bu lampalar ko‘pincha ko‘cha yoritgichlarida ishlatiladi, chunki ular energiya tejamkor va uzoq xizmat muddatiga ega. 
▪️Oson oksidlanadi: Natriy havo bilan kontaktga kirishganda tezda oksidlanadi va natriy oksid (Na₂O) yoki natriy peroksid (Na₂O₂) hosil qiladi. Shu sababli u faqat kimyoviy jihatdan inert sharoitlarda saqlanishi kerak.""")

        elif belgi.lower() == "mg":
           print("""Magniy (Mg)
▪️Magniy – yengil, kumushrang metall bo‘lib, uning biologik va sanoat ahamiyati juda katta. Quyidagi faktlar magniy haqida sizni qiziqtirishi mumkin:
▪️Yuqori yonuvchanlik: Magniy oson yonadi va juda yorqin oq rangdagi olovni hosil qiladi. Bu xususiyati tufayli magniy pirotexnika, fotosuratlar va signal raketalarida keng qo‘llaniladi.
▪️Suyak va mushaklar uchun zarur: Magniy inson organizmidagi suyak va mushak to‘qimalarining to‘g‘ri ishlashi uchun muhimdir. U suyak zichligini saqlashda va mushaklarning qisqarishi jarayonida katta rol o‘ynaydi.
▪️Metallurgiyada qo‘llanilishi: Magniy yengil va mustahkam material sifatida boshqa metallar bilan qotishmalar hosil qiladi. Ayniqsa, alyuminiy bilan qotishmalari aviatsiya va avtomobilsozlik sanoatida yuqori baholanadi.
▪️Xlorofill tarkibida: Magniy o‘simliklarda xlorofill molekulasining markaziy atomi bo‘lib, fotosintez jarayonida asosiy rol o‘ynaydi. U quyosh nurlarini energiyaga aylantirishga yordam beradi.
▪️Asab tizimi uchun foydali: Magniy asab tizimini tinchlantirishda va stressni kamaytirishda foydali hisoblanadi. U uyquni yaxshilash va asab tizimi faoliyatini tartibga solishda ishtirok etadi.
▪️Engil va bardoshli: Magniy engil metall bo‘lib, shu bilan birga yuqori mustahkamlikka ega. Bu xususiyatlari uni transport vositalari va texnologik qurilmalarda ishlatishga mos qiladi.
▪️Korroziyaga chidamli: Magniy qotishmalari korroziyaga chidamli bo‘lib, ularni dengiz transporti va aviatsiyada qo‘llash uchun ideal qiladi.""")

        elif belgi.lower() == "al":
            print("""Aluminiy (Al)
▪️Aluminiy – engil va ko‘p funksiyali metall bo‘lib, yer po‘stining eng keng tarqalgan elementlaridan biri hisoblanadi. Quyidagi faktlar aluminiy haqida sizni qiziqtirishi mumkin:
▪️Yengil va mustahkam: Aluminiy yengil, ammo kuchli metall bo‘lib, u transport vositalari, samolyotlar, avtomobillar va hatto kosmik kemalarda keng qo‘llaniladi. Uning past zichligi va yuqori mustahkamligi uning afzalliklaridandir.
▪️Korroziyaga chidamli: Aluminiy tabiiy ravishda yuzasida oksid qatlami hosil qiladi, bu esa uni korroziyadan himoya qiladi. Shu sababli, u ko‘plab tashqi sharoitlarda foydalaniladi.
▪️Qayta ishlanishi oson: Aluminiy qayta ishlanishi eng oson metallar sirasiga kiradi. Uni qayta ishlash energiya tejamkor bo‘lib, yangi aluminiy ishlab chiqarishga qaraganda kam energiya talab qiladi.
▪️Elektr tokini yaxshi o‘tkazadi: Aluminiy elektr o‘tkazuvchanligi yuqori bo‘lib, misdan keyin elektr kabel va simlarda eng ko‘p ishlatiladigan metall hisoblanadi.
▪️Biologik ahamiyati: Garchi aluminiyning inson organizmi uchun zaruriy elementi bo‘lmasa ham, u ba'zi hollarda suv va oziq-ovqat orqali kirib kelishi mumkin. Inson organizmi aluminiyni yaxshi qayta ishlay oladi va uni to‘g‘ri tashqariga chiqaradi.
▪️Pishirish idishlarida ishlatiladi: Aluminiyning yaxshi issiqlik o‘tkazuvchanligi uni oshxona pishirish idishlarida, qozonlar va tovalar ishlab chiqarishda keng qo‘llanilishiga sabab bo‘ladi.
▪️Sanoatda keng qo‘llaniladi: Aluminiy qurilish, elektronika va qadoqlash sanoatida ham katta ahamiyatga ega. Ayniqsa, aluminiy folga oziq-ovqatlarni saqlashda juda mashhur.
""")

        elif belgi.lower() == "si":
           print("""Kremniy (Si)
▪️Kremniy – metallmas element bo‘lib, yer po‘stining ikkinchi eng ko‘p uchraydigan elementi hisoblanadi. Quyidagi faktlar kremniy haqida sizni qiziqtirishi mumkin:
▪️Yarimo‘tkazgichlar: Kremniy zamonaviy texnologiyalarning asosi bo‘lib, u yarimo‘tkazgich sifatida elektron qurilmalarda, mikroprotsessor va kompyuter chiplarida keng qo‘llaniladi.
▪️Qum va tosh tarkibida: Kremniy yer po‘stining katta qismini tashkil etadi va u asosan kremniy dioksid (SiO₂) shaklida, qum va toshlar tarkibida uchraydi. Shuningdek, shisha ishlab chiqarishda ham muhim rol o‘ynaydi.
▪️Sanoat ahamiyati: Kremniy qotishmalari, ayniqsa, alyuminiy-kremniy qotishmalari, aviatsiya va avtomobilsozlikda qo‘llaniladi. Bu qotishmalar yengil va bardoshli bo‘lib, konstruktiv materiallar sifatida ishlatiladi.
▪️Biologik ahamiyati: Kremniy o‘simliklar va hayvonlar organizmida juda kichik miqdorda uchraydi. Inson suyaklari va to‘qimalari uchun ham kremniy muhim mikroelementlardan biri hisoblanadi.
▪️Shishasozlikda qo‘llaniladi: Kremniy shishasozlik sanoatining asosiy elementi bo‘lib, kremniy dioksidi yuqori haroratlarda eritilib, shisha hosil qiladi. Shu bilan birga, u keramika va sement ishlab chiqarishda ham ishlatiladi.
▪️Yuqori issiqlikka chidamli: Kremniy yuqori haroratlarda ham o‘z xususiyatlarini saqlaydi. Shu sababli, u yuqori haroratli sanoat jarayonlarida, masalan, quyuv texnologiyasida muhim rol o‘ynaydi.
▪️Kremniyli quyosh panellari: Kremniy quyosh panellari uchun asosiy material bo‘lib, u quyosh nurlarini elektr energiyasiga aylantirishda samarali hisoblanadi. Bu texnologiya ekologik toza energiya manbai sifatida tobora ommalashmoqda.
""")

        elif belgi.lower() == "p":
           print("""Fosfor (P)
▪️Fosfor – biologik va sanoat ahamiyatga ega bo‘lgan metallmas elementdir. Quyidagi faktlar fosfor haqida sizni qiziqtirishi mumkin:
▪️Hayot uchun zarur: Fosfor inson organizmi uchun muhim elementlardan biri bo‘lib, DNK va RNK molekulalarining asosiy qismi hisoblanadi. Shuningdek, hujayra energiyasi almashinuvining ajralmas qismi bo‘lgan ATF molekulasida ham fosfor mavjud.
▪️Uch xil allotrop shakli: Fosforning oq, qizil va qora shakllari mavjud. Oq fosfor juda reaktiv bo‘lib, havo bilan kontaktga kirishsa, o‘z-o‘zidan yonib ketadi. Qizil fosfor esa gugurt ishlab chiqarishda keng qo‘llaniladi.
▪️O‘g‘itlarda ishlatiladi: Fosfor o‘g‘it sanoatida asosiy o‘rin tutadi. Fosfat o‘g‘itlari o‘simliklar o‘sishini tezlashtirish va hosildorlikni oshirishda muhim ahamiyatga ega.
▪️Zaharli modda: Oq fosfor juda zaharli bo‘lib, u kimyoviy qurollar ishlab chiqarishda ham qo‘llaniladi. Shu sababli, u bilan ishlaganda ehtiyot choralarini ko‘rish zarur.
▪️Suyak va tishlar uchun zarur: Fosfor kaltsiy bilan birgalikda inson suyaklari va tishlarining mustahkam bo‘lishiga yordam beradi. Suyak to‘qimalari va tish emalining asosiy qismi fosfatlar hisoblanadi.
▪️Fosforli moddalar: Fosfor turli xil kimyoviy birikmalar hosil qiladi. Masalan, fosforik kislota (H₃PO₄) oziq-ovqat sanoatida va ichimliklar ishlab chiqarishda qo‘llaniladi.
▪️Yorqin fosfor: Oq fosfor tunda yorqin yashil nur chiqaradi. Bu xususiyat harbiy texnika va pirotexnikada ishlatiladi.""")

        elif belgi.lower() == "s":
           print("""Oltingugurt (S)
▪️Oltingugurt – metallmas element bo‘lib, ko‘plab sanoat tarmoqlarida va biologik jarayonlarda muhim rol o‘ynaydi. Quyidagi faktlar oltingugurt haqida sizni qiziqtirishi mumkin:
▪️Vulqonlar tarkibida: Oltingugurt vulqon otilishlari natijasida hosil bo‘ladigan moddalar tarkibida ko‘p uchraydi. Shuningdek, tabiatda sof holatda ham topilishi mumkin.
▪️Kislotalar tarkibida: Oltingugurt ko‘plab kislotalar, ayniqsa, sulfat kislota (H₂SO₄) tarkibida mavjud bo‘lib, bu kislota sanoat kimyosining asosiy komponentlaridan biridir. Sulfat kislota o‘g‘itlar, portlovchi moddalar va boshqa kimyoviy mahsulotlarni ishlab chiqarishda keng qo‘llaniladi.
▪️Biologik ahamiyati: Oltingugurt inson organizmidagi oqsillar, fermentlar va vitaminlar tarkibiga kiradi. U asab hujayralari va boshqa hayotiy jarayonlar uchun zarur bo‘lgan aminokislotalarning bir qismidir.
▪️Pirotexnikada qo‘llaniladi: Oltingugurtning yonuvchanligi tufayli u pirotexnika va portlovchi moddalar ishlab chiqarishda qo‘llaniladi. U gugurt va pirotexnika mahsulotlarida yonuvchi komponent sifatida ishlatiladi.
▪️Dori-darmonlarda: Oltingugurt antiseptik va dezinfeksiyalovchi xususiyatlarga ega bo‘lib, teri kasalliklarini davolashda va dori vositalarida ishlatiladi. U teri kasalliklari, masalan, akne va ekzema kabi holatlarda foydali bo‘lishi mumkin.
▪️Kauchuk ishlab chiqarishda: Oltingugurt vulkanizatsiya jarayonida rezina ishlab chiqarishda qo‘llaniladi, bu esa rezinani mustahkam va elastik qiladi. Vulkanizatsiyalangan kauchuk avto shinalarida va sanoatda keng qo‘llaniladi.
▪️Oziq-ovqat sanoatida: Oltingugurt dioksidi (SO₂) konservant sifatida ishlatiladi. U meva-sabzavotlarni uzoq vaqt saqlashda va sharob ishlab chiqarishda mahsulotlarning sifatini saqlab turishga yordam beradi.""")

        elif belgi.lower() == "cl":
           print("""Xlor (Cl)
▪️Xlor – o‘tkir hidli, yashil-sariq gaz bo‘lib, sanoat va kundalik hayotda keng qo‘llaniladi. Quyidagi faktlar xlor haqida sizni qiziqtirishi mumkin:
▪️Dezinfeksiyalash vositasi: Xlor kuchli dezinfeksiyalovchi vosita bo‘lib, suvni, ayniqsa ichimlik suvini va basseyn suvini tozalashda ishlatiladi. U bakteriyalar, viruslar va boshqa patogenlarni o‘ldiradi.
▪️Kimyoviy birikmalar tarkibida: Xlor ko‘plab kimyoviy birikmalar, masalan, natriy xlorid (NaCl) yoki osh tuzi tarkibiga kiradi. Bu birikma oziq-ovqatda va biologik jarayonlarda muhim rol o‘ynaydi.
▪️PVX ishlab chiqarishda: Xlor polivinilxlorid (PVX) plastiklar ishlab chiqarishda asosiy xomashyo hisoblanadi. PVX qurilish materiallari, sanitariya quvurlari, elektr kabellari va ko‘plab boshqa mahsulotlar uchun ishlatiladi.
▪️Urush qurollari sifatida: Xlor Birinchi jahon urushi davrida zaharli gaz sifatida qo‘llanilgan. Xlor gazining yuqori konsentratsiyasi nafas olishni qiyinlashtirib, jiddiy zaharlanishga olib kelishi mumkin.
▪️Oksidlovchi xususiyatlari: Xlor kuchli oksidlovchi bo‘lib, ko‘plab sanoat jarayonlarida kimyoviy reaktsiyalarni katalizator sifatida qo‘llanadi. U ko‘plab mahsulotlarni, jumladan, oqartirish vositalarini ishlab chiqarishda ishlatiladi.
▪️Biologik ahamiyati: Xlor odam tanasida, xususan, qondagi xlorid ionlari (Cl⁻) shaklida muhim rol o‘ynaydi. U hujayra ichidagi suyuqlik muvozanatini saqlash va asab signallarini uzatishda ishtirok etadi.
▪️Oqartirishda qo‘llaniladi: Xlor va uning birikmalari qog‘oz, mato va boshqa materiallarni oqartirishda keng qo‘llaniladi. Xlorli oqartgichlar kundalik tozalash va sanitariya maqsadlarida ishlatiladi.
""")

        elif belgi.lower() == "ar":
           print("""Argon (Ar)
▪️Argon – inert gazlar guruhiga kiruvchi rangsiz va hidsiz gaz bo‘lib, ko‘plab sanoat va ilmiy jarayonlarda qo‘llaniladi. Quyidagi faktlar argon haqida sizni qiziqtirishi mumkin:
▪️Inert gaz: Argon kimyoviy jihatdan inert, ya'ni boshqa modda bilan deyarli reaksiyaga kirishmaydi. Shu sababli, u ko‘pincha metallurgiya sanoatida, ayniqsa, payvandlash jarayonlarida himoya gazi sifatida ishlatiladi.
▪️Yer atmosferasida uchrashi: Garchi argon yer atmosferasining taxminan 1% ini tashkil qilsa ham, u eng ko‘p uchraydigan uchinchi gaz hisoblanadi.
▪️Yoritishda qo‘llanilishi: Argon neon lampalar va boshqa gazli yoritish moslamalarida ishlatiladi. U elektr tokini yaxshi o‘tkazadi va yorqin ko‘k rang hosil qiladi, bu esa yorug‘lik va reklama belgilari yaratishda foydalaniladi.
▪️O‘ta past haroratlarda: Argon kriogenika, ya'ni o‘ta past haroratlar bilan bog‘liq texnologiyalarda muhim rol o‘ynaydi. Suvni muzlatish va boshqa laboratoriya ishlarida inert sharoitlar yaratish uchun qo‘llaniladi.
▪️Ikkinchi eng ko‘p inert gaz: Geliyning ortidan argon yer po‘stida va atmosferada eng ko‘p tarqalgan inert gazdir. Uning inertligi tufayli ko‘plab ilmiy va sanoat jarayonlarda ishlatiladi.
▪️Ikkiatomli molekula emas: Aksariyat gazlar ikkiatomli bo‘lsa-da, argon atomlarining hech biri bir-biri bilan bog‘lanmaydi, bu esa uni noyob qiladi. Argon faqat alohida atomlar shaklida mavjud bo‘ladi.
▪️Sanoat va ilmiy ahamiyati: Argon sanoat payvandlash, metalllarni ishlab chiqarish, yarimo‘tkazgichlar va boshqa yuqori aniqlik talab qiladigan texnologiyalarda keng qo‘llaniladi. Uning inertligi bu jarayonlarda zaruriy muhit yaratishga yordam beradi.""")

        elif belgi.lower() == "k":
           print("""Kaliy (K)
▪️Kaliy – yumshoq, oltinrang metall bo‘lib, biologik ahamiyatga ega va sanoatda keng qo‘llaniladi. Quyidagi faktlar kaliy haqida sizni qiziqtirishi mumkin:
▪️Biologik rol: Kaliy o‘simliklar va hayvonlar organizmidagi hujayra faoliyatida muhim rol o‘ynaydi. U nerv impulslarini uzatishda va mushak kontraksiyalarini boshqarishda ishtirok etadi.
▪️Kaliy tuzlari: Kaliy kationlari (K⁺) oziq-ovqatda, ayniqsa, osh tuzida va mineral o‘g‘itlarda muhim ahamiyatga ega. U o‘simliklar o‘sishini tezlashtiradi va hosildorlikni oshiradi.
▪️Suv bilan reaksiya: Kaliy juda reaktiv metall bo‘lib, suv bilan tez reaksiya berib, kaliy gidroksid (KOH) va vodorod gazini hosil qiladi. Bu reaksiya davomida kuchli energiya chiqariladi.
▪️Yumshoq metall: Kaliy yumshoq metall bo‘lib, barmoq bilan osonlikcha kesilishi mumkin. Shuning uchun uni saqlashda ehtiyot bo‘lish zarur. U havo bilan kontaktga kirishganda tez oksidlanadi.
▪️Yorqin olov: Kaliy yondirilganda, o‘ziga xos yoqimli ko‘k rangli olov chiqaradi. Bu xususiyat kaliy lampalarida va pirotexnikada qo‘llaniladi.
▪️Oziq-ovqatda mavjud: Kaliy oziq-ovqat mahsulotlarida, masalan, banan, pomidor va kartoshkada mavjud bo‘lib, inson organizmiga zarur bo‘lgan minerallardan biridir. Kaliy yetishmovchiligi sog‘liq uchun xavfli bo‘lishi mumkin.
▪️Qishloq xo‘jaligida: Kaliy o‘g‘itlar ishlab chiqarishda muhim komponent hisoblanadi. U o‘simliklarning rivojlanishini va ozuqa moddalarini yaxshi o‘zlashtirishini ta'minlaydi.""")

        elif belgi.lower() == "ca":
           print("""Kaltsiy (Ca)
▪️Kaltsiy – erkin holda uchramaydigan, ammo birikmalar shaklida keng tarqalgan metall bo‘lib, inson organizmi uchun muhim rol o‘ynaydi. Quyidagi faktlar kaltsiy haqida sizni qiziqtirishi mumkin:
▪️Suyak va tishlarning mustahkamligi: Kaltsiy inson suyaklari va tishlarining asosiy tarkibiy qismi bo‘lib, ularni mustahkam qiladi. Kaltsiy yetishmovchiligi osteoporozga olib kelishi mumkin, bu esa suyaklarning mo‘rtlashishi bilan bog‘liq.
▪️Qon ivishida ishtirok etadi: Kaltsiy qonni ivish jarayonida muhim rol o‘ynaydi, bu esa jarohatlar va jarrohlik aralashuvlarida qon yo‘qotishni oldini olishga yordam beradi.
▪️Musak kontraksiyalari: Kaltsiy mushaklarning qisqarishi va yurak urishlarining normal ishlashi uchun zarurdir. U nerv signallarini uzatishda va mushaklarni harakatga keltirishda ishtirok etadi.
▪️Suv bilan reaksiya: Kaltsiy suv bilan reaksiyaga kirishganda kaltsiy gidroksid (Ca(OH)₂) va vodorod hosil qiladi. Bu reaktsiya natijasida issiqlik chiqariladi.
▪️Tsement va gips: Kaltsiy oksidi va kaltsiy sulfat qurilish materiallari, xususan, tsement va gips ishlab chiqarishda keng qo‘llaniladi. Bu materiallar binolarni mustahkam qilish va tugatishda ishlatiladi.
▪️Sanoatda ishlatilishi: Kaltsiy metallurgiyada deoksidlovchi sifatida qo‘llaniladi va boshqa metallardan qotishmalar hosil qilish uchun ishlatiladi. U po‘lat va alyuminiy ishlab chiqarishda zarurdir.
▪️Oziq-ovqat manbalari: Sut mahsulotlari, yashil bargli sabzavotlar va yong‘oqlar kaltsiyga boy oziq-ovqat mahsulotlari hisoblanadi. Ular organizmning kundalik kaltsiyga bo‘lgan ehtiyojini qondiradi.""")

        elif belgi.lower() == "sc":
           print("""Skandiy (Sc)
▪️Skandiy – kam uchraydigan, yengil va o‘ziga xos metall bo‘lib, aerokosmik sanoatda va ilmiy tadqiqotlarda qo‘llaniladi. Quyidagi faktlar skandiy haqida sizni qiziqtirishi mumkin:
▪️Kam uchraydi: Skandiy yer po‘stida juda kam uchraydi va uni sof holda olish qiyin. U asosan skandiy oksid shaklida mavjud bo‘lib, undan metall olish murakkab jarayon talab etadi.
▪️Aerokosmik sanoatda: Skandiy alyuminiy bilan qotishma hosil qilganda, materialning mustahkamligi va yengilligini oshiradi. Bu qotishmalar aerokosmik sanoatda va sport anjomlari ishlab chiqarishda ishlatiladi.
▪️Yorqin chiroq lampalari: Skandiy ksenon lampalari tarkibida ishlatiladi, bu lampalar yuqori sifatli yorug‘lik chiqaradi va filmografiyada, stadionlarda va yirik tadbirlarda ishlatiladi.
▪️Radioaktiv izotoplari: Skandiyning radioaktiv izotoplari ilmiy tadqiqotlarda, ayniqsa, radioaktiv kuzatuv va diagnostika uchun qo‘llaniladi.
▪️O‘ta kuchli qotishmalar: Skandiy boshqa metallar bilan birikib, o‘ta kuchli va engil qotishmalar hosil qiladi, bu esa ularni samolyotlar va boshqa yuqori yuk ko‘taradigan texnologiyalarda qo‘llashga imkon beradi.
▪️Kimyoviy reaksiyalarda: Skandiy katalizator sifatida kimyoviy sanoatda qo‘llanadi, chunki u ko‘plab reaksiyalarning tezlashishiga yordam beradi. Bu esa maxsus mahsulotlar ishlab chiqarishda zarurdir.
▪️Kam foydalanilishi: Skandiy ko‘p foydalanilmaydigan elementlardan biri bo‘lsa-da, uning qotishmalari va boshqa qo‘llanmalari kelajakda texnologik rivojlanish uchun katta ahamiyatga ega bo‘lishi mumkin.""")

        elif belgi.lower() == "ti":
            print("""Titan (Ti)
▪️Titan – yengil, mustahkam va korroziyaga chidamli metall bo‘lib, ko‘plab sanoat va ilmiy sohalarda ishlatiladi. Quyidagi faktlar titan haqida sizni qiziqtirishi mumkin:
▪️Yuqori mustahkamlik: Titan o‘zining yuqori mustahkamligi va yengilligi bilan mashhur. U po‘latdan ikki barobar kuchli, ammo ancha yengil bo‘lib, aviatsiya va kosmik sanoatda keng qo‘llaniladi.
▪️Korroziyaga chidamli: Titan kuchli korroziyaga chidamli metall hisoblanadi, shuning uchun u dengiz texnikasi, kemalar va kimyoviy reaktorlar qurilishida qo‘llaniladi. Tuzli suv va kuchli kislotalar bilan tasirlashganda ham u o‘z xususiyatlarini saqlab qoladi.
▪️Biologik moslik: Titan inson tanasi bilan mos keladigan metall bo‘lib, tibbiyotda implantlar, suyak protezlari va boshqa jarrohlik asbob-uskunalari uchun keng qo‘llaniladi. U tana to‘qimalari bilan reaksiyaga kirishmaydi va uzoq muddatli ishlashga yaroqlidir.
▪️Titan dioksidi (TiO₂): Titan dioksidi oq pigment sifatida bo‘yoqlar, kosmetika mahsulotlari va oziq-ovqat mahsulotlarida ishlatiladi. U quyosh nurini qaytarish xususiyatiga ega bo‘lib, quyoshdan himoya kremlarida ham keng qo‘llaniladi.
▪️Sanoatdagi ahamiyati: Titan neft sanoatida, gaz qazib olishda va kimyo sanoatida maxsus uskunalar tayyorlashda qo‘llaniladi. U yuqori harorat va bosimga chidamliligi sababli bu jarayonlar uchun ideal materialdir.
▪️Koinot tadqiqotlari: Titan o‘zining yuqori harorat va korroziyaga chidamliligi sababli kosmik kemalar, sun'iy yo‘ldoshlar va boshqa koinot texnologiyalarida keng qo‘llaniladi.
▪️Yengil va mustahkam qotishmalar: Titan boshqa metallar bilan qotishmalar hosil qilib, mustahkam va yengil materiallar ishlab chiqarishda ishlatiladi. Bu qotishmalar samolyotlar, avtomobillar va sport anjomlari ishlab chiqarishda qo‘llaniladi.
""")

        elif belgi.lower() == "v":
           print("""Vanadiy (V)
▪️Vanadiy – mustahkam va korroziyaga chidamli metall bo‘lib, qotishmalar va sanoat texnologiyalarida muhim rol o‘ynaydi. Quyidagi faktlar vanadiy haqida sizni qiziqtirishi mumkin:
▪️Kuchli qotishmalar: Vanadiy po‘lat bilan birikib, yuqori mustahkamlikka ega qotishmalar hosil qiladi. Bu qotishmalar asosan avtomobilsozlikda, samolyot va kema qurilishida qo‘llaniladi, chunki ular yengil, lekin juda bardoshlidir.
▪️Korroziyaga chidamlilik: Vanadiy yuqori darajada korroziyaga chidamli bo‘lib, kimyo sanoatida va maxsus metallurgiya jarayonlarida ishlatiladi. U yuqori haroratli muhitlarda ham o‘z xususiyatlarini saqlaydi.
▪️Vanadiy oksidi (V₂O₅): Vanadiy pentoksidi katalizator sifatida kimyo sanoatida va sulfat kislotasi ishlab chiqarishda keng qo‘llaniladi. Bundan tashqari, u rangli shisha va keramikalar ishlab chiqarishda qo‘llaniladi.
▪️Energiya saqlash: Vanadiy yadro energetikasida va qayta tiklanuvchi energiya texnologiyalarida, xususan, vanadiy oqimli batareyalarda energiya saqlash tizimlari uchun ishlatiladi. Bu batareyalar katta hajmdagi energiyani uzoq vaqt saqlash imkonini beradi.
▪️Biologik rol: Garchi vanadiy organizm uchun zarur mikroelement bo‘lmasa-da, ba'zi o‘simliklar va dengiz organizmlari vanadiyni o‘zlarida to‘playdi. Tadqiqotlar vanadiy birikmalarining inson organizmi uchun potentsial biologik ahamiyatini o‘rganmoqda.
▪️Rangli shisha: Vanadiy birikmalari shisha va keramikaga turli ranglar berishda ishlatiladi. Bu birikmalar shishaga yashil, ko‘k va sariq ranglar berishi mumkin.
▪️Sanoat ahamiyati: Vanadiy turli sanoat texnologiyalarida, xususan, mexanik qismlar, asboblar va boshqa yuqori mustahkamlik talab qiladigan mahsulotlar ishlab chiqarishda keng qo‘llaniladi.
""")

        elif belgi.lower() == "cr":
           print("""Xrom (Cr)
▪️Xrom – mustahkamligi va korroziyaga chidamliligi bilan mashhur bo‘lgan metall bo‘lib, ko‘plab sanoat tarmoqlarida qo‘llaniladi. Quyidagi faktlar xrom haqida sizni qiziqtirishi mumkin:
▪️Zanglamaydigan po'lat: Xrom zanglamaydigan po‘lat ishlab chiqarishda asosiy element hisoblanadi. Uning po‘latga qo‘shilishi korroziyaga qarshi himoya qatlamini hosil qiladi, bu esa uni uzoq muddat ishlatishga imkon beradi.
▪️Yaltiroq qoplamalar: Xrom metall buyumlar va texnika asbob-uskunalarini himoya qilish va ularni yanada chiroyli qilish uchun yaltiroq qoplama sifatida keng qo‘llaniladi. Xrom bilan qoplangan buyumlar uzoq vaqt davomida korroziyaga qarshi himoyaga ega bo‘ladi.
▪️Rang beruvchi modda: Xrom birikmalari turli xil rang beruvchi moddalarda, xususan, bo‘yoqlarda va shishalarda ishlatiladi. Xrom oksidlaridan yashil va sariq ranglar hosil qilinadi.
▪️Korroziyaga chidamli: Xrom kuchli korroziyaga chidamliligi tufayli dengiz texnikasida va kimyoviy sanoat uskunalarida qo‘llaniladi. U kimyoviy moddalarga, namlikka va yuqori haroratlarga chidamlidir.
▪️Xrom qotishmalari: Xrom boshqa metallar bilan qotishmalar hosil qilib, ularga mustahkamlik va chidamlilik beradi. Ayniqsa, havo va kislotalarga chidamli materiallar yaratishda xromning qotishmalari qo‘llaniladi.
▪️Tibbiy ishlanmalar: Xromning ba’zi birikmalari tibbiyotda qo‘llaniladi, masalan, rentgen apparatlari va boshqa tibbiy asbob-uskunalar ishlab chiqarishda foydalaniladi.
▪️Kimyoviy reaksiyalar: Xrom katalizator sifatida ko‘plab kimyoviy reaksiyalarda ishtirok etadi, bu esa uni kimyo sanoatida muhim elementga aylantiradi.""")

        elif belgi.lower() == "mn":
           print("""Marganets (Mn)
▪️Marganets – kimyoviy va metallurgik jarayonlarda muhim ahamiyatga ega bo‘lgan metall. Quyidagi faktlar marganets haqida sizni qiziqtirishi mumkin:
▪️Qotishmalardagi roli: Marganets po‘lat ishlab chiqarishda keng qo‘llaniladi. U po‘latning mustahkamligini oshiradi va zanglashga qarshi himoya qiladi. Ayniqsa, temirni marganets bilan qotish orqali mustahkam va elastik po‘lat olinadi.
▪️Batareyalarda ishlatiladi: Marganets dioksidi (MnO₂) quruq elementli batareyalar, xususan, qo‘rg‘oshin-kislota akkumulyatorlari va xususiy akkumulyatorlar ishlab chiqarishda asosiy material hisoblanadi.
▪️Biologik ahamiyati: Marganets tirik organizmlar uchun muhim mikroelementdir. U enzimlar tarkibiga kiradi va metabolizm jarayonida asosiy rol o‘ynaydi. Marganets yetishmovchiligi sog‘liq muammolariga olib kelishi mumkin.
▪️Korroziyaga chidamlilik: Marganets qotishmalarga korroziyaga chidamli xususiyat beradi. Shu sababli, u kimyo sanoatida, dengiz texnikasida va yuqori chidamlilik talab qilinadigan materiallarda keng qo‘llaniladi.
▪️Rangli shisha ishlab chiqarish: Marganets birikmalari shisha va keramika buyumlariga turli ranglar berishda ishlatiladi. U, ayniqsa, binafsha va pushti ranglar hosil qilishda qo‘llaniladi.
▪️Marganets oksidlari: Marganetsning turli oksidlari kimyo sanoatida katalizator sifatida ishlatiladi. Ular ko‘plab kimyoviy reaksiyalarning tezlashishiga yordam beradi, bu esa sanoat mahsulotlarining ishlab chiqarish samaradorligini oshiradi.
▪️Tuproq va o‘g‘itlar: Marganets tuproq tarkibini yaxshilash uchun o‘g‘itlar tarkibida ishlatiladi. U o‘simliklar o‘sishi va rivojlanishi uchun muhim elementdir.""")

        elif belgi.lower() == "fe":
           print("""Temir (Fe)
▪️Temir – eng ko‘p qo‘llaniladigan metallar qatoridan bo‘lib, sanoat va texnologik jarayonlarda katta ahamiyatga ega. Quyidagi faktlar temir haqida sizni qiziqtirishi mumkin:
▪️Po‘latning asosiy komponenti: Temirning asosiy qo‘llanishi – po‘lat ishlab chiqarishdir. Po‘lat – temir va uglerodning qotishmasi bo‘lib, u insoniyat tarixidagi eng muhim qurilish va sanoat materiallaridan biridir. U ko‘priklar, binolar, avtomobillar va boshqa ko‘plab inshootlarda qo‘llaniladi.
▪️Biologik ahamiyati: Temir tirik organizmlar uchun muhim element hisoblanadi. U qon tarkibidagi gemoglobin moddasining asosiy qismi bo‘lib, kislorodni o‘pkadan tananing barcha hujayralariga tashishda ishtirok etadi. Temir yetishmovchiligi kamqonlikka olib keladi.
▪️Magnetik xususiyatlar: Temir kuchli magnit xususiyatlarga ega bo‘lib, u magnitlarni yaratishda va elektromexanik qurilmalarda qo‘llaniladi. Temirning ushbu xususiyati texnologik asbob-uskunalar uchun muhim ahamiyatga ega.
▪️Temir oksidi (Fe₂O₃): Temir oksidi rang beruvchi pigment sifatida ishlatiladi. U qizil rangli bo‘yoqlarda, keramika va beton buyumlarda keng qo‘llaniladi. Shuningdek, u abraziv material sifatida ham ishlatiladi.
▪️Korroziyaga chidamlilik: Temirning zanglashini oldini olish uchun uni boshqa metallar bilan qotish qilib yoki maxsus qoplamalar qo‘llab, uning korroziyaga chidamliligini oshirish mumkin. Temir galvanizatsiya jarayonida sink bilan qoplanib, korroziyadan himoyalanadi.
▪️Temirning arzonligi: Temir nisbatan arzon va keng tarqalgan metall hisoblanadi, bu esa uni qurilish, sanoat va texnologiyada juda ko‘p qo‘llashga imkon beradi.
▪️Sanoatda ishlatilishi: Temirning qotishmalari va birikmalari sanoatning turli sohalarida qo‘llaniladi, jumladan, texnik jihozlar, mexanik asboblar va kimyoviy ishlab chiqarish jarayonlarida.
""")

        elif belgi.lower() == "co":
           print("""Kobalt (Co)
▪️Kobalt – ko‘plab sanoat va biologik jarayonlarda qo‘llaniladigan o‘ziga xos metall. Quyidagi faktlar kobalt haqida sizni qiziqtirishi mumkin:
▪️Superqotishmalar: Kobalt yuqori haroratga va korroziyaga chidamli qotishmalar ishlab chiqarishda keng qo‘llaniladi. Bu qotishmalar asosan aviatsiya dvigatellari va gaz turbinasi qismlarida qo‘llaniladi, chunki ular ekstremal sharoitlarda ham o‘z xususiyatlarini saqlab qoladi.
▪️Batareyalarda ishlatiladi: Kobalt ko‘p miqdorda lityum-ion batareyalar ishlab chiqarishda ishlatiladi. Bu batareyalar zamonaviy smartfonlar, noutbuklar va elektr avtomobillari uchun energiya manbai bo‘lib xizmat qiladi.
▪️Rangli pigmentlar: Kobalt birikmalari o‘zining ajoyib ko‘k rangi bilan mashhur bo‘lib, bu pigmentlar asrlar davomida rassomlar tomonidan ishlatilgan. Bugungi kunda ham u keramika, shisha va bo‘yoqlar ishlab chiqarishda qo‘llaniladi.
▪️Biologik rol: Kobalt vitamin B₁₂ ning muhim komponenti bo‘lib, bu vitamin qizil qon hujayralari ishlab chiqarilishida va asab tizimining sog‘lom ishlashida ishtirok etadi. Kobaltning yetishmasligi kamqonlikka olib kelishi mumkin.
▪️Magnit xususiyatlari: Kobalt kuchli magnit xususiyatlarga ega bo‘lgan metallardan biridir. U magnitli qotishmalar va yuqori samarali magnitlar ishlab chiqarishda keng qo‘llaniladi.
▪️Radiatsiyadan himoya: Kobalt-60 izotopi tibbiyotda nurlanish terapiyasida ishlatiladi. U saraton kasalligini davolashda va oziq-ovqat mahsulotlarini sterilizatsiya qilishda qo‘llaniladi.
▪️Korroziyaga chidamlilik: Kobalt yuqori darajada korroziyaga chidamli metall bo‘lib, uni dengiz texnikasi va kimyoviy reaktorlar kabi sharoitlarda ishlatish juda foydali hisoblanadi.""")

        elif belgi.lower() == "ni":
           print("""Nikel (Ni)
▪️Nikel – yuqori chidamlilikka va keng qo‘llanilish imkoniyatiga ega bo‘lgan metall. Quyidagi faktlar nikel haqida sizni qiziqtirishi mumkin:
▪️Zanglamaydigan po‘lat: Nikel zanglamaydigan po‘lat ishlab chiqarishda asosiy tarkibiy qismlardan biri hisoblanadi. U po‘latga korroziyaga chidamlilik va mustahkamlik beradi, bu esa uni ko‘priklar, binolar va texnik uskunalarda keng qo‘llashga imkon beradi.
▪️Nikel qotishmalari: Nikel yuqori haroratga va korroziyaga chidamli qotishmalar ishlab chiqarishda ishlatiladi. Bu qotishmalar aviatsiya va kosmik texnikalarda, reaktiv dvigatellar va gaz turbinasi qismlarida keng qo‘llaniladi.
▪️Korroziyaga chidamlilik: Nikel o‘zi ham yuqori korroziyaga chidamli metall bo‘lib, bu uni dengiz texnikasida, kimyoviy reaktorlar va boshqa ekstremal sharoitlarda ishlatishga imkon beradi.
▪️Elektrik xususiyatlar: Nikel elektrokimyoviy xususiyatlari tufayli akkumulyatorlar va galvanik elementlar ishlab chiqarishda ishlatiladi. Ayniqsa, nikel-kadmiy va nikel-metal gidrid batareyalari ko‘plab qurilmalarda qo‘llaniladi.
▪️Tilla buyumlar qoplamasi: Nikel oltin va kumush buyumlar yuzasini qoplashda ham keng qo‘llaniladi. U buyumlarni oksidlanishdan himoya qiladi va ularga yaltiroq ko‘rinish beradi.
▪️Biologik rol: Nikel oz miqdorda tirik organizmlar uchun zarur mikroelement hisoblanadi. U ba’zi enzimlar faoliyatida muhim rol o‘ynaydi, lekin yuqori miqdorda zararli bo‘lishi mumkin.
▪️Magnit xususiyatlari: Nikel kuchli magnit xususiyatlarga ega metallar qatoriga kiradi. U sanoatda yuqori samarali magnitlar ishlab chiqarishda qo‘llaniladi.""")

        elif belgi.lower() == "cu":
           print("""Mis (Cu)
▪️Mis – o‘zining yuqori elektr va issiqlik o‘tkazuvchanligi bilan mashhur bo‘lgan metall. Quyidagi faktlar mis haqida sizni qiziqtirishi mumkin:
▪️Elektr o‘tkazuvchanligi: Mis elektr tokini mukammal o‘tkazuvchi metall bo‘lib, u kabel, sim va elektr uskunalarida keng qo‘llaniladi. Misning yuqori o‘tkazuvchanligi uni elektr sanoatida ajralmas materialga aylantirgan.
▪️Issiqlik o‘tkazuvchanligi: Mis juda yaxshi issiqlik o‘tkazuvchanligi tufayli issiqlik almashinish tizimlarida, radiatorlarda va maishiy texnika vositalarida qo‘llaniladi. Bu metall sovutish va isitish tizimlarida samaradorlikni oshiradi.
▪️Korroziyaga chidamlilik: Mis tabiiy ravishda korroziyaga yaxshi qarshilik ko‘rsatadi. Shu sababli u quvurlar, tom qoplamalari va dengiz texnikasida keng ishlatiladi. Dengiz suvida ham uzoq vaqt davomida o‘z xususiyatlarini yo‘qotmaydi.
▪️Zargarlikda qo‘llanilishi: Mis oltin va kumush kabi qimmatbaho metallar bilan qotishmalar shaklida ishlatiladi. Bu qotishmalar zargarlik buyumlarining mustahkamligini oshiradi va ularga chiroyli rang beradi.
▪️Antimikrob xususiyatlari: Mis va uning qotishmalari bakteriya va mikroorganizmlarga qarshi tabiiy himoya xususiyatiga ega. Shuning uchun u tibbiyot vositalari, sanitariya buyumlari va mikroblarga qarshi qo‘llanadigan mahsulotlarda ishlatiladi.
▪️Qizg‘ish rang: Mis o‘ziga xos qizg‘ish rangga ega metall bo‘lib, bu unga zargarlik va dekorativ maqsadlarda keng foydalanish imkonini beradi. Uning estetik ko‘rinishi arxitektura va ichki dizaynda ham qadrlanadi.
▪️Biologik ahamiyati: Mis inson organizmida muhim rol o‘ynaydi. U qizil qon hujayralarining ishlab chiqarilishi, enzimlar faoliyati va asab tizimi sog‘lom ishlashi uchun kerak. Mis yetishmovchiligi sog‘liq muammolariga olib kelishi mumkin.
""")

        elif belgi.lower() == "zn":
           print("""Rux (Zn)
▪️Rux – ko‘plab sanoat va biologik jarayonlarda muhim rol o‘ynaydigan metall. Quyidagi faktlar rux haqida sizni qiziqtirishi mumkin:
▪️Zanglamaydigan po‘lat: Rux zanglamaydigan po‘lat va boshqa metallarni himoya qilish uchun galvanizatsiya jarayonida ishlatiladi. Rux qoplamasi metallarni korroziya va zanglashdan saqlaydi, bu esa ularni uzoq muddat davomida ishlatishga imkon beradi.
▪️Biologik ahamiyati: Rux inson organizmida zarur mikroelement hisoblanadi. U immun tizimini mustahkamlash, yaralarning tez bitishini ta'minlash va hujayra bo‘linishida muhim rol o‘ynaydi. Rux yetishmovchiligi sog‘liq muammolariga olib kelishi mumkin.
▪️Sanoat qo‘llanilishi: Rux turli qotishmalar ishlab chiqarishda, masalan, mis va rux qotishmasi (brass) ishlab chiqarishda qo‘llaniladi. Brass musiqiy asboblar, zargarlik buyumlari va boshqa ko‘plab mahsulotlar ishlab chiqarishda keng tarqalgan.
▪️Antimikrob xususiyatlari: Ruxning antimikrob xususiyatlari uni tibbiyotda qo‘llaniladigan preparatlarda, masalan, yaralar va infektsiyalarni davolashda qo‘llaniladigan kremlarda ishlatishga imkon beradi.
▪️Rux oksidi (ZnO): Rux oksidi ko‘plab sanoat mahsulotlarida, jumladan, kosmetikada, dorilarda va kauchuk ishlab chiqarishda qo‘llaniladi. U yaralarni davolashda ham ishlatiladi.
▪️Yengil metall: Rux yengil metall hisoblanadi va oson ishlanadi. U ko‘plab uskunalarda va qoplamalarda ishlatiladi, bu esa uni sanoatda keng tarqalgan materialga aylantiradi.
▪️Yozgi salqinlashtirish: Ruxning yuqori issiqlik o‘tkazuvchanligi ularni yuqori haroratda ishlatiladigan elektron komponentlarda, masalan, issiqlik almashinish tizimlarida qo‘llashga imkon beradi.
""")

        elif belgi.lower() == "ga":
            print("""Galliy (Ga)
▪️Galliy – o‘ziga xos fizik va kimyoviy xususiyatlarga ega metall. Quyidagi faktlar galliy haqida sizni qiziqtirishi mumkin:
▪️Past erish nuqtasi: Galliy juda past erish nuqtasiga (29.76 °C) ega bo‘lib, u xonada suyuq holatda bo‘lishi mumkin. Bu xususiyati galliyni o‘zgacha metall sifatida ajratadi.
▪️Sanoat qo‘llanilishi: Galliy yarimo‘tkazgichlar, xususan, galliy arsenid (GaAs) ishlab chiqarishda ishlatiladi. Bu materiallar elektronika va optoelektronika sohalarida, masalan, lazerlar va quyosh panellarida keng qo‘llaniladi.
▪️Yorqin rang: Galliy metall bo‘lib, o‘ziga xos metall rangga ega. U, shuningdek, yuqori sifatli ko‘k rangli naychalar va gazlarni ishlab chiqarishda ishlatiladi.
▪️Ehtiyotkorlik bilan ishlash: Galliy juda reaktiv metall bo‘lib, u boshqa metallarga, ayniqsa, alyuminiy va misga qarshi juda yaxshi reaktsiya beradi. U o‘zining quyi metallarga bo‘lgan ta’siri tufayli ehtiyotkorlik bilan ishlatilishi kerak.
▪️Biologik ahamiyati: Galliy inson organizmi uchun zarur bo‘lmasa ham, ba’zi tadqiqotlar uning ba’zi biologik jarayonlarda rol o‘ynashi mumkinligini ko‘rsatmoqda.
▪️Tibbiyotda qo‘llanilishi: Galliyning radioaktiv izotoplari, masalan, galliy-67, tibbiyotda saraton kasalligini aniqlash va davolashda qo‘llaniladi.
▪️Sog‘liq uchun xavfsizlik: Galliy odamlar uchun nisbatan xavfsiz metall hisoblanadi va uning toksikligi kam. Shuning uchun u kimyoviy va biologik tadqiqotlarda foydalanish uchun qiziqarli materialdir.""")

        elif belgi.lower() == "ge":
           print("""Germaniy (Ge)
▪️Germaniy – yarimo‘tkazgich sifatida muhim ahamiyatga ega metall. Quyidagi faktlar germaniy haqida sizni qiziqtirishi mumkin:
▪️Yarimo‘tkazgich xususiyatlari: Germaniy yarimo‘tkazgich sifatida elektr toki o‘tkazuvchanligini oshirish yoki kamaytirish imkonini beradi. Bu xususiyat elektronika sanoatida juda muhimdir.
▪️Transistor va diodlar: Germaniy, asosan, transistorlar, diodlar va boshqa elektron komponentlar ishlab chiqarishda ishlatiladi. U yuqori tezlik va past energiya sarfini ta’minlaydi.
▪️Optik xususiyatlar: Germaniy infraqizil nurlarni o‘tkazish qobiliyatiga ega bo‘lib, optik vositalar, masalan, infraqizil ko‘zoynaklar va fotoelektrik detektorlarda qo‘llaniladi.
▪️Kimyoviy reaktivlik: Germaniy ko‘pgina kimyoviy moddalar bilan reaksiyaga kirishishi mumkin, bu uni qiyin sharoitlarda ishlatishga to‘sqinlik qilishi mumkin.
▪️Past erish nuqtasi: Germaniy 938 °C da eriydi, bu esa uni ishlab chiqarish jarayonlarida oson ishlatilishiga yordam beradi.
▪️Biologik ahamiyati: Germaniy inson organizmida zarur emas, lekin uning ba’zi izotoplari radioaktiv xususiyatlarga ega. U kimyoviy tadqiqotlar va tibbiyotda ishlatilishi mumkin.
▪️Zanglamaydigan xususiyatlar: Germaniy yuqori korroziyaga chidamlilikka ega, bu uni ba’zi kimyoviy muhitlarda ishlatish uchun qulay qiladi.""")

        elif belgi.lower() == "as":
           print("""Mishyak (As)
▪️Mishyak – o‘ziga xos kimyoviy xususiyatlarga ega metalloid. Quyidagi faktlar mishyak haqida sizni qiziqtirishi mumkin:
▪️Zaharli xususiyatlar: Mishyak yuqori toksik xususiyatlarga ega bo‘lib, u inson salomatligiga zarar yetkazishi mumkin. Mishyak bilan ishlaganda ehtiyotkorlik kerak.
▪️Yarimo‘tkazgich sifatlari: Mishyak yarimo‘tkazgich sifatida ishlatiladi, bu uni elektronika va yarimo‘tkazgichlar ishlab chiqarishda qo‘llashga imkon beradi.
▪️Kimyoviy birikmalar: Mishyak ko‘plab kimyoviy birikmalar, jumladan, mishyak oksidi (As₂O₃) va mishyak kislotasi (H₃AsO₄) hosil qiladi. Bu birikmalar sanoat va tibbiyotda qo‘llaniladi.
▪️Tibbiyotda qo‘llanilishi: Mishyak tarixiy jihatdan ba’zi kasalliklarni davolashda qo‘llanilgan. Hozirgi kunda esa, u asosan tibbiy tadqiqotlarda foydalaniladi.
▪️Qishloq xo‘jaligida qo‘llanilishi: Mishyak pestitsidlar va o‘g‘itlar ishlab chiqarishda qo‘llaniladi, ammo uning toksikligi tufayli ehtiyotkorlik bilan ishlatilishi kerak.
▪️Qattiq holatda: Mishyak qattiq holatda bo‘lib, o‘ziga xos metall rangga ega. U kristall tuzilishga ega va birikmalari odatda kuchli reaktiv xususiyatlarga ega.
▪️Qat'iy nazorat: Mishyakning toksikligi va zararli ta’siri tufayli, uning ishlatilishi qat'iy nazorat ostida.""")

        elif belgi.lower() == "se":
           print("""Selen (Se)
▪️Selen – muhim kimyoviy xususiyatlarga ega element. Quyidagi faktlar selen haqida sizni qiziqtirishi mumkin:
▪️Biologik ahamiyati: Selen inson organizmida zarur mikroelement hisoblanadi. U antioksidant sifatida faoliyat ko‘rsatadi va hujayralarni erkin radikallardan himoya qiladi.
▪️Oziq-ovqat manbai: Selen ko‘plab oziq-ovqat mahsulotlarida, jumladan, dengiz mahsulotlari, yong‘oqlar va dukkaklilarda mavjud. Selen yetishmovchiligi sog‘liq muammolariga olib kelishi mumkin.
▪️Selen qotishmalari: Selen metallarning qotishmalarini ishlab chiqarishda, masalan, mis, rux va temir bilan birgalikda qo‘llaniladi. Bu qotishmalarning korroziyaga chidamliligini oshiradi.
▪️Korroziya qarshiligi: Selen korroziyaga chidamli xususiyatlarga ega bo‘lib, ba’zi sanoat jarayonlarida ishlatiladi, masalan, kimyoviy ishlab chiqarish va galvanizatsiya.
▪️Kimyoviy reaktivlik: Selen ko‘plab elementlar va birikmalar bilan reaksiya qilishi mumkin. U kislorod bilan birikib, selen oksidlarini hosil qiladi.
▪️Fotovoltaik xususiyatlar: Selen yarimo‘tkazgich sifatida fotovoltaik elementlar ishlab chiqarishda qo‘llaniladi. Bu quyosh energiyasini elektr energiyasiga aylantirishda muhim ahamiyatga ega.
▪️Zaharli xususiyatlar: Selen yuqori konsentratsiyalarda toksik bo‘lishi mumkin. Shuning uchun, selen bilan ishlashda ehtiyotkorlik kerak.""")

        elif belgi.lower() == "br":
           print("""Brom (Br)
▪️Brom – o‘ziga xos kimyoviy xususiyatlarga ega halogen element. Quyidagi faktlar brom haqida sizni qiziqtirishi mumkin:
▪️Suyuqlik holati: Brom xonada suyuq holatda bo‘lib, qizil-binafsha rangga ega. U halogenlar guruhi a’zosi bo‘lib, bu guruhdagi eng og‘ir elementdir.
▪️Reaktivlik: Brom juda reaktiv kimyoviy element hisoblanadi. U ko‘plab metall va nometall bilan, shuningdek, organik birikmalar bilan oson reaksiya qiladi.
▪️Bromid birikmalari: Brom bromidlar, masalan, natriy bromid (NaBr) va kaltsiy bromid (CaBr₂) hosil qiladi. Bu birikmalar tibbiyotda, sanoatda va qishloq xo‘jaligida qo‘llaniladi.
▪️Antiseptik xususiyatlar: Bromning antiseptik xususiyatlari bor, bu uni tibbiyotda, xususan, yaralarni davolashda ishlatishga imkon beradi.
▪️Kimyoviy ishlab chiqarish: Brom kimyo sanoatida keng qo‘llaniladi, masalan, pestitsidlar, flamadretlar va yoqilg‘i qo‘shilmalari ishlab chiqarishda.
▪️Tibbiyotda qo‘llanilishi: Brom bir vaqtlar sedativ va antiepileptik vosita sifatida qo‘llanilgan. Hozirgi kunda esa u ko‘proq boshqa dori vositalarini ishlab chiqarishda ishlatiladi.
▪️Toksiklik: Brom yuqori konsentratsiyalarda toksik hisoblanadi. Shuning uchun, brom bilan ishlashda ehtiyotkorlik va himoya uskunalaridan foydalanish kerak.""")

        elif belgi.lower() == "kr":
           print("""Krypton (Kr)
▪️Kripton – inert gazlar guruhiga mansub bo‘lgan rangsiz, hidsiz va ta'msiz gaz. Quyidagi faktlar kripton haqida sizni qiziqtirishi mumkin:
▪️Inert gaz: Kripton inert gaz hisoblanadi, ya’ni u kimyoviy reaktivlikka ega emas va boshqa elementlar bilan oson reaksiya qilmaydi.
▪️Yuqori atom og‘irligi: Kripton juda og‘ir gaz bo‘lib, uning atom og‘irligi 83.80 g/mol ni tashkil etadi. Bu xususiyat uni boshqa inert gazlardan ajratib turadi.
▪️Yorug‘lik manbai: Kripton lampalarida ishlatiladi, bu lampalar kuchli va toza yorug‘lik berish imkonini beradi. Kripton lampalari ko‘pincha proyektorlar va bezak lampalarida qo‘llaniladi.
▪️Qizil rangli yorug‘lik: Kripton kuchli elektr o‘tkazuvchanligi tufayli yuqori quvvatli yorug‘lik manbalari sifatida ishlatiladi. U qizil rangli yorug‘lik hosil qiladi, bu esa fotonlar bilan bog‘liq tadqiqotlarda qo‘llaniladi.
▪️Nyuanslar hosil qilish: Kripton ko‘plab kimyoviy birikmalar hosil qilishi mumkin, masalan, kripton diflorid (KrF₂).
▪️Tabiiy manba: Kripton tabiiy gaz sifatida havoda juda kam miqdorda (taxminan 1.14 ppm) mavjud. U asosan argon va neondan ajratish jarayonida olinadi.
▪️Aralashmalar: Kripton boshqalar bilan aralashmasdan, o‘zining birikmalarini hosil qilishda cheklangan.
""")

        elif belgi.lower() == "rb":
           print("""Rubidiy (Rb)
▪️Rubidiy – ishqoriy metallar guruhiga mansub bo‘lgan yumshoq va juda reaktiv metall. Quyidagi faktlar rubidiy haqida sizni qiziqtirishi mumkin:
▪️Yuqori reaktivlik: Rubidiy suv bilan tez reaksiya qiladi va bu reaksiyada vodorod gazini chiqaradi, bu esa portlashga olib kelishi mumkin. Shuning uchun rubidiyni ehtiyotkorlik bilan saqlash kerak.
▪️Qizil rang: Rubidiyning yoqilganida chiqadigan olovi qizil rangda bo‘ladi. Bu xususiyat rubidiyni pirotexnika va olovli lampalarda ishlatishga imkon beradi.
▪️Biologik ahamiyati: Rubidiy organizmda natriy va kaliy bilan birga muhim rol o‘ynaydi. U nerv hujayralarining faoliyatida va elektr impulslarini uzatishda ishtirok etadi.
▪️Sanoatdagi qo‘llanilishi: Rubidiy ba’zi maxsus stakl va optik materiallar ishlab chiqarishda, shuningdek, elektron komponentlarda qo‘llaniladi.
▪️Yuqori atom og‘irligi: Rubidiy atom og‘irligi 85.47 g/mol bo‘lib, bu uni boshqa ishqoriy metallar bilan solishtirganda og‘irroq qiladi.
▪️Kuchli magnit xususiyatlar: Rubidiy magnit maydonlarda qiziqarli xususiyatlarga ega bo‘lib, bu uni kvant hisoblash va optik tadqiqotlarda ishlatishga imkon beradi.
▪️Suvda eruvchanlik: Rubidiy suvda juda yaxshi eriydi, bu esa uning reaktivligini oshiradi va suvda ion hosil qilishda muhim ahamiyatga ega.""")

        elif belgi.lower() == "sr":
           print("""Stronsiy (Sr)
▪️Stronsiy – yer qobig‘ida keng tarqalgan va ishqoriy yer metallari guruhiga mansub bo‘lgan metall. Quyidagi faktlar stronsiy haqida sizni qiziqtirishi mumkin:
▪️Yuqori reaktivlik: Stronsiy havo va suv bilan tez reaksiya qiladi, bu esa uni muhofaza qilishda ehtiyotkorlik talab qiladi. U kislorod bilan oson birikib, stronsiy oksidini (SrO) hosil qiladi.
▪️Yuqori atom og‘irligi: Stronsiy atom og‘irligi 87.62 g/mol bo‘lib, bu uni boshqa ishqoriy yer metallari bilan solishtirganda og‘irroq qiladi.
▪️Oltin rangli olov: Stronsiy yonayotganda o‘ziga xos qizil rangda yorug‘lik chiqaradi. Bu xususiyat stronsiydan pirotexnika mahsulotlarida foydalanish imkonini beradi.
▪️Biologik ahamiyati: Stronsiy, kalsiy kabi, organizmda muhim rol o‘ynaydi. U suyaklarda va tishlarda mavjud bo‘lib, ularning mustahkamligini ta’minlaydi.
▪️Sanoatdagi qo‘llanilishi: Stronsiy kimyoviy birikmalari, masalan, stronsiy karbonat (SrCO₃) va stronsiy sulfat (SrSO₄), keramika va stakl ishlab chiqarishda qo‘llaniladi.
▪️Nyuanslar hosil qilish: Stronsiy birikmalari ko‘plab ranglar hosil qilishda foydalaniladi, bu esa ularni rangli chiroqlar va pirotexnika mahsulotlarida ishlatishga imkon beradi.
▪️Stronsiy-90 izotopi: Stronsiy-90 izotopi radioaktiv bo‘lib, u yadro reaktorlari va yadroviy qurollarda mavjud. U odamlar uchun xavfli bo‘lishi mumkin, shuning uchun uning nazorati zarur.""")

        elif belgi.lower() == "y":
           print("""Ittiriy (Y)
▪️Ittiriy – yer qobig‘ida kam miqdorda mavjud bo‘lgan va d- blok elementlari guruhiga mansub metall. Quyidagi faktlar ittiriy haqida sizni qiziqtirishi mumkin:
▪️Yuqori reaktivlik: Ittiriy havo bilan reaksiya qilganda tez oksidlanadi, shuning uchun u muhofaza qilishda ehtiyotkorlik talab qiladi. Oksidlanishdan saqlash uchun odatda inert gazlar ostida saqlanadi.
▪️Oltin rang: Ittiriy o‘ziga xos oltin rangga ega bo‘lgan metall bo‘lib, boshqa metallarga qaraganda bir oz kuchliroq.
▪️Sanoatdagi qo‘llanilishi: Ittiriy birikmalari, masalan, ittiriy oksidi (Y₂O₃), keramika va pirotexnika mahsulotlarida qo‘llaniladi. U shuningdek, yuqori quvvatli lazerlar ishlab chiqarishda ishlatiladi.
▪️Ittiriy lanthanidlar: Ittiriy, lanthanidlar guruhi bilan birga, yuqori energiyali materiallar va magnit materiallar ishlab chiqarishda muhim rol o‘ynaydi.
▪️Biologik ahamiyati: Ittiriy organizmda asosiy rol o‘ynamasa-da, u ba'zi jarayonlarda iz miqdorida bo‘lishi mumkin.
▪️Yuqori atom og‘irligi: Ittiriy atom og‘irligi 88.91 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Radioaktiv izotoplar: Ittiriy-90 izotopi radioaktiv bo‘lib, yadro tibbiyotida qo‘llaniladi, ayniqsa saraton kasalligini davolashda.
""")

        elif belgi.lower() == "zr":
            print("""Sirkoniy (Zr)
▪️Sirkoniy – d-blok elementlari guruhiga mansub bo‘lgan, yuqori reaktiv metall bo‘lib, qattiq va kuchli xususiyatlarga ega. Quyidagi faktlar sirkoniy haqida sizni qiziqtirishi mumkin:
▪️Kuchli korroziya qarshiligi: Sirkoniy havo va suv bilan reaksiya qilmaydi, shuning uchun u korroziya va oksidlanishga nisbatan juda chidamli.
▪️Yuqori erish nuqtasi: Sirkoniy yuqori erish nuqtasiga ega (1855 °C), bu uni yuqori haroratli muhandislik materiallari sifatida ishlatishga imkon beradi.
▪️Sanoatdagi qo‘llanilishi: Sirkoniy, ayniqsa, yadro reaktorlari, aerokosmik sanoat va yuqori haroratli materiallar ishlab chiqarishda keng qo‘llaniladi.
▪️Sirkoniy oksidi: Sirkoniy oksidi (ZrO₂) keramikalar ishlab chiqarishda, shuningdek, yuqori quvvatli lazerlar va optik materiallar uchun muhim xom ashyo hisoblanadi.
▪️Biologik ahamiyati: Sirkoniy organizmda iz miqdorida bo‘lishi mumkin, lekin u biologik jarayonlarda muhim rol o‘ynamaydi.
▪️Yuqori atom og‘irligi: Sirkoniy atom og‘irligi 91.22 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Sirkoniy birikmalari: Sirkoniy birikmalari, masalan, sirkoniy silikati (ZrSiO₄), keramikalar va yuqori sifatli ranglar ishlab chiqarishda qo‘llaniladi.""")

        elif belgi.lower() == "nb":
           print("""Niobiy (Nb)
▪️Niobiy – d-blok elementlari guruhiga mansub bo‘lgan metall bo‘lib, o‘zining kuchli mexanik xususiyatlari va yuqori erish nuqtasiga ega. Quyidagi faktlar niobiy haqida sizni qiziqtirishi mumkin:
▪️Korroziya qarshiligi: Niobiy yuqori korroziya qarshiligiga ega bo‘lib, ko‘plab kimyoviy moddalar bilan reaksiya qilmaydi.
▪️Yuqori erish nuqtasi: Niobiyning erish nuqtasi 2468 °C, bu uni yuqori haroratli muhandislik materiallari sifatida ishlatishga imkon beradi.
▪️Sanoatdagi qo‘llanilishi: Niobiy ko‘plab sanoat sohalarida, jumladan, metallurgiya, aerokosmik sanoat va elektronika sohalarida qo‘llaniladi.
▪️Niobiy birikmalari: Niobiy birikmalari, masalan, niobiy oksidi (Nb₂O₅), keramika va yuqori kuchli materiallar ishlab chiqarishda muhim rol o‘ynaydi.
▪️Yuqori atom og‘irligi: Niobiy atom og‘irligi 92.91 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Molekulyar tuzilishi: Niobiy oddiy tuzilishga ega bo‘lib, o‘zining qattiq holatidagi kristall tuzilishi bilan ajralib turadi.
▪️Biologik ahamiyati: Niobiy organizmda iz miqdorida bo‘lishi mumkin, lekin u biologik jarayonlarda muhim rol o‘ynamaydi.
""")

        elif belgi.lower() == "mo":
           print("""Molibden (Mo)
▪️Molibden – d-blok elementlari guruhiga mansub metall bo‘lib, o‘zining yuqori erish nuqtasi va mustahkamligi bilan ajralib turadi. Quyidagi faktlar molibden haqida sizni qiziqtirishi mumkin:
▪️Yuqori erish nuqtasi: Molibdenning erish nuqtasi 2623 °C bo‘lib, bu uni yuqori haroratli materiallar ishlab chiqarishda qo‘llash uchun ideal qiladi.
▪️Korroziya qarshiligi: Molibden yuqori korroziya va oksidlanishga qarshilik ko‘rsatadi, bu esa uni kimyoviy jarayonlarda qo‘llashga imkon beradi.
▪️Sanoatdagi qo‘llanilishi: Molibden ko‘plab sanoat sohalarida, jumladan, metallurgiya, aerokosmik sanoat va elektronika sohalarida keng qo‘llaniladi.
▪️Molibden birikmalari: Molibden birikmalari, masalan, molibden oksidi (MoO₃), katalizatorlar va ranglar ishlab chiqarishda muhim rol o‘ynaydi.
▪️Biologik ahamiyati: Molibden organizmda iz miqdorida muhim rol o‘ynaydi, chunki u ba'zi fermentlar faoliyatida qatnashadi.
▪️Yuqori atom og‘irligi: Molibden atom og‘irligi 95.94 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Molibdenning xususiyatlari: Molibdenning yuqori mexanik kuchi va issiqlikka chidamliligi uni ko‘plab muhandislik ilovalarida ideal material sifatida ishlatishga imkon beradi.
""")

        elif belgi.lower() == "tc":
           print("""Texnetsiy (Tc)
▪️Texnetsiy – d-blok elementlari guruhiga mansub bo‘lgan, radioaktiv metall bo‘lib, o‘zining noyob xususiyatlari bilan ajralib turadi. Quyidagi faktlar texnetsiy haqida sizni qiziqtirishi mumkin:
▪️Birlamchi element: Texnetsiy birlamchi sintetik element bo‘lib, tabiiy holda topilmaydi va faqat laboratoriya sharoitida sintetik usullar bilan olinadi.
▪️Yuqori erish nuqtasi: Texnetsiyning erish nuqtasi 2430 °C bo‘lib, bu uni yuqori haroratli muhandislik materiallari sifatida ishlatish imkonini beradi.
▪️Sanoatdagi qo‘llanilishi: Texnetsiy ko‘pincha nuklear tadqiqotlarda va radiologik tahlillarda ishlatiladi.
▪️Radioaktiv xususiyatlar: Texnetsiy radioaktiv element bo‘lib, u juda qisqa yarim umrga ega (taxminan 6,0 soat) va shuning uchun tezda parchalanadi.
▪️Biologik ahamiyati: Texnetsiy biologik jarayonlarda muhim rol o‘ynamaydi, lekin uning izotoplari tibbiyotda, masalan, radiologik tasvirlashda foydalaniladi.
▪️Yuqori atom og‘irligi: Texnetsiy atom og‘irligi 98 g/mol atrofida bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Texnetsiy birikmalari: Texnetsiy birikmalari, masalan, texnetsiy oksidi (TcO₂), tadqiqotlarda va analitik kimyoda qo‘llaniladi.
""")

        elif belgi.lower() == "ru":
           print("""Ruteniy (Ru)
▪️Ruteniy – d-blok elementlari guruhiga mansub bo‘lgan metall bo‘lib, o‘zining noyob xususiyatlari va yuqori korroziya qarshiligi bilan ajralib turadi. Quyidagi faktlar ruteniy haqida sizni qiziqtirishi mumkin:
▪️Korroziya qarshiligi: Ruteniy yuqori korroziya qarshiligiga ega, bu uni kimyoviy jarayonlarda va yuqori haroratli muhandislik ilovalarida ishlatishga imkon beradi.
▪️Sanoatdagi qo‘llanilishi: Ruteniy ko‘plab sanoat sohalarida, jumladan, elektronika, metallurgiya va katalizatorlar ishlab chiqarishda keng qo‘llaniladi.
▪️Yuqori erish nuqtasi: Ruteniyning erish nuqtasi 2334 °C bo‘lib, bu uni yuqori haroratli materiallar sifatida ishlatish uchun ideal qiladi.
▪️Ruteniy birikmalari: Ruteniy birikmalari, masalan, ruteniy oksidi (RuO₂), katalizator sifatida va kimyoviy tahlillarda muhim rol o‘ynaydi.
▪️Biologik ahamiyati: Ruteniy organizmda iz miqdorida bo‘lishi mumkin, lekin uning biologik jarayonlarda muhim roli yo‘q.
▪️Yuqori atom og‘irligi: Ruteniy atom og‘irligi 101.07 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Ruteniy ning xususiyatlari: Ruteniy o‘zining yuqori mexanik kuchi va qattiqligi bilan ajralib turadi, bu uni turli muhandislik ilovalarida ishlatishga imkon beradi.
""")

        elif belgi.lower() == "rh":
           print("""Rodiy (Rh)
▪️Rodiy – d-blok elementlari guruhiga mansub bo‘lgan, qimmatbaho metall bo‘lib, o‘zining yuqori korroziya qarshiligi va metallurgik xususiyatlari bilan ajralib turadi. Quyidagi faktlar rodiy haqida sizni qiziqtirishi mumkin:
▪️Qimmatbaho metall: Rodiy o‘zining qimmatbaho metall sifatida tanilganligi sababli, u zargarlik va yuqori sifatli sanoat mahsulotlarida keng qo‘llaniladi.
▪️Korroziya qarshiligi: Rodiy juda yuqori korroziya qarshiligiga ega, bu uni turli kimyoviy muhitlarda ishlatishga imkon beradi.
▪️Yuqori erish nuqtasi: Rodiyning erish nuqtasi 1964 °C bo‘lib, bu uni yuqori haroratli muhandislik ilovalarida ishlatishga qulay qiladi.
▪️Rodiy birikmalari: Rodiy birikmalari, masalan, rodiy kloridi (RhCl₃), katalizator sifatida kimyoviy jarayonlarda ishlatiladi.
▪️Sanoatdagi qo‘llanilishi: Rodiy asosan avtomobil sanoatida, ayniqsa, katalizatorlarda ishlatiladi, chunki u atrof-muhitni ifloslantiruvchi moddalarni kamaytirishga yordam beradi.
▪️Biologik ahamiyati: Rodiy organizmda muhim rol o‘ynamaydi, lekin uning izotoplari tibbiyotda va analitik kimyoda ishlatiladi.
▪️Yuqori atom og‘irligi: Rodiy atom og‘irligi 102.91 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
""")

        elif belgi.lower() == "pd":
           print("""Palladiy (Pd)
▪️Palladiy – d-blok elementlari guruhiga mansub bo‘lgan, qimmatbaho metall bo‘lib, o‘zining yuqori katalitik xususiyatlari bilan ajralib turadi. Quyidagi faktlar palladiy haqida sizni qiziqtirishi mumkin:
▪️Katalizator sifatida qo‘llanilishi: Palladiy avtomobil sanoatida, ayniqsa, katalizatorlarda ishlatiladi, chunki u atrof-muhitni ifloslantiruvchi moddalarni kamaytirishda samarali hisoblanadi.
▪️Qimmatbaho metall: Palladiy o‘zining qimmatbaho metall sifatida tanilganligi sababli, u zargarlik va yuqori sifatli sanoat mahsulotlarida keng qo‘llaniladi.
▪️Yuqori korroziya qarshiligi: Palladiy juda yuqori korroziya qarshiligiga ega, bu uni turli kimyoviy muhitlarda ishlatishga imkon beradi.
▪️Erish nuqtasi: Palladiyning erish nuqtasi 1554 °C bo‘lib, bu uni yuqori haroratli ilovalar uchun mos qiladi.
▪️Biologik ahamiyati: Palladiy organizmda iz miqdorida bo‘lishi mumkin, lekin uning biologik jarayonlarda muhim roli yo‘q.
▪️Yuqori atom og‘irligi: Palladiy atom og‘irligi 106.42 g/mol bo‘lib, bu uni boshqa d-blok elementlari bilan solishtirganda og‘irroq qiladi.
▪️Palladiy birikmalari: Palladiy birikmalari, masalan, palladiy xloridi (PdCl₂), kimyoviy jarayonlarda qo‘llaniladi.""")

        elif belgi.lower() == "ag":
           print("""Ag (Kumush)
▪️Kumush – d-blok elementlari guruhiga mansub bo‘lgan, qimmatbaho va estetik jihatdan jozibali metall bo‘lib, o‘zining ko‘plab foydali xususiyatlari bilan ajralib turadi. Quyidagi faktlar kumush haqida sizni qiziqtirishi mumkin:
▪️Yuqori elektr va issiqlik o'tkazuvchanligi: Kumush, barcha metallardan eng yuqori elektr va issiqlik o'tkazuvchanligiga ega bo‘lib, bu uni elektr va elektronika sanoatida keng qo‘llanilishiga imkon beradi.
▪️Qimmatbaho metall: Kumush zargarlik buyumlari, monetalar va boshqa san’at asarlarida keng qo‘llaniladi, chunki u estetik ko‘rinishi va qiymati bilan mashhur.
▪️Korroziya qarshiligi: Kumush o‘zining yaxshi korroziya qarshiligiga ega bo‘lib, lekin havo bilan tez oksidlanadi va kumush oksidi (Ag₂O) hosil qiladi.
▪️Antibakterial xususiyatlar: Kumush tabiiy antibakterial xususiyatlarga ega bo‘lib, tibbiyotda va oziq-ovqat saqlashda ishlatiladi.
▪️Yuqori erish nuqtasi: Kumushning erish nuqtasi 961 °C bo‘lib, bu uni yuqori haroratli muhandislik ilovalarida ishlatishga imkon beradi.
▪️Biologik ahamiyati: Kumush organizmda muhim rol o‘ynamaydi, lekin uning izotoplari ba'zi tibbiy jarayonlarda qo‘llaniladi.
▪️Kumush birikmalari: Kumush birikmalari, masalan, kumush nitrati (AgNO₃), kimyo sanoatida va tibbiyotda keng qo‘llaniladi.
""")

        elif belgi.lower() == "cd":
           print("""Cd (Kadmiy)
▪️Kadmiy – d-blok elementlarining bir qismi bo‘lib, yumshoq va ko‘p jihatdan foydali metall hisoblanadi. Ushbu element haqida qiziqarli faktlar bilan tanishing:
▪️Zaharli element: Kadmiy og‘ir metall bo‘lib, zaharli xususiyatlarga ega. U asosan sanoatda, xususan, akkumulyatorlar va qoplamalarda ishlatiladi, lekin inson organizmi uchun zararli.
▪️Past erish nuqtasi: Kadmiyning erish nuqtasi 321 °C bo‘lib, bu uni qoplamalarda va past haroratli lehimlarda ishlatishga imkon beradi.
▪️Galvanik qoplamalarda qo‘llanilishi: Kadmiyning zanglashdan himoyalovchi xususiyatlari uni metall buyumlarni korroziyadan himoyalashda keng qo‘llanilishiga sabab bo‘lgan.
▪️Radioaktiv izotoplar: Kadmiyning ba'zi izotoplari yadro energetikasi va ilmiy tadqiqotlarda ishlatiladi.
▪️Tabiatda kam uchraydi: Kadmiy yer qobig‘ida juda kam miqdorda uchraydi va asosan sink rudalarida topiladi.
▪️Zargarlik sanoati: Ba'zi zargarlik buyumlari tarkibida oz miqdorda kadmiy bo‘lishi mumkin, lekin uning sog‘liq uchun xavfli ekanligi sababli foydalanish cheklangan.
▪️Kadmiy birikmalari: Kadmiyning kimyo sanoatida ishlatiladigan asosiy birikmalaridan biri bu kadmiy sulfid (CdS) bo‘lib, u pigment sifatida qo‘llaniladi.
""")

        elif belgi.lower() == "in":
            print("""In (Indiy)
▪️Indiy – d-blok elementlaridan biri bo‘lib, yumshoq va cho‘ziluvchan metall sifatida ko‘plab sanoat tarmoqlarida qo‘llaniladi. Quyida indiy haqida bir nechta qiziqarli faktlar keltirilgan:
▪️Nozik ko‘rinishga ega metall: Indiy kumushrang porloq metall bo‘lib, nisbatan kam uchraydi va estetik jihatdan yoqimli ko‘rinadi.
▪️Past erish nuqtasi: Indiyning erish nuqtasi 157 °C bo‘lib, bu uni past haroratli lehimlarda ishlatish imkonini beradi.
▪️Elektronika sanoatida muhim: Indiyning elektr o‘tkazuvchanligi yuqori bo‘lgani uchun u elektron qurilmalarning ekranlarida, ayniqsa suyuq kristalli displeylarda (LCD) keng qo‘llaniladi.
▪️Korroziyaga chidamliligi: Indiy yuqori darajada korroziyaga chidamli bo‘lib, bu uni qoplamalar va himoya qatlamlari sifatida foydalanishga yaroqli qiladi.
▪️Noorganik birikmalar: Indiy oksidi (In₂O₃) va indiy qalay oksidi (ITO) optoelektronikada va quyosh batareyalarida qo‘llaniladigan muhim birikmalardir.
▪️Zanglamas po‘lat ishlab chiqarishda: Indiy ba'zi holatlarda zanglamas po‘latlarni himoya qilish uchun ishlatiladi.
▪️Tabiatda kamyob: Indiy yer qobig‘ida juda kam uchraydi va u ko‘pincha sink va qo‘rg‘oshin rudalarida topiladi.
""")

        elif belgi.lower() == "sn":
           print("""Sn (Qalay)
▪️Qalay – p-blok elementlari guruhiga mansub bo‘lib, uzoq tarixga ega va kundalik hayotda keng qo‘llaniladigan metallardan biridir. Quyidagi faktlar qalay haqida sizni qiziqtirishi mumkin:
▪️Qadimiy metall: Qalay insoniyat tomonidan ming yillar davomida ishlatilgan. U bronza yasalishda (mis va qalay qotishmasi) muhim rol o‘ynagan.
▪️Past erish nuqtasi: Qalayning erish nuqtasi 232 °C bo‘lib, bu uni past haroratli lehimlar va qoplamalarda ishlatishga yaroqli qiladi.
▪️Zanglashdan himoya: Qalay odatda temir yoki mis buyumlarini korroziyadan himoyalash uchun yupqa qatlam tarzida qoplanadi (masalan, qalay qoplamali idishlar).
▪️Plastiklik: Qalay yumshoq va cho‘ziluvchan metall bo‘lib, u turli shakllarga osongina keltiriladi va bu uni sanoatda keng qo‘llashga imkon beradi.
▪️Tabiatda kamyob: Qalay yer qobig‘ida ko‘p uchramaydi, asosan kasiterit (SnO₂) rudalarida topiladi.
▪️Kimyo sanoatida qo‘llanilishi: Qalay oksidi va qalay xloridi kabi birikmalar kimyo sanoatida va elektronika ishlab chiqarishda ishlatiladi.
▪️Qalayning biologik ahamiyati: Qalay inson organizmida muhim rol o‘ynamaydi, lekin uning ba'zi birikmalari muhandislikda va tibbiyotda foydalidir.""")

        elif belgi.lower() == "sb":
           print("""Sb (Surma)
▪️Surma – p-blok elementlari guruhiga kiruvchi, qattiq va mo‘rt metall bo‘lib, qadim zamonlardan beri foydalanib kelinadi. Quyida surma haqida bir nechta qiziqarli faktlar keltirilgan:
▪️Qadimdan qo‘llanilgan: Surma qadimgi Misrda va Mesopotamiyada kosmetik vosita sifatida qo‘llanilgan. Ayniqsa, ko‘z bo‘yog‘i (surma) tarkibida bo‘lgan.
▪️Kimyoviy barqarorlik: Surma kimyoviy jihatdan barqaror metall bo‘lib, ko‘p haroratda oksidlanishga chidamli.
▪️Korroziyaga qarshi: Surma qotishmalarda, ayniqsa qo‘rg‘oshin va qalay bilan aralashtirib, korroziyaga qarshi himoya qatlami hosil qiladi.
▪️Yuqori zichlikdagi akkumulyatorlar: Surma qo‘rg‘oshin qotishmasi tarkibida avtomobil akkumulyatorlarida qo‘llaniladi, bu ularning chidamliligini oshiradi.
▪️Zaharli xususiyatlar: Surma va uning birikmalari zaharli hisoblanadi. U sanoatda va o‘q-dori ishlab chiqarishda, shuningdek olovga chidamli materiallar tayyorlashda qo‘llaniladi.
▪️Elektronika va yarimo‘tkazgichlar: Surma yarimo‘tkazgich sifatida elektronika sanoatida, xususan, diodlar va infraqizil detektorlar ishlab chiqarishda qo‘llaniladi.
▪️Tabiatda uchrashi: Surma asosan stibnit (Sb₂S₃) rudalarida topiladi va ko‘p hollarda sanoat uchun muhim metall hisoblanadi.
""")

        elif belgi.lower() == "te":
           print("""Te (Tellur)
▪️Tellur – p-blok elementlari guruhiga mansub bo‘lgan, qattiq va metallga o'xshash metall, tabiiy ravishda kam uchraydi. Quyida tellur haqida qiziqarli faktlar keltirilgan:
▪️Metallga o'xshash xususiyatlar: Tellur metall va noorganik birikmalar hosil qilish qobiliyatiga ega bo‘lib, ko‘plab sanoat ilovalarida qo‘llaniladi.
▪️Kondensatorlar va yarimo‘tkazgichlar: Tellur yarimo‘tkazgich sifatida elektr qurilmalari, xususan, fotovoltaik panellarda keng qo‘llaniladi.
▪️Tabiatda kam miqdorda uchraydi: Tellur yer qobig‘ida juda kam miqdorda uchraydi, asosan mis va qo‘rg‘oshin rudalarida topiladi.
▪️Toksik xususiyatlar: Tellur va uning birikmalari yuqori darajada toksik bo‘lishi mumkin, shuning uchun ular bilan ehtiyotkorlik bilan ishlash zarur.
▪️Kimyoviy birikmalari: Tellur kislotalari, masalan, tellur kislotasi (H₂TeO₄), kimyo sanoatida foydalaniladi.
▪️Biologik ahamiyati: Tellur inson organizmida muhim rol o‘ynamaydi, lekin ba'zi tadqiqotlarda uning izotoplari biologik jarayonlarda o‘rganilgan.""")

        elif belgi.lower() == "i":
           print("""I (Yod)
▪️Yod – p-blok elementlaridan biri bo‘lib, ko‘k rangga ega, zarur metall bo‘lmagan, lekin biologik jihatdan muhim element hisoblanadi. Quyida yod haqida qiziqarli faktlar keltirilgan:
▪️Tabiiy holati: Yod gaz holatida mavjud emas, lekin qattiq va suyuq holatlarida uchraydi. U ko‘pincha qizil-kor rangda yoki qora chang shaklida bo‘ladi.
▪️Tibbiyotda foydalanish: Yod, asosan, antiseptik va kontrast moddalari sifatida tibbiyotda qo‘llaniladi. Yodli preparatlar jarohatlar va infektsiyalarni davolashda yordam beradi.
▪️Qandli diyetada ahamiyati: Yod organizm uchun muhim bo‘lib, qalqonsimon bezning sog‘lom ishlashi uchun zarur. Yod yetishmovchiligi qalqonsimon bezning kasalliklariga olib kelishi mumkin.
▪️Tabiatda uchrashi: Yod asosan dengiz suvida, albatta, tuzlar shaklida mavjud bo‘lib, shuningdek, ba'zi organik birikmalarda ham uchraydi.
▪️Oziq-ovqatda: Yod, xususan, dengiz mahsulotlari va tuzlarda ko‘p uchraydi, shuning uchun uning iste'moli ahamiyatlidir.
▪️Kimyoviy xususiyatlar: Yod kuchli oksidlovchi xususiyatlarga ega bo‘lib, ba'zi metallarga qarshi reaksiya berishi mumkin.
""")

        elif belgi.lower() == "xe":
           print("""Ksenon (Xe)
▪️Ksenon – kimyoviy elementlar davriy jadvalining 54-elementi bo‘lib, inert gazlar guruhiga kiradi. Quyidagi qiziqarli faktlar ksenon haqida sizni qiziqtirishi mumkin:
▪️Yorug‘lik manbai: Ksenon gazidan avtomobillarning faralari, kinoproektorlar va kameralar uchun kuchli yorug‘lik chiqaruvchi manba sifatida foydalaniladi. Ksenon lampalari kuchli yorqinligi bilan mashhur.
▪️Tibbiyotda qo‘llanilishi: Ksenon tibbiyotda narkoz moddalari tarkibida qo‘llaniladi. U xavfsiz va oson chiqariladigan anestezik modda hisoblanadi, bu esa uni jarrohlik amaliyotlarida foydali qiladi.
▪️Kosmos texnologiyasida qo‘llanilishi: Ksenon ion dvigatellari uchun yoqilg‘i sifatida kosmos tadqiqotlarida ishlatiladi. U juda samarali yoqilg‘i bo‘lib, koinot kemalarini uzoq masofalarga harakatlantirishda yordam beradi.
▪️Gazlashgan atmosfera: Ksenon Yerdagi atmosferada juda kam uchraydi. U havoning taxminan 0,0000087 foizini tashkil etadi, bu uni qimmatli va noyob gazga aylantiradi.
▪️Inert gazlar oilasi: Ksenon kimyoviy reaksiyalarga juda kam kirishadi, chunki u inert gazlar oilasiga mansub. Biroq, ba’zi maxsus sharoitlarda u boshqa moddalardan birikmalar hosil qilishi mumkin.
▪️Tibbiy tasvir olishda foydalaniladi: Ksenon MRI (magnetik-rezonansli tasvirlash) uskunasida o‘pkalar va boshqa organlar holatini tasvirlashda yordam beruvchi kontrast modda sifatida ishlatiladi.
▪️Noyob va qimmat: Ksenon tabiiy gazlar orasida eng noyob va qimmat hisoblanadi. Shu sababli, uning sanoat va tibbiyotdagi qo‘llanilishi cheklangan.""")

        elif belgi.lower() == "cs":
           print("""Seziy (Cs)
▪️Seziy – davriy jadvalning 55-elementi bo‘lib, ishqoriy metallar guruhiga kiradi. Quyidagi qiziqarli faktlar seziy haqida sizni qiziqtirishi mumkin:
▪️Eng yumshoq metall: Seziy – eng yumshoq metallardan biri bo‘lib, xona haroratida hatto pichoq bilan ham oson kesiladi. U o‘zining past erish nuqtasi bilan ham ajralib turadi – 28,5 °C da suyuqlanadi.
▪️Atom soatlari: Seziy atomlari atom soatlarida qo‘llaniladi. Bu soatlar eng yuqori aniqlikka ega bo‘lib, ular faqat million yillar davomida bir soniyadan kam xatolikka yo‘l qo‘yadi. Atom soatlari zamonaviy navigatsiya va kommunikatsiya tizimlarida muhim ahamiyatga ega.
▪️Yuqori reaktivlik: Seziy juda reaktiv element bo‘lib, suv bilan reaksiyaga kirishganda kuchli portlash sodir bo‘ladi. Shu sababli, u odatda mineral moyda saqlanadi.
▪️Tibbiyotda qo‘llanilishi: Seziy radioaktiv izotoplari tibbiyotda, xususan, saraton kasalliklarini davolashda qo‘llaniladi. U gamma nurlari chiqarish orqali o‘simta hujayralarini yo‘q qiladi.
▪️Elektron qurilmalarda foydalanish: Seziyning fotoemisiyaga ega bo‘lgan xususiyati uni elektron qurilmalarda, ayniqsa, fotoelektrik hujayralarda qo‘llashga imkon beradi. Bu hujayralar yorug‘lik energiyasini elektr energiyasiga aylantiradi.
▪️Quyosh batareyalari uchun material: Seziy quyosh batareyalarida ham qo‘llaniladi, ayniqsa, yuqori samaradorlikka ega bo‘lgan fotoelektrik elementlar yaratishda.
▪️Sanoatda qo‘llanilishi: Seziy neft va gaz sanoatida ham qo‘llaniladi. U burg‘ulash jarayonida quduqlarni samarali tozalash uchun ishlatiladi va shu orqali quduqni chuqurroq ochishga imkon beradi.""")

        elif belgi.lower() == "ba":
           print("""Bariy (Ba)
▪️Bariy – davriy jadvalning 56-elementi bo‘lib, ishqoriy yer metallari guruhiga kiradi. Quyidagi qiziqarli faktlar bariy haqida sizni qiziqtirishi mumkin:
▪️Yonuvchan metall: Bariy juda reaktiv va yonuvchan metall bo‘lib, u havo bilan tezda reaksiyaga kirishadi va yonadi. Shu sababli, uni odatda moy yoki gazsiz muhitda saqlash kerak bo‘ladi.
▪️Tibbiyotda qo‘llanilishi: Bariy sulfat tibbiy tasvir olishda kontrast modda sifatida ishlatiladi. U asosan rentgen va boshqa tasvirlash usullarida ichki organlar, ayniqsa, oshqozon-ichak tizimini kuzatish uchun qo‘llaniladi.
▪️Pirotexnika: Bariy tuzlari pirotexnika sanoatida yashil rangli alanga hosil qilish uchun ishlatiladi. Ushbu xususiyati tufayli, bariy ko‘pincha mushakbozliklarda foydalaniladi.
▪️Shisha va keramika sanoatida: Bariy shisha va keramika sanoatida ishlatiladi. Uning oksidi (BaO) maxsus shisha turlarini ishlab chiqarishda ishlatiladi, bu esa yorug‘lik sinishini yaxshilaydi va shisha mustahkamligini oshiradi.
▪️Radiatsiyaga qarshi himoya: Bariy yuqori zichlikka ega bo‘lganligi uchun radiatsiya ekranlarida ishlatiladi. Bariy bilan to‘ldirilgan materiallar rentgen nurlaridan himoya qilish uchun foydalaniladi.
▪️Bariyning reaktivligi: Bariy suv bilan juda kuchli reaksiyaga kirishib, vodorod gazi chiqaradi va issiqlik hosil qiladi. Shu sababli, bariy suvdan uzoqda saqlanishi kerak.
▪️Yadro sanoatida qo‘llanilishi: Bariy yadro sanoatida qo‘llaniladi, chunki uning ba’zi izotoplari yadro quvvat qurilmalarida reaktsiyalarni boshqarishda yordam beradi.
""")

        elif belgi.lower() == "la":
           print("""Lantan (La)
▪️Lantan – davriy jadvalning 57-elementi bo‘lib, lantanidlar guruhining birinchi elementi hisoblanadi. Quyidagi qiziqarli faktlar lantan haqida sizni qiziqtirishi mumkin:
▪️Oson qayta ishlanadigan metall: Lantan – kumushrang oq metall bo‘lib, yumshoq va oson qayta ishlanadi. Bu xususiyati tufayli, u turli qotishmalar yaratishda qo‘llaniladi.
▪️Katalizator sifatida qo‘llanilishi: Lantan neftni qayta ishlashda katalizator sifatida keng qo‘llaniladi. Uning birikmalari neftdan benzin ishlab chiqarishda jarayonni tezlashtiradi va samaradorligini oshiradi.
▪️Optik shisha ishlab chiqarishda: Lantan oksidi maxsus optik shisha turlarini yaratishda ishlatiladi. Ushbu shisha yuqori sifatli kameralar, teleskoplar va mikroskoplar linzalarini yaratishda qo‘llaniladi.
▪️Gibrid avtomobillarning batareyalarida: Lantan nikelli metall gidrid (NiMH) batareyalarining asosiy komponentlaridan biri hisoblanadi. Ushbu batareyalar, asosan, gibrid avtomobillarda qo‘llanilib, ular yuqori energiya sig‘imi va uzoq muddat xizmat qilish xususiyatiga ega.
▪️Yuqori issiqlikka chidamliligi: Lantanli qotishmalar yuqori haroratlarda o‘z mustahkamligini saqlab qoladi, shu sababli u reaktiv dvigatellar va boshqa yuqori haroratda ishlovchi qurilmalarda keng qo‘llaniladi.
▪️Kamdan kam uchraydi: Lantan tabiatda nisbatan kam uchraydigan elementlardan biri bo‘lib, yer po‘stining taxminan 0,003 foizini tashkil etadi. Biroq, u asosan fosfatlar va karbonatlar shaklida uchraydi.
▪️Televidenie texnologiyasida foydalaniladi: Lantan oksidi eski turdagi katodli-nur trubkali (CRT) televizor ekranlarida ishlatilgan. U yorqin tasvirlar hosil qilishga yordam beradi.""")

        elif belgi.lower() == "ce":
            print("""Seriy (Ce)
▪️Seriy – davriy jadvalning 58-elementi bo‘lib, lantanidlar guruhiga kiradi va eng keng tarqalgan noyob yer metallardan biri hisoblanadi. Quyidagi qiziqarli faktlar seriy haqida sizni qiziqtirishi mumkin:
▪️Eng ko‘p uchraydigan lantanid: Seriy lantanidlar ichida yer po‘stida eng ko‘p uchraydigan elementdir. U yer po‘stining taxminan 0,0046 foizini tashkil etadi va turli minerallarda uchraydi.
▪️Katalitik konvertorlarda qo‘llanilishi: Seriy avtomobillarning katalitik konvertorlarida ishlatiladi. U zararli gazlar, xususan, karbonat angidrid va azot oksidlarini zararsizlantirishda yordam beradi. Bu avtomobillarni ekologik toza qilishda muhim rol o‘ynaydi.
▪️Oksidining ajoyib xususiyatlari: Seriy oksidi (CeO₂) juda samarali abraziv modda hisoblanadi va shisha sayqallashda keng qo‘llaniladi. Shuningdek, bu oksid yorug‘likni yutish va qaytarish xususiyatiga ega bo‘lib, optik linzalarda ham qo‘llaniladi.
▪️Olov yoqish uchun foydalaniladi: Seriy ferroseriy qotishmasining asosiy komponenti hisoblanadi. Bu qotishma oson uchqun chiqaradi, shu sababli u zažigalka va olov yoqish qurilmalarida keng ishlatiladi.
▪️Yadro reaktorlarida foydalaniladi: Seriy ba’zi izotoplari yadro reaktorlarida neytronlarni yutuvchi moddalar sifatida qo‘llaniladi. Bu yadro reaktsiyalarini boshqarish va xavfsizligini ta’minlashda yordam beradi.
▪️Quyosh batareyalari va yoqilg‘i hujayralarida: Seriy dioksidi ba’zan quyosh batareyalari va yoqilg‘i hujayralarida ishlatiladi, chunki u energiyani samarali uzatishga yordam beradi.
▪️Rangli ekranlarda qo‘llanilishi: Seriy birikmalari eski televizor ekranlarida va rangli monitorlarda ranglarni yanada yorqinroq qilish uchun ishlatilgan.""")

        elif belgi.lower() == "pr":
           print("""Prazeodim (Pr)
▪️Prazeodim – davriy jadvalning 59-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar prazeodim haqida sizni qiziqtirishi mumkin:
▪️Magnit va elektrotexnik qotishmalar: Prazeodim kuchli magnit qotishmalar yaratishda ishlatiladi. Bu qotishmalar yuqori samarali magnitlar va elektrotexnik qurilmalarda qo‘llaniladi, masalan, generatorlar va elektr dvigatellarida.
▪️Shisha va sirlarni bo‘yashda: Prazeodim birikmalari sariq va yashil rang hosil qiladi, shu sababli u shisha va keramika sirlarini bo‘yashda keng qo‘llaniladi. Shuningdek, u optik linzalarni quyosh nurlaridan himoya qilishda ham ishlatiladi.
▪️Neodim bilan birgalikda magnitlarda: Prazeodim ko‘pincha neodim bilan birgalikda kuchli magnitlarni yaratishda ishlatiladi. Ushbu magnitlar turli sanoat sohalarida, xususan, avtomobilsozlik va elektronika sanoatida keng qo‘llaniladi.
▪️Aviatsiya sanoatida qo‘llanilishi: Prazeodim alyuminiy qotishmalarida qo‘llanilib, bu qotishmalarni bardoshli va yengil qiladi. Bu xususiyati uni aviatsiya sanoatida muhim materialga aylantiradi.
▪️Yorug‘lik filtrlari uchun material: Prazeodimning kimyoviy birikmalari yorug‘lik filtrlarini yaratishda qo‘llaniladi. Ushbu filtrlar yorug‘likni ma’lum to‘lqin uzunliklarida yutib, ko‘zoynaklar va optik asboblar uchun qo‘llanadi.
▪️Yadro sanoatida foydalanish: Prazeodimning ayrim izotoplari yadro sanoatida, xususan, neytron yutuvchi modda sifatida qo‘llaniladi. Bu yadro reaktsiyalarini boshqarishda yordam beradi.
▪️Kuchli elektrokimyoviy faollik: Prazeodim oson ionlashadi va elektrokimyoviy reaktsiyalarda faol qatnashadi. Bu xususiyati uni elektrotexnik va kimyoviy qo‘llanmalarda foydali qiladi.
""")

        elif belgi.lower() == "nd":
           print("""Neodim (Nd)
▪️Neodim – davriy jadvalning 60-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar neodim haqida sizni qiziqtirishi mumkin:
▪️Kuchli magnit qotishmalar: Neodim magnit qotishmalari ishlab chiqarishda muhim rol o‘ynaydi. Neodimli magnitlar eng kuchli doimiy magnitlar hisoblanadi va ular turli elektrotexnik qurilmalarda, masalan, elektr dvigatellarida va qattiq disk drayvlarida qo‘llaniladi.
▪️Lazer texnologiyalarida qo‘llanilishi: Neodim kristallarida lazerlar yaratiladi. Ushbu lazerlar meditsina, sanoat va ilmiy sohalarda, masalan, jarrohlikda yoki kesish va payvandlash jarayonlarida keng qo‘llaniladi.
▪️Neodim stakani: Neodim birikmalari shishalarni binafsha yoki ko‘k rangga bo‘yashda ishlatiladi. Bunday shisha turli optik asboblarda, shu jumladan, quyosh nurlarini filtrlash uchun ishlatiladigan maxsus linzalarda qo‘llaniladi.
▪️Magnit-rezonans tomografiyasi (MRT): Neodim magnitlari tibbiyotda, ayniqsa, magnit-rezonans tomografiyasi uskunalarida ham qo‘llaniladi. Bu texnologiya ichki organlarni tasvirlashda yuqori aniqlikni ta’minlaydi.
▪️Aviatsiya va avtomobilsozlikda: Neodim kuchli va yengil qotishmalar yaratishda ishlatiladi, bu esa uni aviatsiya va avtomobilsozlik sanoati uchun muhim materialga aylantiradi.
▪️Energetika sanoatida foydalanish: Neodimli magnitlar shamol turbinalari va boshqa qayta tiklanadigan energiya manbalarida qo‘llaniladi. Ular energiya ishlab chiqarish samaradorligini oshiradi.
▪️Yadro texnologiyalarida qo‘llanilishi: Neodimning ayrim izotoplari yadro sanoatida ishlatiladi. U neytron yutuvchi modda sifatida yadro reaktsiyalarini boshqarishda yordam beradi.
""")

        elif belgi.lower() == "pm":
           print("""Prometiy (Pm)
▪️Prometiy – davriy jadvalning 61-elementi bo‘lib, lantanidlar guruhiga kiradi va radioaktiv kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar prometiy haqida sizni qiziqtirishi mumkin:
▪️Radioaktivlik xususiyati: Prometiy tabiiy holatda yer yuzida juda kam uchraydi va asosan yadroviy reaktorlarda sun’iy ravishda olinadi. Uning barcha izotoplari radioaktivdir, ya’ni vaqt o‘tishi bilan boshqa elementlarga aylanishi mumkin.
▪️Batareyalarda qo‘llanilishi: Prometiyning ba’zi izotoplari, xususan, Pm-147, uzoq muddat ishlaydigan yadro batareyalarida foydalaniladi. Bu batareyalar uzoq muddat energiya kerak bo‘lgan qurilmalarda, masalan, sun’iy yo‘ldoshlar va kosmik apparatlarda qo‘llaniladi.
▪️Luminestsent materiallarda: Prometiy birikmalari yorug‘lik chiqaradigan materiallar sifatida foydalaniladi. Bu materiallar, asosan, soat raqamlarini yoritishda yoki yo‘l belgilari va boshqa ko‘rsatmalarda qo‘llaniladi.
▪️Tibbiy asbob-uskunalarda: Prometiy izotoplari ba’zan tibbiyot sohasida, xususan, ko‘z va teri kasalliklarini davolashda, radioaktiv nurlanish manbai sifatida qo‘llaniladi.
▪️Ilmiy tadqiqotlarda foydalanish: Prometiy o‘zining radioaktivligi tufayli ilmiy tajribalarda, xususan, radioaktiv parchalanish jarayonlarini o‘rganishda qo‘llaniladi.
▪️Elektr energiyasini ishlab chiqarish: Prometiyning radioaktiv parchalanishi natijasida hosil bo‘ladigan issiqlik kichik miqdordagi elektr energiyasini ishlab chiqarishda ishlatilishi mumkin, bu esa kichik kuchlanishli energiya manbalarida qo‘llaniladi.
▪️Tabiatda kam uchrashi: Prometiy yer qobig‘ida juda kam uchraydi, shuning uchun uni sanoatda foydalanish cheklangan va asosan laboratoriyalarda sintez qilinadi.""")

        elif belgi.lower() == "sm":
           print("""Samariy (Sm)
▪️Samariy – davriy jadvalning 62-elementi bo‘lib, lantanoidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar samariy haqida sizni qiziqtirishi mumkin:
▪️Samariy kobalt magnitlari: Samariy kuchli doimiy magnitlar, ayniqsa, samariy-kobalt qotishmasi asosida yaratilgan magnitlar ishlab chiqarishda ishlatiladi. Bu magnitlar yuqori harorat va og‘ir sharoitlarda ham samarali ishlaydi, masalan, aerokosmik va mudofaa sanoatida.
▪️Neytron yutuvchi moddalar: Samariy yadroviy reaktorlarda neytron yutuvchi modda sifatida qo‘llaniladi. Bu uning izotoplarining neytronlarni yaxshi yutish qobiliyatiga ega bo‘lishi bilan bog‘liq bo‘lib, yadro reaktsiyalarini boshqarishda muhim rol o‘ynaydi.
▪️Optik linzalarda va shishalarda: Samariy birikmalari optik shishalarni bo‘yashda qo‘llaniladi. U maxsus linzalarga sariq rang beradi va bu linzalar ko‘zoynaklar, kameralar va boshqa optik asboblar uchun ishlatiladi.
▪️Yadro sanoatida foydalanish: Samariyning izotoplari, xususan, Sm-149, neytronlarni yuqori darajada yutishi tufayli yadro reaktorlarida qo‘llaniladi. Bu yadro reaktorlarini yanada samarali va xavfsiz ishlashiga yordam beradi.
▪️Rentgen nurlanishi manbalari: Samariy radioaktiv izotoplari rentgen nurlari manbasi sifatida ishlatiladi. Bu tibbiy va texnik diagnostika uskunalarida qo‘llaniladi.
▪️O‘ta past haroratlarda foydalanish: Samariy birikmalari kriogenik uskunalarda, ya’ni juda past haroratlarda ishlatiladigan qurilmalarda foydalaniladi. Bu uskunalar ilmiy tadqiqotlarda va sanoatda qo‘llaniladi.
▪️Luminestsent xususiyatlar: Samariyning ayrim birikmalari yorug‘lik chiqarish qobiliyatiga ega. Ular turli maqsadlarda, jumladan, optik signallar va indikatorlarda foydalaniladi.""")

        elif belgi.lower() == "eu":
           print("""Yevropiy (Eu)
▪️Yevropiy – davriy jadvalning 63-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar yevropiy haqida sizni qiziqtirishi mumkin:
▪️Luminestsent xususiyatlari: Yevropiy birikmalari o‘zining yorqin luminestsent xususiyatlari bilan mashhur. U televizor va monitor ekranlarida ko‘k va qizil ranglarni yaratishda qo‘llaniladi. Shuningdek, u yorug‘lik diodlarida (LED) va flüoresan chiroqlarda ishlatiladi.
▪️Yadro reaktorlarida foydalanish: Yevropiyning ayrim izotoplari, xususan, Eu-151 va Eu-153, yadroviy reaktorlarda neytron yutuvchi modda sifatida qo‘llaniladi. Bu uning yadro reaktorlarini samarali boshqarishga yordam berish qobiliyatini oshiradi.
▪️Qizil fosforlarda qo‘llanilishi: Yevropiy birikmalari qizil fosforlar ishlab chiqarishda qo‘llaniladi, ayniqsa, televizor ekranlari va monitorlarida yuqori sifatli tasvir yaratish uchun.
▪️Tibbiyotda qo‘llanilishi: Yevropiy izotoplari meditsina sohasida ham foydalaniladi, jumladan, radioaktiv diagnostika uskunalarida va davolash jarayonlarida.
▪️Rentgen va flüoresan texnologiyalarida: Yevropiy radioaktiv izotoplari flüoresan va rentgen texnologiyalarida manba sifatida ishlatiladi, bu texnologiyalar ilmiy tadqiqotlar va diagnostikada muhim rol o‘ynaydi.
▪️Yevropiy izotoplari: Yevropiyning tabiiy va sun’iy izotoplari ilmiy tadqiqotlar uchun qimmatli materiallardir, ular yadro tadqiqotlarida va yangi texnologiyalarni ishlab chiqishda qo‘llaniladi.
""")

        elif belgi.lower() == "gd":
           print("""Gadoliniy (Gd)
▪️Gadoliniy – davriy jadvalning 64-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar gadoliniy haqida sizni qiziqtirishi mumkin:
▪️Magnit xususiyatlari: Gadoliniy o‘zining kuchli magnit xususiyatlari bilan ajralib turadi. Ayniqsa, gadoliniy-titan va gadoliniy-kobalt qotishmalari yuqori magnit o‘tkazuvchanlikka ega bo‘lib, turli sanoat va ilmiy texnologiyalarda qo‘llaniladi.
▪️Tibbiyotda foydalanish: Gadoliniy birikmalari magnit-rezonans tomografiyasida (MRT) kontrast modda sifatida keng qo‘llaniladi. Bu gadoliniyning magnit maydonlarga sezgirligi bilan bog‘liq bo‘lib, tibbiy diagnostika jarayonlarini yaxshilashga yordam beradi.
▪️Neytron yutuvchi modda: Gadoliniy yadroviy reaktorlarda neytron yutuvchi modda sifatida foydalaniladi. Uning yuqori neytron yutish qobiliyati yadro reaktorlarini samarali boshqarishga yordam beradi.
▪️Yorug‘lik chiqaruvchi materiallar: Gadoliniy birikmalari luminestsent xususiyatlarga ega bo‘lib, yorug‘lik diodlari (LED) va flüoresan lampalarda keng qo‘llaniladi. Bu birikmalar yorqin ranglarni yaratishga qodir.
▪️Yadro qurollarida himoya modda: Gadoliniy yadroviy qurollar va reaktorlar xavfsizligini ta’minlash uchun ishlatiladi, chunki u neytron yutish orqali yadroviy reaktsiyalarni boshqarishga yordam beradi.
▪️Kriogenika sohasida: Gadoliniy birikmalari o‘ta past haroratli qurilmalarda, ya’ni kriogenika sohasida foydalaniladi. Bu uskunalar ilmiy tajribalar va texnologik ishlanmalarda qo‘llaniladi.
▪️Ilmiy tadqiqotlarda foydalanish: Gadoliniyning magnit va yadro xususiyatlari uni ilmiy tajribalarda muhim materialga aylantiradi. Uning neytron yutish va magnit sezgirligi ko‘plab ilmiy tadqiqotlar uchun qimmatlidir.""")

        elif belgi.lower() == "tb":
           print("""Terbiy (Tb)
▪️Terbiy – davriy jadvalning 65-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar terbiy haqida sizni qiziqtirishi mumkin:
▪️Luminestsent xususiyatlari: Terbiy birikmalari yashil rangdagi luminestsent xususiyatlarga ega. U yorug‘lik diodlari (LED) va flüoresan chiroqlarida yashil rang hosil qilish uchun qo‘llaniladi. Ayniqsa, televizor va monitor ekranlarida ishlatiladigan fosforlar tarkibida terbiy muhim rol o‘ynaydi.
▪️Magnit qotishmalarda qo‘llanilishi: Terbiy magnit xususiyatlarga ega bo‘lib, kuchli magnit materiallar yaratishda ishlatiladi. Ayniqsa, terbiy-kobalt qotishmasi yuqori samarali magnitlarni yaratishda qo‘llaniladi.
▪️Yorug‘lik chiqaruvchi keramikalarda: Terbiy birikmalari keramikalarda foydalaniladi. Ushbu keramik materiallar ko‘pincha yuqori samarali yorug‘lik manbalari, masalan, LED va lazerni yaratishda qo‘llaniladi.
▪️Tibbiyotda foydalanish: Terbiyning ayrim radioaktiv izotoplari tibbiy diagnostikada, ayniqsa, qiyosiy tomografiya va radioterapiya sohasida kontrast modda sifatida ishlatiladi.
▪️Neytron yutuvchi modda: Terbiy yadroviy reaktorlarda neytron yutuvchi modda sifatida ishlatiladi. Uning yuqori neytron yutish qobiliyati yadro reaktorlarini samarali boshqarishga yordam beradi.
▪️Yuqori haroratli o‘tkazuvchilar: Terbiy yuqori haroratli o‘tkazuvchi materiallar sifatida ishlatilishi mumkin. Bu materiallar turli ilmiy va texnologik sohalarda, xususan, energiya va elektronika sanoatida qo‘llaniladi.
▪️Lazer texnologiyasida qo‘llanilishi: Terbiyning optik va luminestsent xususiyatlari uni lazer texnologiyasida muhim materialga aylantiradi. Lazerlar va optik qurilmalarda yuqori samarali material sifatida qo‘llaniladi.
""")

        elif belgi.lower() == "dy":
           print("""Disprosiy (Dy)
▪️Disprosiy – davriy jadvalning 66-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar disprosiy haqida sizni qiziqtirishi mumkin:
▪️Yuqori magnit xususiyatlari: Disprosiy magnit xususiyatlariga ega bo‘lib, kuchli magnit qotishmalar yaratishda qo‘llaniladi. Ayniqsa, disprosiy va neodim qotishmalari yuqori samarali magnitlarni yaratishda foydalaniladi. Bu qotishmalar elektr dvigatellari va generatorlar kabi yuqori magnit talab qiladigan texnologiyalarda qo‘llaniladi.
▪️Yadro sanoatida qo‘llanilishi: Disprosiyning neytron yutuvchi xususiyati uni yadroviy reaktorlarda ishlatish uchun muhim modda qiladi. Bu element reaktorlarning barqaror ishlashini ta'minlashda muhim rol o‘ynaydi.
▪️Yuqori haroratli o‘tkazuvchilar: Disprosiy yuqori haroratlarda yaxshi o‘tkazuvchanlikka ega materiallarga kiritiladi. Bu xususiyati uni energiya va elektronika sanoatlarida qimmatli materialga aylantiradi.
▪️Tibbiyotda foydalanish: Disprosiyning radioaktiv izotoplari tibbiy diagnostikada, xususan, radioaktiv terapiya va qo‘shimcha tahlillar uchun qo‘llaniladi.
▪️Luminestsent xususiyatlari: Disprosiy birikmalari luminestsent materiallar yaratishda ishlatiladi, ayniqsa, qizil va sariq rangdagi fosforlar sifatida. Bu xususiyati uni yorug‘lik manbalari, LED texnologiyalari va optik asboblarda keng qo‘llaniladigan materialga aylantiradi.
▪️Aviatsiya sanoatida: Disprosiy alyuminiy qotishmalarida qo‘llanilib, qotishmalarni yengil va bardoshli qiladi. Bu qotishmalar aviatsiya sanoatida keng qo‘llaniladi.
▪️Lazer texnologiyalarida: Disprosiy birikmalari optik va lazer texnologiyalarida qo‘llaniladi. U yuqori samarali lazerlar yaratishda foydali modda bo‘lib xizmat qiladi.""")

        elif belgi.lower() == "ho":
            print("""Golmiy (Ho)
▪️Golmiy – davriy jadvalning 67-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar golmiy haqida sizni qiziqtirishi mumkin:
▪️Yuqori magnit xususiyatlari: Golmiy kuchli magnit xususiyatlariga ega. U magnit qotishmalarda ishlatiladi va yuqori samarali magnitlarni yaratish uchun foydalidir. Golmiy, ayniqsa, magnit materiallar ishlab chiqarishda ishlatiladi.
▪️Tibbiyotda qo‘llanilishi: Golmiy birikmalari tibbiy diagnostika va terapiyada ishlatiladi. Xususan, golmiy-166 izotopi, radioterapiya jarayonida o‘tkazgich sifatida qo‘llaniladi.
▪️Lazer texnologiyalarida: Golmiy, lazer texnologiyalarida ham muhim rol o‘ynaydi. U golmiy lazerlar yaratishda ishlatiladi, bu lazerlar tibbiy va sanoat qo‘llanmalarida keng foydalaniladi.
▪️Yadro sanoatida: Golmiy, yadroviy reaktorlarda neytron yutuvchi modda sifatida foydalaniladi. Uning yutish xususiyati yadro reaktsiyalarini boshqarishga yordam beradi.
▪️Kriogenik dasturlar: Golmiy, o‘ta past haroratli muhitlarda foydalanishga mo‘ljallangan materiallarga kiritiladi. Bu xususiyati, uni ilmiy tadqiqotlar va texnologiyalarda muhim qiladi.
▪️Optik asboblarda qo‘llanilishi: Golmiy, optik asboblar va elektron qurilmalarda ishlatiladigan material sifatida qo‘llaniladi. Bu xususiyati, uni turli xil optik texnologiyalar va asboblar ishlab chiqarishda foydali qiladi.
▪️Yuqori energiyali materiallar: Golmiy birikmalari yuqori energiya bilan bog‘liq bo‘lgan muhandislik va ilmiy tadqiqotlarda muhim material sifatida xizmat qiladi.
""")

        elif belgi.lower() == "er":
           print("""Erbiy (Er)
▪️Erbiy – davriy jadvalning 68-elementi bo‘lib, lantanidlar guruhiga kiradi va kamyob yer metallaridan biridir. Quyidagi qiziqarli faktlar erbiy haqida sizni qiziqtirishi mumkin:
▪️Yuqori magnit xususiyatlari: Erbiy kuchli magnit xususiyatlariga ega bo‘lib, yuqori samarali magnit qotishmalar yaratishda qo‘llaniladi. Erbiy, ayniqsa, magnit materiallar ishlab chiqarishda muhimdir.
▪️Lazer texnologiyalarida: Erbiy, lazer texnologiyalarida keng qo‘llaniladi. U lazerlarda ishlatiladigan aktiv muhit sifatida xizmat qiladi va qizil rangli lazerlarni ishlab chiqarishda qo‘llaniladi.
▪️Tibbiyotda foydalanish: Erbiyning birikmalari tibbiy asboblar va diagnostika jarayonlarida qo‘llaniladi. Xususan, u radioterapiya jarayonida foydalidir.
▪️Shisha va keramika sanoatida: Erbiy birikmalari shisha va keramika mahsulotlarini bo‘yashda ishlatiladi. Bu ranglar asosan qizil va pushti ranglarda bo‘ladi.
▪️Yadro sanoatida: Erbiy, yadroviy reaktorlarda neytron yutuvchi modda sifatida ishlatiladi. Bu xususiyati yadro reaktsiyalarini boshqarishda yordam beradi.
▪️Optik asboblarda qo‘llanilishi: Erbiy, optik asboblar va elektron qurilmalarda ishlatiladigan material sifatida muhimdir. Bu xususiyati, uni turli xil optik texnologiyalar va asboblar ishlab chiqarishda foydali qiladi.
▪️Kimyoviy xususiyatlari: Erbiy oson ionlashadigan elementlardan biri bo‘lib, turli kimyoviy reaktsiyalarda faol qatnashadi. Bu xususiyati uni elektrotexnika va kimyo sanoatlarida qo‘llaniladigan material sifatida muhim qiladi.""")

        elif belgi.lower() == "tm":
           print("""Tuliy (Tm)
▪️Tuliy – davriy jadvalning 69-elementi bo‘lib, uning nomi Skandinaviya mintaqasidagi qadimiy nom "Tuliya" sharafiga qo‘yilgan. Bu kamyob yer metallaridan biri bo‘lib, boshqa elementlardan farqli xususiyatlarga ega.
▪️Tuliy kam miqdorda topilgan bo‘lsa ham, uning yetarlicha o‘rganilmagan jihatlari mavjud. U 1879-yilda shved kimyogari Per Teodor Kleve tomonidan kashf etilgan va o‘zining noyob tabiati bilan olimlarni hayratga solgan.
▪️Magnetitda yashirinib yotgan: Tuliy yer qobig‘ida juda kam uchraydi, va bu elementni sof holda ajratish qiyin. Asosan, magnetit kabi minerallarda uchraydi. Ushbu minerallar qazib olinib, tuliy elementini ajratib olish jarayoni juda murakkab va xarajatli.
▪️Yorug‘lik va to‘lqinlar: Tuliy optik tolalar ishlab chiqarishda, ayniqsa, lazer texnologiyalarida ishlatiladi. U infraqizil to‘lqinlarni hosil qiluvchi qimmatbaho aktiv muhit sifatida xizmat qiladi. Bu xususiyat tibbiyotda lazer davolash usullarida muhim rol o‘ynaydi.
▪️Tuliyning kelajagi: Bugungi kunda tuliyning sanoat miqyosida keng qo‘llanilishi unchalik rivojlanmagan bo‘lsa-da, uning noyob xususiyatlari yangi texnologiyalar uchun katta potensialga ega. Tuliy lazerlar, tibbiyot texnologiyalari va boshqa zamonaviy sohalarda yangi imkoniyatlar yaratishi mumkin.
""")

        elif belgi.lower() == "yb":
           print("""Itterbiy (Yb)
▪️Itterbiy – davriy jadvalning 70-elementi bo‘lib, lantanidlar guruhiga kiradi. Element o‘z nomini Shvetsiyaning Itterbi shahridan olgan va kamyob yer metallaridan biridir.
▪️Minerallar orasidagi sir: Itterbiy boshqa elementlar bilan ko‘plab aralashmalar hosil qiladi va odatda minerallar tarkibida uchraydi. Uni ajratib olish jarayoni murakkab bo‘lsa-da, u sanoat uchun qimmatli resurs hisoblanadi.
▪️Fazoviy o‘zgaruvchanlik: Itterbiy uchta kristall fazaga ega, bu uni fazalar o‘rtasidagi o‘zgarishlarni o‘rganishda qiziqarli ob’ektga aylantiradi. Ayniqsa, uning fizik xususiyatlari harorat va bosimga bog‘liq ravishda sezilarli darajada o‘zgarishi bilan ajralib turadi.
▪️Supero‘tkazuvchanlikdagi roli: Itterbiy yarim o‘tkazgichli texnologiyalar va supero‘tkazuvchi materiallar yaratishda foydali hisoblanadi. Uning qotishmalari elektr qarshiligini kamaytirishga yordam beradi va yuqori texnologiyali asbob-uskunalarda qo‘llaniladi.
▪️Tibbiyotdagi qo‘llanilishi: Itterbiyning radioaktiv izotoplari tibbiyotda, xususan, saraton kasalligini aniqlashda ishlatiladi. Bu izotoplar yordamida xavfli o‘simtalarni aniqlash va ularni davolash imkoniyati oshadi.
▪️Optik texnologiyalar: Itterbiy, ayniqsa, lazer texnologiyalarida qo‘llaniladi. Itterbiy-lazerlar yuqori energiyali va samarali bo‘lib, optik tola aloqa tizimlarida ishlatiladi.
""")

        elif belgi.lower() == "lu":
           print("""Lutetsiy (Lu)
▪️Lutetsiy – davriy jadvalning 71-elementi bo‘lib, lantanidlar qatorining oxirgi elementi hisoblanadi. U o‘zining noyob fizik va kimyoviy xususiyatlari bilan ajralib turadi.
▪️Nomining kelib chiqishi: Lutetsiyning nomi qadimgi Rimning Lutetia shahridan kelib chiqqan (hozirgi Parij). Bu element 1907-yilda fransuz kimyogari Jorj Urbain tomonidan kashf qilingan.
▪️Tibbiyotda yuqori samaradorlik: Lutetsiy izotoplari, xususan, 177Lu izotopi, saraton terapiyasida muhim ahamiyatga ega. U o‘simtalarni nurlantirish orqali ularning rivojlanishini to‘xtatadi va zamonaviy onkologiya davolash usullarining asosini tashkil qiladi.
▪️Eng qattiq lantanid: Lutetsiy lantanidlar orasida eng zich va qattiq bo‘lib, mexanik jihatdan bardoshlidir. Bu xususiyat uni yuqori kuch talab qilinadigan sanoat jarayonlarida ishlatishga imkon beradi.
▪️Ne’matli metallar qatorida: Lutetsiy kam uchraydi, ammo yuqori bahoga ega. Uning qimmatligi uni qotishmalar va katalizatorlar sifatida ishlatishda cheklov qo‘yadi. Shunga qaramasdan, lutetsiy yuqori sifatli katalizator sifatida kimyo sanoatida va neft qayta ishlashda qo‘llaniladi.
▪️Noyob qo‘llanilish sohalari: Lutetsiy yuqori samarali rentgen nurlanish detektorlari ishlab chiqarishda ishlatiladi. Bu texnologiyalar tibbiy tasvirlash va sanoatning ko‘plab sohalarida qo‘llaniladi.
""")

        elif belgi.lower() == "hf":
           print("""Gafniy (Hf)
▪️Gafniy – davriy jadvalning 72-elementi bo‘lib, d-blok metallari qatoriga kiradi. Bu element o‘zining yuqori issiqlik chidamliligi va kimyoviy barqarorligi bilan mashhur.
▪️Nomining kelib chiqishi: Gafniy 1923-yilda Nils Bor va Jorj de Hevesi tomonidan kashf qilingan va uning nomi qadimgi Kopengagen (Hafnia) sharafiga berilgan.
▪️Yadro sanoatida: Gafniy neytronlarni samarali yutish xususiyatiga ega, shuning uchun u yadroviy reaktorlarda xavfsizlik uchun ishlatiladi. U reaktorda neytron oqimini boshqarishda muhim rol o‘ynaydi.
▪️Superalloylarning asosiy elementi: Gafniy yuqori issiqlikka chidamli qotishmalarda ishlatiladi. Bu qotishmalar raketa dvigatellari va kosmik texnologiyalarda keng qo‘llaniladi, chunki ular ekstremal sharoitlarda o‘z kuchini saqlab qoladi.
▪️Nozik keramika ishlab chiqarishda: Gafniy oksidi (HfO₂) yuqori issiqlik va elektr qarshiligiga ega bo‘lgan keramika materiallarini ishlab chiqarishda qo‘llaniladi. Bu materiallar elektronika va sanoat pechlarida keng qo‘llaniladi.
▪️Optik texnologiyalardagi roli: Gafniy birikmalari optik qoplamalar ishlab chiqarishda ishlatiladi. Ular linzalar va optik uskunalarda yorug‘likni o‘tkazish samaradorligini oshiradi.
▪️O‘rganilmagan imkoniyatlar: Gafniy kamyob element bo‘lishiga qaramasdan, u hali ko‘plab yangi texnologik sohalarda o‘z o‘rnini topishi mumkin. Olimlar gafniyning boshqa ilovalarini o‘rganishda davom etmoqdalar.""")

        elif belgi.lower() == "ta":
           print("""Tantal (Ta)
▪️Tantal – davriy jadvalning 73-elementi bo‘lib, o‘zining yuqori korroziyaga chidamliligi va barqarorligi bilan ajralib turadi. Bu element asosan yuqori texnologiyali qurilmalarda keng qo‘llaniladi.
▪️Nomi afsonadan: Tantalning nomi qadimgi yunon mifologiyasidagi Tangri Zevsning o‘g‘li Tantaldan olingan. Bu nom elementning kimyoviy jihatdan inaktivligi va qiyin eruvchanligini tasvirlash uchun tanlangan.
▪️Elektronika sanoatidagi ahamiyati: Tantal kondensatorlar ishlab chiqarishda keng qo‘llaniladi. Uning elektr sig‘imi va past qarshiligi tufayli, tantal kondensatorlari mobil telefonlar, noutbuklar va boshqa elektron qurilmalarda muhim rol o‘ynaydi.
▪️Tibbiyotda mustahkam material: Tantal biologik jihatdan inert bo‘lib, inson tanasiga mos keladi. U jarrohlik implantantlari va suyaklar o‘rnini bosuvchi protezlar ishlab chiqarishda ishlatiladi. Tantalning bu xususiyati uni tibbiyot sohasida qimmatli materialga aylantiradi.
▪️Korroziyaga chidamli gigant: Tantal hatto yuqori kislotali muhitlarda ham oksidlanmaydi va yemirilmaydi. Shuning uchun u kimyoviy reaktorlar va asboblar ishlab chiqarishda ishlatiladi.
▪️Kosmik texnologiyalarda: Tantal o‘zining yuqori erish harorati va kuchli mexanik xususiyatlari tufayli kosmik texnologiyalarda, raketa va sun’iy yo‘ldosh qismlarini ishlab chiqarishda foydalaniladi.
▪️Kashfiyoti va qo‘llanilish tarixi: Tantal 1802-yilda shved kimyogari Anders Gustav Ekeberg tomonidan kashf etilgan va o‘shandan beri u yuqori texnologiyalarni rivojlantirishda katta ahamiyat kasb etmoqda.
""")

        elif belgi.lower() == "w":
           print("""Volfram (W)
▪️Volfram – davriy jadvalning 74-elementi bo‘lib, o‘zining yuqori zichligi va erish harorati bilan mashhur. Volfram yuqori kuch va issiqlik talab qilinadigan ko‘plab sanoat sohalarida qo‘llaniladi.
▪️Dunyodagi eng yuqori erish harorati: Volfram barcha metallar ichida eng yuqori erish haroratiga ega – 3422 °C. Shu sababli, u yuqori haroratli muhitlarda ishlatiladigan qotishmalar va qismlarda qo‘llaniladi, masalan, raketa dvigatellari va issiqlik ekranlarida.
▪️Chidamlilik va zichlik: Volfram juda zich va qattiq bo‘lib, uning zichligi hatto oltindan ham yuqori. Bu xususiyat uni og‘irligi yuqori bo‘lgan va katta yuklarga chidamli material sifatida ishlatiladigan joylarda muhim qiladi, masalan, harbiy texnika va sanoat asboblarida.
▪️Lampalar va elektronika: Volframning erish harorati yuqori bo‘lgani uchun, u chiroq filamentlari va elektr lampalarda ishlatiladi. Bundan tashqari, u rentgen nurlari hosil qilishda ishlatiladigan katodlar uchun ham zarurdir.
▪️Kesuvchi asboblarda: Volfram karbidi kesuvchi asboblarda keng qo‘llaniladi. Bu qotishma o‘ta qattiqligi va aşinaga chidamliligi bilan mashhur bo‘lib, matkaplar, torna asboblari va frezalarda asosiy komponent hisoblanadi.
▪️Qurollar va zirhlar: Volframning yuqori zichligi va qattiqligi uni harbiy texnikalar, qurollar va zirhlarda qo‘llaniladigan muhim materialga aylantiradi. Bu xususiyatlar uni harbiy ilovalarda qimmatli qiladi.
▪️Tabiiy holatda kam uchraydi: Volfram tabiiy holatda juda kam uchraydi va ko‘pincha minerallar tarkibida uchraydi, masalan, volframit va sheelit. Uni ajratib olish va tozalash jarayoni qiyin bo‘lsa-da, u sanoatda o‘ta zarur materialdir.""")

        elif belgi.lower() == "re":
           print("""Reniy (Re)
▪️Reniy – davriy jadvalning 75-elementi bo‘lib, o‘zining noyob fizik va kimyoviy xususiyatlari bilan mashhur. Bu element yuqori erish harorati va yuqori kuchga ega bo‘lgani uchun zamonaviy texnologiyalarda keng qo‘llaniladi.
▪️Nomi va kashfiyoti: Reniy 1925-yilda nemis kimyogarlar Walter Noddack, Ida Tacke va Otto Berg tomonidan kashf qilingan. Uning nomi Rehn daryosi (Rhein) sharafiga qo‘yilgan.
▪️Yuqori erish harorati: Reniyning erish harorati 3186 °C bo‘lib, uni issiqlikka chidamli qotishmalar yaratishda ideal qiladi. U, ayniqsa, samolyot dvigatellari va gaz turbinalarida foydalaniladigan qotishmalarning ajralmas qismi hisoblanadi.
▪️Katalizator sifatida qo‘llanilishi: Reniy kimyo sanoatida katalizator sifatida keng qo‘llaniladi. U, xususan, neftni qayta ishlash jarayonlarida oktan sonini oshirish uchun ishlatiladi.
▪️Elektron qurilmalarda: Reniy elektron sanoatida ham muhim rol o‘ynaydi. Uning birikmalari elektr kontaktlar va yuqori haroratli dasturlar uchun ishlatiladigan materiallarda qo‘llaniladi.
▪️Platinadan keyingi qimmatbaho element: Reniy dunyodagi eng kam uchraydigan va qimmatbaho metallar qatoriga kiradi. Uning noyobligi va yuqori texnologiyadagi ahamiyati uni iqtisodiy jihatdan muhim elementga aylantiradi.
▪️Supero‘tkazuvchilar va tibbiyot: Reniy qotishmalari supero‘tkazuvchi materiallar yaratishda ishlatiladi. Shuningdek, u radioaktiv izotoplar tayyorlashda va tibbiyotda diagnostika jarayonlarida qo‘llaniladi.""")

        elif belgi.lower() == "os":
            print("""Osmiy (Os)
▪️Osmiy – davriy jadvalning 76-elementi bo‘lib, o‘zining ajoyib zichligi va o‘ta qattiqligi bilan tanilgan. U eng zich element hisoblanadi va ko‘plab sanoat sohalarida noyob xususiyatlari tufayli keng qo‘llaniladi.
▪️Eng zich element: Osmiy zichligi eng yuqori element bo‘lib, uning zichligi 22.59 g/sm³. Bu xususiyat uni og‘irligi katta bo‘lgan va qattiq materiallar ishlab chiqarishda muhim qiladi, masalan, og‘ir yuk ko‘taruvchi texnikalarda va maxsus qotishmalarda.
▪️O‘ta qattiqlik va mexanik chidamlilik: Osmiy yuqori qattiqlikka ega bo‘lib, o‘ta mustahkam qotishmalarda ishlatiladi. U kesuvchi asboblar, burg‘ulash qurilmalari va sanoatning boshqa sohalarida ishlatiladigan qattiq materiallar tarkibiga kiradi.
▪️Zargarlik sanoatidagi roli: Osmiy qimmatbaho metallardan biri bo‘lib, zargarlik buyumlarini mustahkamlash uchun platinaga qo‘shiladi. Bu qotishmalar yuqori chidamlilik va parilash xususiyatiga ega.
▪️Kimyo sanoatida: Osmiy tetraoksidi (OsO₄) organik kimyoda muhim reaktiv hisoblanadi. U organik birikmalarni oksidlovchi vosita sifatida ishlatiladi. Shuningdek, osmiyning bu birikmasi mikroskopiya va tibbiyotda to‘qimalarni bo‘yashda ham qo‘llaniladi.
▪️Tibbiyotda noyob ilovalar: Osmiy izotoplari radioaktiv nurlanishni tadqiq qilish va diagnostika jarayonlarida ishlatiladi. U hali keng o‘rganilmagan, lekin istiqbolli tibbiy texnologiyalar uchun muhim bo‘lishi mumkin.
▪️Kashfiyoti: Osmiy 1803-yilda ingliz kimyogari Smitson Tennant tomonidan kashf qilingan. U platina rudalarini tadqiq qilayotganda osmiyni topgan. Osmiyning nomi yunon tilidagi "osme" (o‘tkir hid) so‘zidan kelib chiqqan, bu uning birikmalaridan biri – osmiy tetraoksidining kuchli hidiga ishora qiladi.""")

        elif belgi.lower() == "ir":
           print("""Iridiy (Ir)
▪️Iridiy – davriy jadvalning 77-elementi bo‘lib, o‘zining yuqori korroziyaga chidamliligi va kuchli qattiqligi bilan tanilgan. Bu element qimmatbaho metallardan biri hisoblanadi va ko‘plab sanoat sohalarida muhim ahamiyatga ega.
▪️Nomi va kashfiyoti: Iridiy 1803-yilda ingliz kimyogari Smitson Tennant tomonidan kashf qilingan. Uning nomi yunoncha "iris" so‘zidan olingan bo‘lib, bu ranglar bilan bog‘liq, chunki iridiy birikmalari rang-barang bo‘ladi.
▪️Korroziyaga chidamlilik: Iridiy korroziyaga juda chidamli bo‘lib, hatto kuchli kislotalar va boshqa kimyoviy muhitlarda ham yemirilmaydi. Bu xususiyat uni sanoat asboblarida va qimmatbaho zargarlik buyumlarida ishlatishni imkoniyatini yaratadi.
▪️Zargarlik sanoatida qo‘llanilishi: Iridiy qimmatbaho metallardan biri sifatida zargarlik buyumlarida ishlatiladi. U platina va boshqa metallarga qo‘shilib, qotishmalar ishlab chiqarishda foydalaniladi, bu esa buyumlarning mustahkamligini oshiradi.
▪️Asboblarda va elektronika: Iridiy, yuqori haroratda ishlash uchun talab qilinadigan asboblar va materiallar tayyorlashda qo‘llaniladi. Shuningdek, elektron qurilmalarda alohida o‘rin tutadi.
▪️O‘ziga xos fizik xususiyatlar: Iridiy juda qattiq va zich metal bo‘lib, uning zichligi 22.56 g/sm³. Bu xususiyatlar uni og‘ir yuklarni ko‘tarish va mexanik kuchni talab qiladigan joylarda foydalanishga mos qiladi.
▪️Geologik tadqiqotlarda: Iridiy er yuzidagi qiyin sharoitlarda ham o‘ta barqaror. Shuning uchun u geologik tadqiqotlarda, jumladan meteoritlar va er yuzidagi qatlamlar o‘rtasida tarqalgan metallni o‘rganishda muhim bo‘ladi.""")

        elif belgi.lower() == "pt":
           print("""Platina (Pt)
▪️Platina – davriy jadvalning 78-elementi bo‘lib, o‘zining yuqori korroziyaga chidamliligi, yumshoqligi va qimmatbaho metall sifatida tanilgan. Platina metall sanoatining asosiy elementlaridan biridir va keng qo‘llaniladi.
▪️Nomi va kashfiyoti: Platina 1735-yilda ispan kimyogari Antonio de Ulloa tomonidan kashf qilingan. Uning nomi ispanchadan kelib chiqib, "kichik oltin" degan ma'noni anglatadi.
▪️Korroziyaga chidamlilik: Platina kislotalarga va boshqa kimyoviy muhitlarga juda chidamli, bu esa uni sanoatda keng qo‘llanadigan materialga aylantiradi. U, masalan, kimyo laboratoriyalarida reaktiv sifatida foydalaniladi.
▪️Zargarlik sanoatida: Platina qimmatbaho zargarlik buyumlari tayyorlashda keng qo‘llaniladi. U, shuningdek, olmos va boshqa qimmatbaho toshlar bilan birgalikda ishlatiladi. Platina zargarlik buyumlariga go‘zallik va qiymat qo‘shadi.
▪️Tibbiyotda: Platina birikmalari tibbiyotda, ayniqsa, saraton kasalliklarini davolashda kimyoviy terapevtik vositalar sifatida ishlatiladi. Platina asosidagi dori vositalari onkologiyada keng qo‘llaniladi.
▪️Avtomobil sanoatida: Platina katalizatorlar tayyorlashda ishlatiladi, bu esa avtomobillarning chiqindi gazlarini tozalash jarayonida muhim ahamiyatga ega. Platina asosidagi katalizatorlar zararli gazlarni kamaytirishda yordam beradi.
▪️Jahon bo‘ylab mavjudligi: Platina dunyoda juda kam uchraydi va asosan Janubiy Afrika, Kolumbiya va Rossiya kabi mamlakatlarda qazib olinadi. Uning noyobligi va qiymati uni iqtisodiy jihatdan muhim elementga aylantiradi.""")

        elif belgi.lower() == "au":
           print("""Oltin (Au)
▪️Oltin (Au) – davriy jadvalning 79-elementi bo‘lib, qimmatbaho metall sifatida keng tanilgan. U o‘zining go‘zalligi, yumshoqligi va kimyoviy barqarorligi bilan ajralib turadi. Oltin asrlar davomida odamlar tomonidan qimmatbaho toshlar bilan birga ishlatilgan.
▪️Zargarlik sanoatidagi ahamiyati: Oltin qimmatbaho zargarlik buyumlarining asosiy materialidir. U uzuklar, bilaguzuklar va boshqa bezaklar tayyorlashda keng qo‘llaniladi, chunki u go‘zallik va qiymatni anglatadi.
▪️Investitsiya vositasi sifatida: Oltin iqtisodiy jihatdan muhim bo‘lib, ko‘plab investorlar tomonidan aktiv sifatida saqlanadi. U global iqtisodiyotda qiymatni saqlash vositasi sifatida tanilgan.
▪️Kimyoviy barqarorlik: Oltin kimyoviy jihatdan juda barqaror metall bo‘lib, kislotalar va boshqa kimyoviy moddalarga chidamli. Bu xususiyati uni tibbiyot va texnologiyada ishlatishga imkon beradi.
▪️Tibbiyotda qo‘llanilishi: Oltin birikmalari tibbiy muolajalarda, masalan, onkologik kasalliklarni davolashda foydalaniladi. Oltin nanopartikalari yangi tibbiy texnologiyalarning rivojlanishida muhim rol o‘ynaydi.
▪️Kashfiyot va tarix: Oltin qadim zamonlardan beri insoniyatga ma'lum bo'lgan metall bo‘lib, qadimgi Misr va Gretsiyda muhim ahamiyatga ega bo‘lgan. U ko‘plab madaniyatlarda qudrat va boylikni anglatadi.""")

        elif belgi.lower() == "hg":
           print("""Simob (Hg)
▪️Simob (Hg) – davriy jadvalning 80-elementi bo‘lib, og‘ir metall va suyuq metall sifatida tanilgan. Simob o‘zining xususiyatlari va keng qo‘llanilishi bilan ajralib turadi.
▪️Nomi va kashfiyoti: Simob nomi lotincha "hydrargyrum" so‘zidan kelib chiqadi, bu "suvli kumush" degan ma'noni anglatadi. U qadim zamonlardan beri ma'lum bo'lgan metall hisoblanadi.
▪️Suyuq holati: Simob xona haroratida suyuq holatda bo‘lgan yagona metall hisoblanadi. Bu xususiyati uni tibbiyot va sanoatda keng qo‘llanilishiga imkon beradi.
▪️Tibbiyotda foydalanish: Simob ko‘pincha termometrlar va barometrlar ishlab chiqarishda ishlatiladi. Biroq, uning toksikligi sababli, hozirgi kunda tibbiyotda foydalanish kamaygan.
▪️Kimyoviy xususiyatlari: Simob oson ionlashadigan metall bo‘lib, turli kimyoviy reaktsiyalarda faol qatnashadi. U kislotalar va asoslar bilan birga reaktsiyaga kirishadi.
▪️Odam organizmidagi ta'siri: Simobning organizmga kirishi sog‘liq uchun xavfli bo‘lishi mumkin, chunki u nevrologik va boshqa jiddiy kasalliklarni keltirib chiqarishi mumkin. Shuning uchun uning iste'moli cheklangan.
▪️Tabiatda tarqalishi: Simob yerning qatlamlarida keng tarqalgan bo‘lib, asosan rudalardan olinadi. U oz miqdorda, lekin kuchli toksik bo‘lgan metall hisoblanadi.
""")

        elif belgi.lower() == "tl":
           print("""Talliy (Tl)
▪️Talliy (Tl) – davriy jadvalning 81-elementi bo‘lib, yumshoq, oltin rangga o‘xshash metall hisoblanadi. U kimyoviy xususiyatlari va sanoatdagi turli qo‘llanilishi bilan ajralib turadi.
▪️Nomi va kashfiyoti: Talliy nomi lotincha "tallium" so‘zidan olingan bo‘lib, bu "yashil novda" degan ma'noni anglatadi. U 1861-yilda ingliz olimi William Crookes tomonidan kashf etilgan. Talliy kashf qilinganidan keyin tez orada uning kimyoviy xususiyatlari va imkoniyatlari o‘rganila boshladi.
▪️Fizik xususiyatlari: Talliy — yumshoq, kumushrang metall bo‘lib, 303°C da eriydi. Uning erish nuqtasi past bo‘lgani uchun u oson qayta ishlanadi va shaklga keltiriladi. U bir oz odatdagi temperaturada solishtirishda yumshoq va bo‘shashgan bo‘ladi.
▪️Kimyoviy xususiyatlari: Talliy asosan ikki valentli (Tl⁺) va uch valentli (Tl³⁺) holatda mavjud bo‘lib, kislotalar va asoslar bilan oson reaksiyaga kirishadi. Talliy birikmalari juda toksik bo‘lishi mumkin va muhim kimyoviy materiallar sifatida ishlatiladi.
▪️Sanoatdagi qo‘llanilishi: Talliy yarimo‘tkazgichlar, batareyalar, ekranlar, kompyuter texnologiyalari, elektronda va maxsus issiqlik o‘tkazuvchi materiallarda ishlatiladi. Shuningdek, u optik asboblar va infraqizil sensorlar ishlab chiqarishda ham qo‘llaniladi.
▪️Tibbiyotdagi qo‘llanilishi: Talliyning ba'zi birikmalari tibbiyotda rentgen tomografiyasida ishlatiladi. Ammo uning toksikligi sababli uning tibbiyotda qo‘llanilishi cheklangan.
▪️Odam organizmidagi ta'siri: Talliy va uning birikmalari organizmga kirishi mumkin bo‘lsa, ular jiddiy toksik ta'sir ko‘rsatishi mumkin. U asab tizimiga, yurak va buyraklarga zarar yetkazishi mumkin. Talliy o'zining toksik xususiyatlari bilan maxsus xavf tug'diradi va juda ehtiyotkorlik bilan ishlatilishi lozim.
▪️Tabiatda tarqalishi: Talliy yer qobig‘ida kam miqdorda tarqalgan, asosan sulfid minerallari, masalan, krokoit (Tl2Cr2O7) orqali olinadi. U tabiatda va yer qatlamlarida kislorodli birikmalar sifatida mavjud.
▪️Ekologik xavf: Talliy va uning birikmalari atrof-muhitga zarar yetkazishi mumkin. Ayniqsa, sanoatda ishlatilganda va chiqindilar orqali tabiiy suv resurslariga kirishi ekologik muammolarni keltirib chiqaradi.
▪️Fizik-kimyoviy xususiyatlari: Talliyning ikki valentli shakli (Tl⁺) ko‘proq barqaror, ammo uch valentli shakli (Tl³⁺) kamroq barqaror va ko‘proq toksik hisoblanadi. U o‘ta elektr o‘tkazuvchan va ionlashuv energiyasi past metall hisoblanadi.
""")

        elif belgi.lower() == "pb":
           print("""Qo'rg'oshin (Pb)
▪️Qo'rg'oshin (Pb) – davriy jadvalning 82-elementi bo‘lib, og‘ir metall va toksik modda sifatida tanilgan. Qo'rg'oshin o‘zining kimyoviy xususiyatlari va sanoatda keng qo‘llanilishi bilan ajralib turadi.
▪️Nomi va kashfiyoti: Qo'rg'oshin nomi lotincha "plumbum" so‘zidan kelib chiqadi, bu "og‘ir" yoki "og‘ir metall" degan ma'noni anglatadi. Qo'rg'oshin qadim zamonlardan beri tanilgan va ko‘plab qadimiy tsivilizatsiyalarda ishlatilgan.
▪️Fizik xususiyatlari: Qo'rg'oshin – yumshoq, sirg‘aluvchi va bo‘shashgan metall bo‘lib, o‘zining yuqori zichligi va xususiy elastikligi bilan ajralib turadi. U oson qayriladi va kesiladi.
▪️Kimyoviy xususiyatlari: Qo'rg'oshin kimyoviy reaktsiyalarda o‘rtacha faollikka ega. U havo bilan ta'sirlanganda oksidlanib, qo'rg'oshin oksidi yoki qo'rg'oshin sulfidini hosil qiladi. Kislotalar bilan reaksiya berib, turli xil tuzlar hosil qiladi.
▪️Sanoatdagi qo‘llanilishi: Qo'rg'oshin asosan akkumulyatorlar (masalan, svinxov akkumulyatorlar), quyosh panellari, plastmassa va elektrotexnikada ishlatiladi. Uning qo‘llanilishi ilgari yanada kengroq bo‘lgan, ammo uning toksikligi sababli, ko‘plab sohalarda o‘rnini boshqa materiallar egallagan.
▪️Tibbiyotdagi qo‘llanilishi: Qo'rg'oshin kimyoviy moddalarini tibbiyotda ba'zi holatlarda ishlatish mumkin, lekin uning toksikligi tufayli undan foydalanish juda cheklangan. Qo'rg'oshin bilan zaharlanish og‘ir nevrologik va boshqa jiddiy kasalliklarga olib kelishi mumkin.
▪️Odam organizmidagi ta'siri: Qo'rg'oshin organizmga kirsa, u jigar, buyraklar va asab tizimiga zarar yetkazadi. Qo'rg'oshin toksik bo‘lganligi uchun, uning organizmga kirishini oldini olish zarur. Qo'rg'oshin bilan zaharlanishdan saqlanish uchun ko‘plab me'yorlar belgilangan.
▪️Tabiatda tarqalishi: Qo'rg'oshin yer qobig‘ida keng tarqalgan bo‘lib, asosan rudalardan olinadi. Qo'rg'oshin ruda shakllari, masalan, galenit va qorong‘i qo‘rg'oshin minerallari, juda ko‘p uchraydi.
▪️Ekologik xavf: Qo'rg'oshin atrof-muhitga zarar etkazishi mumkin. U yerda uzoq muddat davomida barqaror bo‘lib, o‘simliklar va hayvonlarga toksik ta'sir ko‘rsatishi mumkin. Shu sababli, qo'rg'oshin chiqindilari va ifloslanishiga qarshi kurashish zarur.
▪️Fizik-kimyoviy xususiyatlari: Qo'rg'oshin yuqori zichlikka ega va korroziyaga chidamli bo‘lib, ko‘plab sanoat jarayonlarida qo‘llaniladi. U o‘ta barqaror va qattiq metall bo‘lib, yuqori haroratlarda ishlov berishda yaxshi natijalar beradi.""")

        elif belgi.lower() == "bi":
           print("""Vismut (Bi)
▪️Vismut – juda kam uchraydigan og'ir metall bo‘lib, uning xususiyatlari juda o'ziga xosdir. Quyidagi faktlar Vismut haqida sizni qiziqtirishi mumkin:
▪️Tibbiyotda qo‘llaniladi: Vismut bir qator dori-darmonlarda, jumladan, oshqozon-ichak tizimi kasalliklarini davolashda ishlatiladi. Masalan, bizmut subtsalisilatidan oshqozon yarasi va gastritni davolashda foydalaniladi.
▪️Yengil va oson ishlov beriladigan: Vismut metallari juda og'ir bo'lmasa-da, juda mustahkam va asosan tish va maishiy texnikada ishlatiladi. Shuningdek, Vismutning past erish harorati uni oson eritish imkonini beradi.
▪️Ekologik toza: Vismut og'ir metallar orasida eng kam toksiklaridan biri hisoblanadi va u ekologik zarar etkazmaydi. Shuning uchun u atrof-muhitni ifloslantirmasdan ishlab chiqarish jarayonlarida qo‘llaniladi.
▪️Elektronika sanoatida: Vismutning xususiyatlari ularni elektron qurilmalarda, ayniqsa past voltajli batareyalar va termoelektrik generatorlarda ishlatishga imkon beradi.
▪️Spontan yo‘qolish: Vismut juda tez eriydi va issiqlikni yaxshi o'tkazadi, bu esa uning kimyoviy jarayonlarda ishlatilishini ta'minlaydi.
▪️Yuqori o‘tish temperaturasi: Vismut tarkibidagi birikmalar yuqori haroratlarda ham barqaror bo‘lib, yuqori texnologiyalarda ishlatiladi.
▪️Vismutli qotishmalar: Vismut o'zining qotishmalarida o'ziga xos xususiyatlarga ega, ular ko'pincha elektrokimyoviy qurilmalar, og‘ir yuk ko‘tarish sanoatida ishlatiladi.""")

        elif belgi.lower() == "po":
           print("""Poloniy (Po)
▪️Poloniy – radioaktiv element bo‘lib, u juda kuchli nurlanish chiqaradi. Quyidagi faktlar Poloniy haqida sizni qiziqtirishi mumkin:
▪️Tarixi: Poloniy 1898-yilda Mariya va Pyotr Kuri tomonidan kashf etilgan va uning nomi Polshaga hurmat sifatida berilgan.
▪️Radioaktiv xususiyatlar: Poloniy juda yuqori darajadagi alfa-nurlanishni chiqaradi, shuning uchun u xavfli va ehtiyotkorlik bilan ishlov berishni talab qiladi.
▪️Sanoatda foydalanish: Poloniy yadro sanoatida, asosan nurlanish manbai sifatida, va o'ziga xos termoyadroviy jarayonlarda ishlatiladi.
▪️Biologik ta'siri: Poloniyning kuchli radioaktivligi tufayli inson organizmiga juda zararli ta'sir ko‘rsatadi, shu sababli uni faqat maxsus laboratoriyalarda va xavfsiz sharoitda ishlatish mumkin.
▪️Kosmik tadqiqotlar: Poloniy kosmik apparatlarda ishlatiladi, chunki u uzoq muddat davomida barqaror energiya manbai sifatida xizmat qilishi mumkin.
▪️Yadro energetikasi: Poloniyning nuklidlari nurlanish manbai sifatida yadro batareyalarida va kosmik tadqiqotlarda foydalaniladi.
▪️Poloniy va xavfsizlik: Poloniy og‘ir yoki halokatli kasalliklarga olib kelishi mumkin bo‘lgani uchun, uning xavfsiz ishlatilishi qat'iy nazoratga olinadi.""")

        elif belgi.lower() == "at":
            print("""Astat (At)
▪️Astat – juda kam uchraydigan radioaktiv element bo‘lib, uning xususiyatlari hali ham to‘liq o‘rganilmagan. Quyidagi faktlar Astat haqida sizni qiziqtirishi mumkin:
▪️Radioaktivlik: Astat juda yuqori darajadagi alfa-nurlanishni chiqaradi va bu uni juda xavfli elementga aylantiradi.
▪️Tarkibi va mavjudligi: Astat Yer po‘stida juda kam miqdorda mavjud bo‘lib, uning asosan yadro reaksiya jarayonlarida hosil bo‘ladi.
▪️Tibbiiyotda qo‘llanilishi: Astat, ayniqsa, saratonni davolashda ishlatiladi. Uni saraton hujayralariga nurlanish yuborib, ularning o‘sishini to‘xtatish maqsadida qo‘llash mumkin.
▪️Kimyoviy xususiyatlar: Astat – halqa va guruh bo‘yicha galogenlar oilasiga kiradi, lekin u o‘zining kimyoviy xususiyatlari bilan boshqa galogenlardan farq qiladi.
▪️Sanoat va texnologiyada qo‘llanilishi: Astatinning radioaktivligi va nurlanish chiqarish qobiliyati uni maxsus sanoat ilovalari, masalan, nurlanish manbalari va detectorlar uchun foydali qiladi.
▪️Juda kam uchraydi: Astat Yer po‘stida tabiiy ravishda juda kam miqdorda mavjud bo‘lib, uning kashf etilishi juda qiyin.
▪️Biologik ta'siri: Astatinning kuchli radioaktivligi uni organizm uchun xavfli qiladi va odamlar bilan aloqa qilishdan oldin ehtiyotkorlik bilan ishlov berilishi kerak.""")

        elif belgi.lower() == "rn":
           print("""Radon (Rn)
▪️Radon – tabiiy radioaktiv gaz bo‘lib, uning mavjudligi va xavfi ko‘plab tadqiqotlarga sabab bo‘lgan. Quyidagi faktlar Radon haqida sizni qiziqtirishi mumkin:
▪️Tabiiy mavjudlik: Radon tabiiy ravishda yer osti qazilmalari, xususan, toriy va uran izotoplarining parchalanish jarayonida hosil bo‘ladi.
▪️Sog‘liq uchun xavf: Radon gazining yuqori konsentratsiyasi xonadonda va yopiq joylarda havoga mikroskopik zararli zarrachalar yuborib, uzoq muddatda saraton kasalligiga olib kelishi mumkin.
▪️Tibbiyotda foydalanish: Radonning nurlanishi ba'zi onkologik kasalliklarni davolashda ishlatiladi, ammo uning xavfini kamaytirish uchun maxsus texnikalar talab qilinadi.
▪️Yopiq muhitdagi xavf: Radon gazining yuqori darajada to‘planishi uylar va boshqa yopiq joylarda odamlar uchun xavfli bo‘lishi mumkin. Shu sababli, radon darajasi doimiy nazorat ostida bo‘lishi kerak.
▪️Kimyoviy xususiyatlar: Radon – nobir element bo‘lib, o‘zining kimyoviy xususiyatlari bo‘yicha inert gazlarga o‘xshashdir.
▪️Xavfli nurlanish: Radon kuchli alfa-nurlanish chiqaradi, bu esa uni yuqori xavfli radioaktiv gazga aylantiradi.
▪️Boshqa elementlar bilan reaksiyalar: Radon boshqa kimyoviy elementlar bilan oson reaksiyaga kirishmaydi, ammo u alfa-nurlanish chiqarishi tufayli biologik tizimlarga zarar yetkazishi mumkin.
""")

        elif belgi.lower() == "fr":
           print("""Fransiyum (Fr)
▪️Fransiyum – eng kam uchraydigan va eng radioaktiv elementlardan biri bo‘lib, u juda qisqa muddatli yashash davriga ega. Quyidagi faktlar Fransiyum haqida sizni qiziqtirishi mumkin:
▪️Tarixi: Fransiyum 1939-yilda Irène Joliot-Curie va Frédéric Joliot-Curie tomonidan kashf etilgan. Uning nomi Frantsiyaga hurmat sifatida berilgan.
▪️Radioaktivlik: Fransiyum juda kuchli radioaktiv xususiyatlarga ega bo‘lib, uning barcha izotoplari juda qisqa umr ko‘radi.
▪️Sanoatda qo‘llanilmaydi: Fransiyumning radioaktivligi va qisqa umri sababli u sanoatda yoki tibbiyotda keng qo‘llanilmaydi.
▪️Kimyoviy xususiyatlar: Fransiyum kimyoviy xususiyatlari bo‘yicha rubidiy va seziy elementlariga o‘xshash bo‘lib, u yengil metallar guruhiga kiradi.
▪️Tabiiy mavjudlik: Fransiyum Yer po‘stida juda kam miqdorda uchraydi va asosan yadro reaktsiyalari yoki boshqa radioaktiv jarayonlarda hosil bo‘ladi.
▪️Xavfli ta'sirlar: Fransiyumning kuchli nurlanishi odam organizmi uchun juda xavfli bo‘lishi mumkin, shuning uchun u bilan ishlashda katta ehtiyotkorlik talab qilinadi.
▪️Ilmiy tadqiqotlar: Fransiyum ilmiy tadqiqotlarda va yadro fizikasi sohasida cheklangan miqdorda qo‘llaniladi.""")

        elif belgi.lower() == "ra":
           print("""Radiy (Ra)
▪️Radiy – kuchli radioaktiv element bo‘lib, uning nurlanishi turli sohalarda ishlatiladi. Quyidagi faktlar Radiy haqida sizni qiziqtirishi mumkin:
▪️Tarixi: Radiy 1898-yilda Mariya va Pyotr Kuri tomonidan kashf etilgan. Uning nomi "radius" so‘zidan kelib chiqqan bo‘lib, "nurlanish" ma'nosini anglatadi.
▪️Radioaktivlik: Radiy kuchli alfa-nurlanish chiqaradi va u uzoq muddat davomida nurlanish manbai sifatida ishlatilgan.
▪️Tibbiyotda foydalanish: Radiy uzoq vaqt davomida onkologik kasalliklarni davolashda ishlatilgan, ayniqsa, saratonni davolashda radioterapiya usullarida.
▪️Sanoatda qo‘llanilishi: Radiyning nurlanish xususiyatlari radon gazining ishlab chiqarilishida va nurlanishni o‘lchash vositalarida foydalanilgan.
▪️Biologik ta'siri: Radiyning kuchli radioaktivligi organizmga zarar yetkazishi mumkin, shuning uchun u bilan ishlashda ehtiyotkorlik zarur.
▪️Xavfli nurlanish: Radiyning nurlanishi uzoq muddatda odamlar uchun xavfli bo‘lishi mumkin, bu esa uni foydalanishda nazoratni talab qiladi.
▪️Yadro fizikasi: Radiy yadro fizikasi tadqiqotlarida qo‘llaniladi, chunki uning nurlanishi yadro jarayonlarini o‘rganishda foydalidir.
""")

        elif belgi.lower() == "ac":
           print("""Aktiniy (Ac)
▪️Aktiniy – kuchli radioaktiv element bo‘lib, uning kimyoviy va fizikal xususiyatlari ham juda o‘ziga xosdir. Quyidagi faktlar Aktiniy haqida sizni qiziqtirishi mumkin:
▪️Tarixi: Aktiniy 1899-yilda Friedrich Oskar Giesel tomonidan kashf etilgan va nomi "Aktin" so‘zidan olingan, bu so‘z "nurlanish" ma'nosini anglatadi.
▪️Radioaktivlik: Aktiniy kuchli alfa-nurlanish chiqaradi, shu sababli u xavfli radioaktiv elementlardan biridir.
▪️Sanoatda qo‘llanilishi: Aktiniy o‘zining nurlanishi tufayli yadro texnologiyalarida, xususan, yadro reaktorlarida ishlatiladi.
▪️Tibbiyotda foydalanish: Aktiniyning nurlanish xususiyatlari onkologik kasalliklarni davolashda qo‘llaniladi, ammo u juda kam uchraydi.
▪️Tabiiy mavjudlik: Aktiniy tabiiy ravishda Yer po‘stida juda kam miqdorda uchraydi va asosan uran va toriy izotoplarining parchalanishi jarayonida hosil bo‘ladi.
▪️Biologik ta'siri: Aktiniy kuchli radioaktiv bo‘lgani uchun, u organizmga zarar yetkazishi mumkin, shu sababli u bilan ishlashda ehtiyotkorlik zarur.
▪️Kimyoviy xususiyatlar: Aktiniy kimyoviy xususiyatlari bo‘yicha alkali yer metallari bilan o‘xshash bo‘lib, o‘zining nurlanishi bilan ajralib turadi.""")

        elif belgi.lower() == "th":
           print("""Toriy (Th)
▪️Toriy – radioaktiv metall bo‘lib, yadro energetikasi va ilmiy tadqiqotlarda muhim o‘rin egallaydi. Quyidagi faktlar Toriy haqida sizni qiziqtirishi mumkin:
▪️Kashfiyot: Toriy 1828-yilda Jöns Jakob Berzelius tomonidan kashf etilgan va u Norvegiya xudosi Tor nomi bilan atalgan.
▪️Yadro energetikasi: Toriy, urandan farqli o‘laroq, xavfsiz va uzoq muddat davomida ishlatilishi mumkin bo‘lgan yadro yoqilg‘isi sifatida ko‘riladi. Uning yadro reaktsiyalaridagi roli reaktorlarda energiya ishlab chiqarish uchun juda muhimdir.
▪️Radioaktivlik: Toriy tabiiy ravishda radioaktiv bo‘lib, alfa nurlanishi chiqaradi. U juda uzoq vaqt davomida nurlanish manbai sifatida mavjud bo‘lishi mumkin.
▪️Tabiiy mavjudlik: Toriy Yer po‘stida nisbatan ko‘p miqdorda mavjud bo‘lib, u asosan uran va boshqa radioaktiv izotoplar bilan birga uchraydi.
▪️Sanoatda foydalanish: Toriy yadro energetikasidan tashqari, ba'zi yuqori haroratli sanoat jarayonlarida ham qo‘llaniladi.
▪️Biologik ta'siri: Toriy kuchli radioaktiv element bo‘lgani uchun, uning yuqori konsentratsiyasi organizmga zarar yetkazishi mumkin.
▪️Kimyoviy xususiyatlar: Toriy kimyoviy jihatdan boshqa alkali yer metallari bilan o‘xshashdir, lekin uning radioaktivligi uni ajratib turadi.""")

        elif belgi.lower() == "pa":
           print("""Protaktiniy (Pa)
▪️Protaktiniy – davriy jadvalning 91-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar protaktiniy haqida sizni qiziqtirishi mumkin:
▪️Noyob va radioaktiv: Protaktiniy juda kam uchraydigan elementlardan biri bo‘lib, tabiatda juda kam miqdorda uchraydi. Bu elementning ko‘pchilik izotoplari radioaktivdir, shu sababli u bilan ishlash maxsus xavfsizlik choralarini talab qiladi.
▪️Oliy kimyoviy faollik: Protaktiniy kimyoviy jihatdan juda faol bo‘lib, suv bilan oson reaksiyaga kirishadi va bu jarayonda og‘ir metallar bilan birikmalar hosil qiladi.
▪️Yadro texnologiyalarida qo‘llanilishi: Protaktiniy izotoplari yadro texnologiyalarida muhim o‘rin tutadi. Ayniqsa, 233Pa izotopi uranni 233U izotopiga aylantirish jarayonida vositachi sifatida ishlatiladi, bu esa yadro energiyasini ishlab chiqarishda katta ahamiyatga ega.
▪️Zaharliligi va xavfi: Protaktiniy odam organizmi uchun juda zaharli hisoblanadi. U bilan ishlashda maxsus himoya kiyimlari va uskunalari talab qilinadi, chunki bu elementning radioaktiv nurlari hujayralarga zarar yetkazishi mumkin.
▪️Sanoatda cheklangan qo‘llanilishi: Protaktiniy juda kam qo‘llaniladi, asosan ilmiy tadqiqotlarda va yadro energetikasida foydalaniladi. Uning yuqori radioaktivligi va kam miqdorda uchrashi sanoatdagi qo‘llanishini cheklaydi.
▪️Tabiatdagi tarqalishi: Protaktiniy odatda uran va toriy rudalarida juda kichik miqdorda uchraydi. U rudalarni qayta ishlash jarayonida ajratib olinadi, ammo bu jarayon juda qiyin va murakkabdir.
▪️Izlanishlarda ahamiyati: Protaktiniy kimyo va fizika sohasida muhim tadqiqot obyekti bo‘lib, uning xossalari ilmiy jamoatchilik tomonidan chuqur o‘rganilmoqda.
""")

        elif belgi.lower() == "u":
           print("""Uran (U)
▪️Uran – davriy jadvalning 92-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar uran haqida sizni qiziqtirishi mumkin:
▪️Yadro yoqilg‘isi: Uran yadro energetikasida eng ko‘p qo‘llaniladigan yoqilg‘i hisoblanadi. 235U izotopi atom elektr stansiyalarida yadro zanjir reaksiyalarini qo‘zg‘atish uchun ishlatiladi, bu esa katta miqdorda energiya ishlab chiqarishga imkon beradi.
▪️Radioaktivlik: Uran radioaktiv element bo‘lib, uning izotoplari asta-sekin parchalanadi va bu jarayonda radioaktiv nurlar chiqaradi. Bu xususiyat uranni yadro qurollari va yadro energetikasida foydalanishga imkon beradi.
▪️Tabiatdagi keng tarqalishi: Uran Yerning qobig‘ida keng tarqalgan bo‘lib, asosan uran rudalarida topiladi. Uning zaxiralari bir qancha mamlakatlarda, xususan, Kanada, Avstraliya va Qozog‘istonda katta miqdorda mavjud.
▪️Zaharli va xavfli: Uran radioaktivligi tufayli odamlar uchun juda xavfli bo‘lib, u bilan ishlashda maxsus ehtiyot choralariga rioya qilinishi kerak. Ayniqsa, uning changi nafas yo‘llariga tushganda salomatlikka jiddiy zarar yetkazishi mumkin.
▪️Yadro qurollari yaratishda qo‘llanilishi: Uranning ayrim izotoplari yadro qurollarini ishlab chiqarishda foydalaniladi. Xususan, 235U izotopi atom bombalari uchun asosiy material hisoblanadi.
▪️Og‘ir element: Uran eng og‘ir tabiiy elementlardan biri hisoblanadi. Uning zichligi oltinning zichligidan taxminan 1,6 baravar yuqori bo‘lib, og‘irligi jihatidan qattiq metallar orasida eng yuqorilardan biridir.
▪️Tibbiyotda qo‘llanilishi: Uran izotoplari tibbiyotda ham foydalaniladi. Ba’zi radioaktiv izotoplar onkologiya sohasida saraton kasalliklarini davolashda yordam beradi.""")

        elif belgi.lower() == "np":
           print("""Neptuniy (Np)
▪️Neptuniy – davriy jadvalning 93-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar neptuniy haqida sizni qiziqtirishi mumkin:
▪️Sun’iy element: Neptuniy 1930-yillarda laboratoriya sharoitida birinchi marta sintez qilingan elementlardan biridir. Bu element tabiiy ravishda Yerda juda kam miqdorda uchraydi va asosan yadro reaktorlarida ishlab chiqariladi.
▪️Yadro chiqindilari: Neptuniy asosan yadro yoqilg‘isi chiqindilarida hosil bo‘ladi. Yadro reaktorlarida uran va plutoniy parchalanganda neptuniy izotoplari paydo bo‘ladi, bu esa uni yadro energetikasidagi muhim elementga aylantiradi.
▪️Radioaktivlik: Neptuniy juda kuchli radioaktiv elementdir. Uning izotoplari uzoq yarim yemirilish davriga ega bo‘lib, bu nurlarni chiqarish jarayonida ko‘p yillar davomida radiatsiya tarqatadi.
▪️Yadro qurollari uchun potentsial: Neptuniyning ayrim izotoplari, masalan, 237Np, yadro qurollari uchun potentsial material hisoblanadi. Uning yadro zanjir reaksiyalarini qo‘zg‘atish qobiliyati uni strategik ahamiyatga ega elementga aylantiradi.
▪️Zaharliligi va xavfi: Neptuniy odamlar va atrof-muhit uchun katta xavf tug‘dirishi mumkin. U bilan ishlashda maxsus himoya choralariga rioya qilinishi kerak, chunki uning radioaktiv nurlari sog‘liq uchun jiddiy xavf soladi.
▪️Izlanishlarda ahamiyati: Neptuniy ilmiy tadqiqotlar uchun qiziqarli element hisoblanadi. Uning fizik-kimyoviy xossalari hali to‘liq o‘rganilmagan va bu sohada ko‘plab izlanishlar olib borilmoqda.
▪️Sanoatda cheklangan qo‘llanilishi: Neptuniyning keng sanoat miqyosida qo‘llanilishi mavjud emas, asosan ilmiy tadqiqotlar va yadro texnologiyalarida foydalaniladi. Uning radioaktivligi va kam miqdorda sintez qilinishi sanoatda keng qo‘llanilishiga to‘sqinlik qiladi.""")

        elif belgi.lower() == "pu":
            print("""Plutoniy (Pu)
▪️Plutoniy – davriy jadvalning 94-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar plutoniy haqida sizni qiziqtirishi mumkin:
▪️Yadro qurollarida qo‘llanilishi: Plutoniy 239 izotopi yadro qurollarining asosiy materiallaridan biridir. 1945-yilda AQSh tomonidan tashlangan ikkinchi atom bombasi aynan plutoniy asosida ishlab chiqilgan.
▪️Yadro energiyasida muhim rol o‘ynaydi: Plutoniy reaktorlar uchun yadro yoqilg‘isi sifatida ham ishlatiladi. U uran izotoplari bilan birgalikda ishlatilgan yoqilg‘ini qayta ishlash jarayonida hosil bo‘ladi va energiya ishlab chiqarishda muhim ahamiyatga ega.
▪️Radioaktivlik va xavf: Plutoniy juda kuchli radioaktiv element bo‘lib, inson salomatligiga jiddiy xavf tug‘diradi. Uning changi yoki kichik zarrachalari nafas yo‘llari orqali organizmga tushganda rak kabi kasalliklarni keltirib chiqarishi mumkin.
▪️Kosmik izlanishlarda qo‘llanilishi: Plutoniy 238 izotopi kosmik apparatlarda energiya manbai sifatida qo‘llaniladi. U uzoq muddatli kosmik missiyalarda radioizotopli termoelektrik generatorlarda foydalaniladi, bu esa kosmik zondlarga uzoq yillar davomida energiya yetkazib turadi.
▪️Sun’iy ravishda sintez qilingan element: Plutoniy tabiatda juda kam uchraydi va asosan sun’iy ravishda ishlab chiqariladi. Bu element 1940-yilda birinchi marta Kaliforniya universiteti olimlari tomonidan sintez qilingan.
▪️Zichligi yuqori metall: Plutoniy zichligi juda yuqori bo‘lgan metallar qatoriga kiradi. U yer ostida joylashgan uran rudalarida topilishi mumkin, ammo uning sanoat miqyosida olinishi asosan yadro reaktorlari orqali amalga oshiriladi.
▪️Sanoatda cheklangan qo‘llanilishi: Plutoniyning radioaktivligi tufayli uning qo‘llanilishi cheklangan. Asosan yadro energetikasida va ilmiy izlanishlarda foydalaniladi.
""")

        elif belgi.lower() == "am":
           print("""Ameritsiy (Am)
▪️Ameritsiy – davriy jadvalning 95-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar ameritsiy haqida sizni qiziqtirishi mumkin:
▪️Sun’iy ravishda sintez qilingan element: Ameritsiy 1944-yilda Qo‘shma Shtatlar olimlari tomonidan birinchi marta sintez qilingan. U plutoniyni neytronlar bilan bombardimon qilish natijasida hosil bo‘ladi va tabiatda tabiiy ravishda uchramaydi.
▪️Tutun detektorlarida qo‘llanilishi: Ameritsiy 241 izotopi eng keng tarqalgan qo‘llanilishlaridan biri – tutun detektorlarida foydalaniladi. U alfa zarrachalarini chiqaradi, bu esa havodagi tutun zarrachalarini aniqlashda yordam beradi va shu tariqa xavfsizlikni ta’minlaydi.
▪️Radioaktivlik: Ameritsiy kuchli radioaktiv element bo‘lib, uzoq yarim yemirilish davriga ega. Uning radiatsiyasi inson organizmi uchun xavf tug‘diradi, shu sababli u bilan ishlashda ehtiyotkorlik talab qilinadi.
▪️Yadro izlanishlarida qo‘llanilishi: Ameritsiy yadro izlanishlari va yadro texnologiyalari sohasida muhim o‘rin tutadi. Uning izotoplari neytronlar manbai sifatida qo‘llanilib, ilmiy tadqiqotlar va yadro energetikasida foydalaniladi.
▪️Og‘ir metall: Ameritsiy zichligi juda yuqori bo‘lgan metallar qatoriga kiradi. U boshqa og‘ir elementlar singari radioaktiv bo‘lib, metall shaklda olinishidan avval bir nechta murakkab texnologik jarayonlardan o‘tadi.
▪️Radiografiyada foydalanish: Ameritsiy radiografiya sohasida ham qo‘llaniladi. Uning izotoplari x-ray nurlanishining o‘rnini bosuvchi neytron manbai bo‘lib xizmat qiladi va shu tariqa metallarning ichki tarkibini tekshirishda yordam beradi.
▪️Sanoatda cheklangan qo‘llanilishi: Ameritsiyning yuqori radioaktivligi uning sanoatda keng ko‘lamda qo‘llanilishini cheklaydi. Asosan ilmiy izlanishlar va texnik qurilmalarda foydalaniladi.""")

        elif belgi.lower() == "cm":
           print("""Kyuriy (Cm)
▪️Kyuriy – davriy jadvalning 96-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar kyuriy haqida sizni qiziqtirishi mumkin:
▪️Marie va Pierre Curie sharafiga nomlangan: Kyuriy elementi mashhur olimlar Marie va Pierre Curie sharafiga nomlangan. U 1944-yilda amerikalik olimlar Glenn Seaborg va Albert Ghiorso tomonidan sintez qilingan.
▪️Sun’iy element: Kyuriy tabiatda tabiiy ravishda uchramaydi va faqat yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U plutoniy yoki ameritsiy izotoplarini neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Yuqori radioaktivlik: Kyuriy kuchli radioaktiv element bo‘lib, uning izotoplari katta miqdorda alfa nurlanishini chiqaradi. U bilan ishlashda maxsus himoya choralariga rioya qilish zarur.
▪️Kosmik izlanishlarda qo‘llanilishi: Kyuriy izotoplari uzoq muddatli energiya manbai sifatida radioizotopli termoelektrik generatorlarda qo‘llaniladi. Bu izotoplar kosmik zondlarga uzoq masofalarda energiya yetkazib turadi.
▪️Issiqlik manbai: Kyuriy izotoplari o‘zlarining radioaktiv parchalanish jarayonida katta miqdorda issiqlik ajratib chiqaradi. Bu xususiyat uni kosmik missiyalar va ilmiy qurilmalarda energiya manbai sifatida ishlatishga imkon beradi.
▪️Yadro tadqiqotlarida ahamiyati: Kyuriy izotoplari yadro sohasidagi tadqiqotlarda foydalaniladi. U neytronlar manbai sifatida ilmiy tajribalarda qo‘llaniladi va yangi elementlar va birikmalar sintez qilishda muhim ahamiyatga ega.
▪️Tibbiyotda cheklangan qo‘llanilishi: Kyuriy izotoplarining radioaktivligi tufayli u ba’zi tibbiy ilovalarda, xususan, radioterapiyada foydalaniladi. Shu bilan birga, uning yuqori radioaktivligi qo‘llanishini cheklaydi.""")

        elif belgi.lower() == "bk":
           print("""Berkliy (Bk)
▪️Berkliy – davriy jadvalning 97-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar berkliy haqida sizni qiziqtirishi mumkin:
▪️Kaliforniya universiteti sharafiga nomlangan: Berkliy elementi 1949-yilda Kaliforniya universiteti (Berkli) olimlari tomonidan sintez qilingan va ushbu universitet nomi bilan atalgan.
▪️Sun’iy element: Berkliy tabiiy ravishda uchramaydigan sun’iy element bo‘lib, plutoniy yoki ameritsiy izotoplarini tezlatgichlarda yoki yadro reaktorlari yordamida neytronlar bilan bombardimon qilish orqali olinadi.
▪️Radioaktivlik: Berkliy kuchli radioaktiv element hisoblanadi. U alfa va beta nurlanishini chiqaradi, bu esa uni tibbiyot va sanoatda foydalanishni cheklaydi.
▪️Yadro izlanishlarida foydalanish: Berkliy yadro texnologiyalari va izlanishlarida muhim ahamiyatga ega. Uning izotoplari boshqa transuran elementlarni, masalan, kaliforniy yoki einshteyniy elementlarini sintez qilishda qo‘llaniladi.
▪️Metall shaklda olinishi: Berkliyni sof metall shaklida olish qiyin va murakkab jarayonlarni talab qiladi. U odatda birikmalar holida uchraydi va faqat maxsus laboratoriyalarda metall shaklga keltiriladi.
▪️Ilmiy izlanishlarda ahamiyati: Berkliyning izlanishlar uchun qo‘llanilishi transuran elementlar va yadro kimyosi sohasida katta ahamiyatga ega. Uning yangi birikmalarini sintez qilish va ularning xossalarini o‘rganish ilm-fan uchun qimmatli ma’lumotlar beradi.
▪️Sanoatda kam qo‘llanilishi: Berkliyning yuqori radioaktivligi uni sanoatda keng qo‘llanilishiga to‘sqinlik qiladi, biroq uning izotoplari ilmiy tadqiqotlar va yadro reaktorlarida foydalaniladi.
""")

        elif belgi.lower() == "cf":
           print("""Kaliforniy (Cf)
▪️Kaliforniy – davriy jadvalning 98-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar kaliforniy haqida sizni qiziqtirishi mumkin:
▪️Kaliforniya shtati nomidan: Kaliforniy elementi 1950-yilda Kaliforniya universiteti olimlari tomonidan birinchi marta sintez qilingan va Kaliforniya shtati nomi bilan atalgan.
▪️Sun’iy element: Kaliforniy tabiatda tabiiy ravishda uchramaydigan element bo‘lib, plutoniy yoki kuriy izotoplarini neytronlar bilan bombardimon qilish orqali yadro reaktorlari yoki zarralar tezlatgichlarida sintez qilinadi.
▪️Yadro reaktorlarida qo‘llanilishi: Kaliforniyning izotoplari, ayniqsa, Cf-252, neytron manbai sifatida yadro reaktorlarida va yadro izlanishlarida keng qo‘llaniladi. U yadro reaktorlarini ishga tushirishda va reaktorlarning ishlashini boshqarishda muhim rol o‘ynaydi.
▪️Radiatsion terapiyada foydalanish: Kaliforniyning Cf-252 izotopi tibbiyotda, xususan, saraton kasalligini davolashda qo‘llaniladi. U yadro terapiyasi orqali o‘simtalarni nurlantirishda ishlatiladi va saraton hujayralarini yo‘q qilishga yordam beradi.
▪️Portlash xavfi: Kaliforniy yuqori radioaktiv element bo‘lib, uning izotoplari katta miqdorda energiya chiqaradi. U bilan ishlash maxsus ehtiyotkorlik va himoya choralarini talab qiladi.
▪️Zich metall: Kaliforniy yuqori zichlikka ega metall bo‘lib, og‘irligi bo‘yicha og‘ir elementlar qatoriga kiradi. Shu bilan birga, uning yuqori radioaktivligi uni faqat maxsus ilmiy maqsadlar uchun qo‘llashni taqozo etadi.
▪️Sanoat qo‘llanilishi: Kaliforniy Cf-252 izotopi ba’zi sanoat tarmoqlarida, masalan, burg‘ulash jarayonlarida va materiallarni tekshirishda neytron nurlanishidan foydalaniladi. Ushbu nurlanish materiallarning ichki tarkibini aniqlashda yordam beradi.""")

        elif belgi.lower() == "es":
           print("""Einshteyniy (Es)
▪️Einshteyniy – davriy jadvalning 99-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar einshteyniy haqida sizni qiziqtirishi mumkin:
▪️Albert Einshtein sharafiga nomlangan: Einshteyniy elementi mashhur fizik Albert Einstein sharafiga nomlangan. U 1952-yilda AQSh olimlari tomonidan sintez qilingan va birinchi marta vodorod bombasini sinovdan o‘tkazish jarayonida kashf etilgan.
▪️Sun’iy element: Einshteyniy tabiatda uchramaydi va faqat yadro reaktorlari yoki zarralar tezlatgichlari yordamida sun’iy yo‘l bilan sintez qilinadi. U plutoniy yoki kuriy izotoplarini neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Cheklangan miqdorda ishlab chiqariladi: Einshteyniy nihoyatda kam uchraydigan element bo‘lib, uni ishlab chiqarish jarayoni juda murakkab va qimmatga tushadi. Bu elementning faqat bir necha milligrammi sintez qilingan.
▪️Radioaktivlik: Einshteyniy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. U bilan ishlash maxsus ehtiyot choralarini talab qiladi, chunki nurlanish salomatlikka zarar yetkazishi mumkin.
▪️Yadro tadqiqotlarida ahamiyati: Einshteyniy asosan ilmiy tadqiqotlarda qo‘llaniladi. Uning izotoplari boshqa transuran elementlarni, jumladan, mendeleviy elementini sintez qilishda foydalaniladi.
▪️Amaliy qo‘llanilish yo‘q: Einshteyniy yuqori radioaktivligi va cheklangan miqdori tufayli keng sanoat yoki tijorat ilovalarga ega emas. U faqat yadro sohasidagi ilmiy tadqiqotlar uchun muhimdir.
▪️Yadro energiyasi va ilm-fan uchun qimmatli: Einshteyniyning sintez qilinishi va o‘rganilishi yangi elementlar va birikmalarni tushunishda muhim ilmiy yutuqlarni ta’minlaydi.
""")

        elif belgi.lower() == "fm":
           print("""Fermiy (Fm)
▪️Fermiy – davriy jadvalning 100-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar fermiy haqida sizni qiziqtirishi mumkin:
▪️Enrico Fermi sharafiga nomlangan: Fermiy elementi mashhur italiyalik fizik Enrico Fermi sharafiga nomlangan. U 1952-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Fermiy tabiatda tabiiy ravishda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U plutoniy yoki kuriy izotoplarini neytronlar bilan bombardimon qilish orqali olinadi.
▪️Yadro izlanishlarida qo‘llanilishi: Fermiy izotoplari asosan yadro tadqiqotlarida qo‘llaniladi. Ular transuran elementlarini sintez qilish va yadro reaksiyalarini o‘rganishda muhim rol o‘ynaydi.
▪️Radioaktivlik: Fermiy kuchli radioaktiv element hisoblanadi. Uning izotoplari alfa nurlanishini chiqaradi va yuqori darajadagi radioaktivlik tufayli uni ko‘plab amaliy sohalarda qo‘llashni cheklaydi.
▪️Ilmiy tadqiqotlarda cheklangan qo‘llanilishi: Fermiy izotoplarining yuqori radioaktivligi va cheklangan miqdori uni sanoat ilovalarida keng qo‘llanilishiga to‘sqinlik qiladi. Uning asosan ilmiy izlanishlar va eksperimentlar uchun ishlatilishi mumkin.
▪️Elementlarni sintez qilishda yordam: Fermiy va uning izotoplari boshqa og‘ir elementlarni sintez qilishda ishlatiladi. Ularning xossalari va o‘zaro reaksiyalari yadro kimyosi va fizikasida muhim o‘ringa ega.
▪️Cheklangan ishlab chiqarish: Fermiy nihoyatda kam ishlab chiqariladi, faqat maxsus ilmiy laboratoriyalarda sintez qilinadi. Uning ishlab chiqarilishi juda murakkab va juda qimmatga tushadi.
""")

        elif belgi.lower() == "md":
           print("""Mendeleyviy (Md)
▪️Mendeleyviy – davriy jadvalning 101-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar mendeleviy haqida sizni qiziqtirishi mumkin:
▪️Dmitri Mendeleyev sharafiga nomlangan: Mendeleyviy elementi rus olimi Dmitri Mendeleyev sharafiga nomlangan. U 1955-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Mendeleyviy tabiatda uchramaydi va faqat sun’iy yo‘l bilan yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U plutoniy yoki kuriy izotoplarini neytronlar bilan bombardimon qilish orqali olinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Mendeleyviy asosan yadro izlanishlarida qo‘llaniladi. U transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim rol o‘ynaydi.
▪️Radioaktivlik: Mendeleyviy kuchli radioaktiv element bo‘lib, uning izotoplari alfa nurlanishini chiqaradi. U bilan ishlash maxsus ehtiyotkorlik va himoya choralarini talab qiladi.
▪️Ilmiy tadqiqotlarda cheklangan qo‘llanilishi: Mendeleyviyning izotoplari sanoat yoki tibbiyotda keng qo‘llanilmaydi. Uning asosan ilmiy tadqiqotlar va yangi transuran elementlarni sintez qilish uchun ishlatilishi mumkin.
▪️Elementlarni sintez qilishda yordam: Mendeleyviy va uning izotoplari yadro fizikasidagi yangi tadqiqotlar uchun muhim material hisoblanadi. U transuran elementlarini o‘rganish va yangi elementlarni sintez qilishda qo‘llaniladi.
▪️Cheklangan ishlab chiqarish: Mendeleyviy nihoyatda kam miqdorda ishlab chiqariladi va faqat maxsus ilmiy laboratoriyalarda sintez qilinadi.""")

        elif belgi.lower() == "no":
           print("""Nobeliy (No)
▪️Nobeliy – davriy jadvalning 102-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar nobeliy haqida sizni qiziqtirishi mumkin:
▪️Alfred Nobel sharafiga nomlangan: Nobeliy elementi shvetsiyalik kimyogar va ixtirochi Alfred Nobel sharafiga nomlangan. U 1958-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Nobeliy tabiatda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U plutoniy yoki kuriy izotoplarini neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Nobeliy asosan yadro tadqiqotlarida qo‘llaniladi. Uning izotoplari boshqa transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim rol o‘ynaydi.
▪️Radioaktivlik: Nobeliy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari uzoq vaqt davomida yuqori darajada radioaktiv bo‘lib qoladi, shuning uchun uning bilan ishlashda ehtiyotkorlik zarur.
▪️Ilmiy tadqiqotlar uchun qo‘llanilish: Nobeliy asosan ilmiy izlanishlar va yangi elementlarni sintez qilishda ishlatiladi. U yadro fizikasi va kimyosida yangi tadqiqotlar uchun muhim ahamiyatga ega.
▪️Sanoatda cheklangan qo‘llanilish: Nobeliy yuqori radioaktivligi va cheklangan ishlab chiqarish miqdori tufayli sanoat yoki tibbiyotda keng qo‘llanilmaydi. Uning asosiy qo‘llanilishi ilmiy laboratoriyalarda yangi elementlarni yaratishda foydalaniladi.""")

        elif belgi.lower() == "lr":
            print("""Laurensiy (Lr)
▪️Laurensiy – davriy jadvalning 103-elementi bo‘lib, aktinoidlar guruhiga kiradi. Quyidagi qiziqarli faktlar laurensiy haqida sizni qiziqtirishi mumkin:
▪️Ernest O. Lawrence sharafiga nomlangan: Laurensiy elementi amerikalik fiziker Ernest O. Lawrence sharafiga nomlangan. U 1958-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Laurensiy tabiatda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U berkeliy va kaliforniy izotoplarini neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Laurensiy asosan yadro tadqiqotlarida qo‘llaniladi. Uning izotoplari transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim ahamiyatga ega.
▪️Radioaktivlik: Laurensiy kuchli radioaktiv element hisoblanadi. Uning izotoplari alfa nurlanishini chiqaradi va ular uzoq vaqt davomida yuqori darajadagi radioaktiv bo‘lib qoladi, shu sababli u bilan ishlash maxsus ehtiyotkorlikni talab qiladi.
▪️Ilmiy tadqiqotlar uchun qo‘llanilishi: Laurensiy elementlari asosan ilmiy izlanishlar va yangi elementlarni sintez qilishda qo‘llaniladi. Yadro fizikasida muhim tajribalar o'tkazish uchun ishlatiladi.
▪️Sanoatda cheklangan qo‘llanilishi: Laurensiy sun’iy ravishda ishlab chiqariladigan element bo‘lib, uning sanoat yoki tibbiyotda qo‘llanilishi cheklangan. U asosan ilmiy laboratoriyalarda sintez qilish uchun ishlatiladi.
""")

        elif belgi.lower() == "rf":
           print("""Rezerfordiy (Rf)
▪️Rezerfordiy – davriy jadvalning 104-elementi bo‘lib, 4-guruhga kiradi. Quyidagi qiziqarli faktlar rezerfordiy haqida sizni qiziqtirishi mumkin:
▪️Ernest Rezerford sharafiga nomlangan: Rezerfordiy elementi yangi elementlarni kashf etgan buyuk fizik Ernest Rutherford sharafiga nomlangan. U 1964-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Rezerfordiy tabiatda uchramaydi va faqat sun’iy yo‘l bilan yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U kaliforniy izotoplarini neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Rezerfordiy asosan yadro tadqiqotlarida qo‘llaniladi. U transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim ahamiyatga ega.
▪️Radioaktivlik: Rezerfordiy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari uzoq vaqt davomida yuqori darajadagi radioaktiv bo‘lib qoladi, shuning uchun u bilan ishlashda ehtiyotkorlik talab qilinadi.
▪️Ilmiy tadqiqotlar uchun qo‘llanilishi: Rezerfordiy asosan ilmiy izlanishlar va yangi elementlarni sintez qilishda qo‘llaniladi. Yadro fizikasi va kimyosida yangi tadqiqotlar uchun ishlatiladi.
▪️Sanoatda cheklangan qo‘llanilishi: Rezerfordiy sun’iy ravishda ishlab chiqariladigan element bo‘lib, sanoat yoki tibbiyotda keng qo‘llanilmaydi. Uning asosiy qo‘llanilishi ilmiy laboratoriyalarda sintez qilishda foydalaniladi.""")

        elif belgi.lower() == "db":
           print("""Dubniy (Db)
▪️Dubniy – davriy jadvalning 105-elementi bo‘lib, 5-guruhga kiradi. Quyidagi qiziqarli faktlar dubniy haqida sizni qiziqtirishi mumkin:
▪️Dubna shahriga nomlangan: Dubniy elementi Rossiyaning Dubna shahridagi yadro tadqiqotlari markaziga sharafiga nomlangan. U 1970-yilda sovet olimlari tomonidan sintez qilingan.
▪️Sun’iy element: Dubniy tabiatda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U amerikalik va sovet olimlari tomonidan kaliforniy va berkeliy izotoplariga neytronlar bilan bombardimon qilish orqali hosil qilingan.
▪️Yadro tadqiqotlarida qo‘llanilishi: Dubniy asosan yadro tadqiqotlarida qo‘llaniladi. U transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim ahamiyatga ega.
▪️Radioaktivlik: Dubniy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari uzoq vaqt davomida yuqori darajadagi radioaktiv bo‘lib qoladi, shuning uchun u bilan ishlashda ehtiyotkorlik talab qilinadi.
▪️Ilmiy tadqiqotlar uchun qo‘llanilishi: Dubniy asosan ilmiy izlanishlar va yangi elementlarni sintez qilishda qo‘llaniladi. Yadro fizikasi va kimyosida yangi tadqiqotlar uchun ishlatiladi.
▪️Sanoatda cheklangan qo‘llanilishi: Dubniy sun’iy ravishda ishlab chiqariladigan element bo‘lib, uning sanoat yoki tibbiyotda qo‘llanilishi cheklangan. U asosan ilmiy laboratoriyalarda sintez qilish uchun ishlatiladi.
""")

        elif belgi.lower() == "sg":
           print("""Siborgiy (Sg)
▪️Siborgiy – davriy jadvalning 106-elementi bo‘lib, 6-guruhga kiradi. Quyidagi qiziqarli faktlar siborgiy haqida sizni qiziqtirishi mumkin:
▪️Glen T. Seaborg sharafiga nomlangan: Siborgiy elementi amerikalik kimyogar Glen T. Seaborg sharafiga nomlangan. U 1974-yilda amerikalik olimlar tomonidan sintez qilingan.
▪️Sun’iy element: Siborgiy tabiatda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U kaliforniy izotoplariga neytronlar bilan bombardimon qilish orqali hosil qilinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Siborgiy asosan yadro tadqiqotlarida qo‘llaniladi. U transuran elementlarini sintez qilishda va yadro reaksiyalarini o‘rganishda muhim ahamiyatga ega.
▪️Radioaktivlik: Siborgiy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari uzoq vaqt davomida yuqori darajadagi radioaktiv bo‘lib qoladi, shuning uchun u bilan ishlashda ehtiyotkorlik talab qilinadi.
▪️Ilmiy tadqiqotlar uchun qo‘llanilishi: Siborgiy asosan ilmiy izlanishlar va yangi elementlarni sintez qilishda qo‘llaniladi. Yadro fizikasi va kimyosida yangi tadqiqotlar uchun ishlatiladi.
▪️Sanoatda cheklangan qo‘llanilishi: Siborgiy sun’iy ravishda ishlab chiqariladigan element bo‘lib, uning sanoat yoki tibbiyotda qo‘llanilishi cheklangan. U asosan ilmiy laboratoriyalarda sintez qilish uchun ishlatiladi.
""")

        elif belgi.lower() == "bh":
           print("""Boriy (Bh)
▪️Boriy – davriy jadvalning 107-elementi bo‘lib, 7-guruhga kiradi. Quyidagi qiziqarli faktlar boriy haqida sizni qiziqtirishi mumkin:
▪️Nils Bor sharafiga nomlangan: Boriy elementi Daniyalik fizik Nils Bor sharafiga nomlangan. Bohr kvant mexanikasi va atom modeli bo‘yicha muhim tadqiqotlar olib borgan olimlardan biri hisoblanadi.
▪️Sun’iy element: Boriy tabiatda uchramaydi va faqat sun’iy ravishda zarralar tezlatgichlari yordamida sintez qilinadi. U 1976-yilda germaniyalik olimlar tomonidan sintez qilingan.
▪️Yadro tadqiqotlarida qo‘llanilishi: Boriy asosan ilmiy tadqiqotlarda qo‘llaniladi. U transuran elementlar sintezida va yadro reaksiyalarini o‘rganishda muhim ahamiyatga ega.
▪️Radioaktivlik: Boriy kuchli radioaktiv element bo‘lib, alfa va beta nurlanishini chiqaradi. Uning izotoplari qisqa yashovchan bo‘lib, bir necha soniyalarda yemiriladi, bu esa uni yanada qiziqarli ilmiy tadqiqotlarga asos bo‘ladi.
▪️Ilmiy tadqiqotlar uchun qo‘llanilishi: Boriy elementining asosiy qo‘llanilishi ilmiy tadqiqotlarda va yangi elementlarni sintez qilishda bo‘ladi. Uning noyob va qisqa muddatli barqaror izotoplari yadro fizikasi bo‘yicha tadqiqotlar uchun ishlatiladi.
▪️Sanoatda cheklangan qo‘llanilishi: Boriyning sanoat yoki tibbiyotda qo‘llanilishi cheklangan. U faqat ilmiy laboratoriyalarda sintez qilinib, tadqiqot maqsadlarida qo‘llaniladi.""")

        elif belgi.lower() == "hs":
           print("""Hassiy (Hs)
▪️Hassiy – davriy jadvalning 108-elementi bo‘lib, og‘ir elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar hassiy haqida sizni qiziqtirishi mumkin:
▪️Germaniyadagi GSI tadqiqot markazi sharafiga nomlangan: Hassiy elementi Germaniyadagi Darmstadt shahrida joylashgan GSI (Gesellschaft für Schwerionenforschung) og‘ir ionlar tadqiqot markazi sharafiga nomlangan. Bu element 1984-yilda nemis olimlari tomonidan sintez qilingan.
▪️Sun’iy element: Hassiy tabiatda uchramaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. U kuriy va rutherfordiy kabi og‘ir elementlarning izotoplarini bombardimon qilish orqali hosil qilinadi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Hassiy asosan ilmiy tadqiqotlar va yadro reaksiyalarini o‘rganishda qo‘llaniladi. Bu element va uning izotoplari boshqa og‘ir elementlar sintezida foydalaniladi.
▪️Radioaktivlik: Hassiy kuchli radioaktiv element bo‘lib, uning izotoplari qisqa umr ko‘radi. U alfa nurlanishini chiqaradi va radioaktivligi tufayli uzoq muddatli qo‘llanilishga ega emas.
▪️Ilmiy tadqiqotlar uchun qo‘llanilish: Hassiy ilmiy laboratoriyalarda boshqa og‘ir elementlarni o‘rganish va sintez qilish uchun muhim ahamiyatga ega. U yadro fizikasi va kimyosidagi fundamental tadqiqotlar uchun qo‘llaniladi.
▪️Sanoatda qo‘llanilmasligi: Hassiy qisqa umrga ega bo‘lgani va yuqori radioaktivligi sababli sanoat yoki tibbiyot sohasida qo‘llanilmaydi. Uning asosiy qo‘llanilishi faqat ilmiy tadqiqotlar bilan cheklanadi.""")

        elif belgi.lower() == "mt":
           print("""Meytneriy (Mt)
▪️Meytneriy – davriy jadvalning 109-elementi bo‘lib, og‘ir elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar meitneriy haqida sizni qiziqtirishi mumkin:
▪️Liza Meitner sharafiga nomlangan: Meytneriy elementi avstriyalik fizik va yadroviy bo‘linish kashfiyotchilaridan biri bo‘lgan Liza Meitner sharafiga nomlangan. Bu element 1982-yilda Germaniyadagi GSI tadqiqot markazida nemis olimlari tomonidan sintez qilingan.
▪️Sun’iy element: Meytneriy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. Uni og‘ir ionlarni tezlatgichlar yordamida bombardimon qilish orqali hosil qilishadi.
▪️Cheklangan ma’lumotlar: Meytneriy juda qisqa umrga ega bo‘lgan izotoplardan iborat bo‘lib, ularning xususiyatlari hali to‘liq o‘rganilmagan. Odatda uning izotoplari soniyalardan kamroq vaqt davomida mavjud bo‘ladi.
▪️Radioaktivlik: Meytneriy kuchli radioaktiv element bo‘lib, qisqa umrli alfa nurlanishini chiqaradigan izotoplarga ega. Bu uni faqat ilmiy tadqiqotlar uchun mos qiladi.
▪️Yadro fizikasi tadqiqotlarida qo‘llanilishi: Meytneriy yadro fizikasi va og‘ir elementlar kimyosini o‘rganish uchun qo‘llaniladi. Bu elementning kimyoviy xususiyatlari hali yetarli darajada o‘rganilmagan, ammo ilmiy izlanishlarda qimmatli rol o‘ynaydi.
▪️Sanoatda qo‘llanilmasligi: Meytneriy juda qisqa umrga ega bo‘lgani va yuqori radioaktivligi tufayli sanoat yoki tibbiyotda keng qo‘llanilmaydi. Uning asosiy qo‘llanilishi ilmiy izlanishlar bilan cheklanadi.
""")

        elif belgi.lower() == "ds":
           print("""Darmshtadtiy (Ds)
▪️Darmshtadtiy – davriy jadvalning 110-elementi bo‘lib, og‘ir elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar darmshtadtiy haqida sizni qiziqtirishi mumkin:
▪️Darmshtadt shahri sharafiga nomlangan: Darmshtadtiy elementi Germaniyaning Darmshtadt shahrida joylashgan GSI tadqiqot markazida sintez qilingan va shu shahar sharafiga nomlangan. U 1994-yilda nemis olimlari tomonidan ochilgan.
▪️Sun’iy element: Darmshtadtiy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. Bu element og‘ir ionlarni bir-biriga yuqori energiyada bombardimon qilish orqali hosil qilinadi.
▪️Cheklangan xususiyatlar: Darmshtadtiyning kimyoviy va fizik xususiyatlari hali to‘liq o‘rganilmagan, chunki uning izotoplari juda qisqa umr ko‘radi. Uning izotoplari soniyalardan kam vaqt davomida mavjud bo‘ladi.
▪️Radioaktivlik: Darmshtadtiy kuchli radioaktiv element bo‘lib, qisqa umrli izotoplarni hosil qiladi. U alfa va beta nurlanishini chiqaradi, shuning uchun bu element bilan ishlashda ehtiyotkorlik talab etiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Darmshtadtiy asosan yadro fizikasi va og‘ir elementlar kimyosini o‘rganish uchun ishlatiladi. Bu element yangi transuran elementlarini sintez qilishda muhim rol o‘ynaydi.
▪️Sanoatda qo‘llanilmasligi: Darmshtadtiyning qisqa umr va yuqori radioaktivligi tufayli uni sanoatda yoki tibbiyotda qo‘llashning iloji yo‘q. Uning asosiy qo‘llanilishi faqat ilmiy izlanishlar bilan cheklanadi.""")

        elif belgi.lower() == "rg":
           print("""Rentgeniy (Rg)
▪️Rentgeniy – davriy jadvalning 111-elementi bo‘lib, og‘ir elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar rentgeniy haqida sizni qiziqtirishi mumkin:
▪️Vilgelm Rentgen sharafiga nomlangan: Rentgeniy elementi rentgen nurlari kashfiyotchisi bo‘lgan nemis fizik Vilgelm Rentgen sharafiga nomlangan. U 1994-yilda Germaniyadagi GSI tadqiqot markazida sintez qilingan va 2004-yilda rasman tan olingan.
▪️Sun’iy element: Rentgeniy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. Bu element og‘ir ionlarni tezlatgich yordamida yuqori energiyada bombardimon qilish orqali hosil qilinadi.
▪️Cheklangan ma’lumotlar: Rentgeniy juda qisqa umrga ega bo‘lgan izotoplardan iborat bo‘lib, ularning xususiyatlari hali to‘liq o‘rganilmagan. Uning eng barqaror izotopi atigi bir necha soniya davomida mavjud bo‘ladi.
▪️Radioaktivlik: Rentgeniy kuchli radioaktiv element bo‘lib, qisqa umrli izotoplarini hosil qiladi. U alfa nurlanishini chiqaradi, va radioaktivligi tufayli faqat ilmiy maqsadlarda qo‘llaniladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Rentgeniy asosan ilmiy laboratoriyalarda yadro tadqiqotlari va yangi og‘ir elementlarni o‘rganishda qo‘llaniladi. Uning kimyoviy xususiyatlari haqida cheklangan ma’lumot mavjud.
▪️Sanoatda qo‘llanilmasligi: Rentgeniy juda qisqa umrga ega bo‘lgani va yuqori radioaktivligi sababli sanoat yoki tibbiyot sohasida foydalanilmaydi. Uning asosiy qo‘llanilishi faqat ilmiy tadqiqotlar bilan cheklanadi.""")

        elif belgi.lower() == "cn":
            print("""Kopernitsiy (Cn)
▪️Kopernitsiy – davriy jadvalning 112-elementi bo‘lib, og‘ir elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar kopernitsiy haqida sizni qiziqtirishi mumkin:
▪️Nikolay Kopernik sharafiga nomlangan: Kopernitsiy elementi mashhur astronom va olim Nikolay Kopernik sharafiga nomlangan. U 1996-yilda Germaniyaning GSI tadqiqot markazida sintez qilingan va 2009-yilda rasman tan olingan.
▪️Sun’iy element: Kopernitsiy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. Og‘ir ionlar bir-biriga tezlatgich yordamida yuqori energiyada bombardimon qilish orqali hosil qilinadi.
▪️Cheklangan ma’lumotlar: Kopernitsiyning kimyoviy va fizik xususiyatlari hali to‘liq o‘rganilmagan, chunki uning izotoplari juda qisqa umrga ega. Eng barqaror izotopi atigi bir necha soniya davomida mavjud bo‘ladi.
▪️Radioaktivlik: Kopernitsiy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. U qisqa umrli izotoplarga ega bo‘lgani uchun asosan ilmiy tadqiqotlar uchun ishlatiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Kopernitsiy yadro fizikasi va og‘ir elementlar kimyosini o‘rganishda muhim element hisoblanadi. Yangi transuran elementlarni sintez qilishda va ularning xususiyatlarini o‘rganishda qo‘llaniladi.
▪️Sanoatda qo‘llanilmasligi: Kopernitsiyning yuqori radioaktivligi va qisqa umri tufayli uni sanoatda yoki tibbiyotda qo‘llashning iloji yo‘q. Uning asosiy qo‘llanilishi ilmiy laboratoriyalarda yangi elementlarni sintez qilish bilan cheklanadi.""")

        elif belgi.lower() == "nh":
           print("""Nihoniy (Nh)
▪️Nihoniy – davriy jadvalning 113-elementi bo‘lib, sintetik elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar nihoniy haqida sizni qiziqtirishi mumkin:
▪️Yaponiya sharafiga nomlangan: Nihoniy elementi Yaponiyaning nomidan olingan. Nihon so‘zi “Yaponiya” degan ma’noni bildiradi. Bu element 2004-yilda Yaponiyaning RIKEN ilmiy markazida sintez qilingan.
▪️Sun’iy element: Nihoniy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. Bu element og‘ir ionlarni yuqori energiyada bir-biriga bombardimon qilish orqali olinadi.
▪️Radioaktivlik: Nihoniy kuchli radioaktiv element bo‘lib, uning izotoplari juda qisqa umrga ega. Eng barqaror izotopi atigi bir necha soniya davomida mavjud bo‘ladi.
▪️Kimyoviy xususiyatlari: Nihoniyning kimyoviy xususiyatlari hali to‘liq o‘rganilmagan. U davriy jadvalning 13-guruhiga kiradi va uning xatti-harakati boshqa guruh elementlari bilan o‘xshash bo‘lishi mumkin deb taxmin qilinmoqda.
▪️Yadro tadqiqotlarida qo‘llanilishi: Nihoniy asosan ilmiy izlanishlar va yangi transuran elementlarni sintez qilishda qo‘llaniladi. Uning yadro fizikasi va kimyosidagi o‘rganilishlari elementlarning chegaralarini kengaytirishga xizmat qiladi.
▪️Sanoatda qo‘llanilmasligi: Nihoniyning yuqori radioaktivligi va qisqa umrga ega bo‘lgani sababli uni sanoat yoki tibbiyot sohasida ishlatishning iloji yo‘q. Uning asosiy qo‘llanilishi ilmiy tadqiqotlar bilan cheklangan.""")

        elif belgi.lower() == "fl":
           print("""Fleroviy (Fl)
▪️Fleroviy – davriy jadvalning 114-elementi bo‘lib, sun'iy elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar fleroviy haqida sizni qiziqtirishi mumkin:
▪️Georgiy Flerov sharafiga nomlangan: Fleroviy elementi sovet yadroviy fizigi Georgiy Flerov sharafiga nomlangan. U 1999-yilda Rossiyaning Dubna shahridagi Birlashgan Yadro Tadqiqotlari Institutida sintez qilingan.
▪️Sun’iy element: Fleroviy tabiatda mavjud bo‘lmaydi va faqat sun’iy ravishda yadro reaktorlari yoki zarralar tezlatgichlari yordamida sintez qilinadi. Bu element kaliforniy va kaltsiy izotoplarini bir-biriga yuqori energiyada bombardimon qilish orqali olinadi.
▪️Cheklangan ma’lumotlar: Fleroviy izotoplarining barqarorligi juda qisqa, eng barqaror izotopi bir necha soniyagina mavjud bo‘ladi. Shu sababli, uning fizik va kimyoviy xususiyatlari haqida ma’lumotlar cheklangan.
▪️Radioaktivlik: Fleroviy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari qisqa umrga ega bo‘lgani uchun asosan ilmiy tadqiqotlar uchun ishlatiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Fleroviy transuran elementlarini sintez qilish va yadro reaksiyalarini o‘rganishda qo‘llaniladi. U yadro fizikasi va kimyosi tadqiqotlarida muhim o‘rin tutadi.
▪️Sanoatda qo‘llanilmasligi: Fleroviy yuqori radioaktivligi va qisqa umrga ega bo‘lgani sababli uni sanoatda yoki tibbiyotda ishlatishning imkoni yo‘q. U faqat ilmiy tadqiqotlarda yangi elementlarni sintez qilishda ishlatiladi.""")

        elif belgi.lower() == "mc":
           print("""Moskoviy (Mc)
▪️Moskoviy – davriy jadvalning 115-elementi bo‘lib, sun'iy elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar moskoviy haqida sizni qiziqtirishi mumkin:
▪️Moskva sharafiga nomlangan: Moskoviy elementi Rossiya poytaxti Moskva sharafiga nomlangan. Bu element 2003-yilda Rossiyaning Dubna shahridagi Birlashgan Yadro Tadqiqotlari Institutida sintez qilingan va 2016-yilda rasman tan olingan.
▪️Sun’iy element: Moskoviy tabiatda mavjud bo‘lmaydi va faqat sun’iy ravishda sintez qilinadi. U og‘ir elementlarning yuqori energiyada bir-biriga bombardimon qilinishi orqali olinadi, masalan, ameritsiy va kaltsiy izotoplari yordamida.
▪️Cheklangan ma’lumotlar: Moskoviyning barqaror izotoplari juda qisqa umrga ega, faqat bir necha millisoniyalarda parchalanadi. Shu sababli, uning kimyoviy va fizik xususiyatlari to‘liq o‘rganilmagan.
▪️Radioaktivlik: Moskoviy kuchli radioaktiv element bo‘lib, u alfa nurlanishi chiqaradi va juda qisqa umrli izotoplarga ega. Shuning uchun u faqat ilmiy maqsadlar uchun qo‘llaniladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Moskoviy asosan yadro tadqiqotlarida va yangi transuran elementlarni sintez qilishda ishlatiladi. Uning o‘rganilishi yadro fizikasi va kimyosining chegaralarini kengaytiradi.
▪️Sanoatda qo‘llanilmasligi: Moskoviy qisqa umrga ega bo‘lgani va yuqori radioaktivligi sababli sanoat yoki tibbiyotda qo‘llanilmaydi. U ilmiy laboratoriyalarda yangi elementlarni o‘rganish va sintez qilish uchun qo‘llaniladi.
""")

        elif belgi.lower() == "lv":
           print("""Livermoriy (Lv)
▪️Livermoriy – davriy jadvalning 116-elementi bo‘lib, sun'iy elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar livermoriy haqida sizni qiziqtirishi mumkin:
▪️Livermore sharafiga nomlangan: Livermoriy elementi AQShning Livermore shahridagi Lawrence Livermore Milliy laboratoriyasining sharafiga nomlangan. U 2000-yilda AQSh va Rossiya olimlari tomonidan birgalikda sintez qilingan.
▪️Sun’iy element: Livermoriy tabiatda uchramaydi va faqat sun’iy ravishda sintez qilinadi. U og‘ir ionlar bir-biriga yuqori energiyada bombardimon qilinishi orqali olinadi, masalan, kaliforniy va kaltsiy izotoplarini birlashtirish orqali.
▪️Cheklangan ma’lumotlar: Livermoriy elementining kimyoviy va fizik xususiyatlari hali to‘liq o‘rganilmagan, chunki uning izotoplari juda qisqa umrga ega. Eng barqaror izotopi atigi bir necha millisoniyalarda parchalanadi.
▪️Radioaktivlik: Livermoriy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari juda qisqa umrga ega, shuning uchun u asosan ilmiy tadqiqotlar uchun ishlatiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Livermoriy yadro fizikasi va kimyosini o‘rganishda, yangi transuran elementlarni sintez qilishda va yadro reaksiyalarini tushunishda muhim ahamiyatga ega.
▪️Sanoatda qo‘llanilmasligi: Livermoriy yuqori radioaktivligi va qisqa umrga ega bo‘lgani sababli sanoat yoki tibbiyotda qo‘llanilmaydi. U faqat ilmiy laboratoriyalarda yangi elementlarni sintez qilishda qo‘llaniladi.""")

        elif belgi.lower() == "ts":
           print("""Tennessiy (Ts)
▪️Tennessiy – davriy jadvalning 117-elementi bo‘lib, sun'iy elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar tennessiy haqida sizni qiziqtirishi mumkin:
▪️Tennessee shtati sharafiga nomlangan: Tennessiy elementi AQShning Tennessee shtati sharafiga nomlangan. Bu element 2010-yilda Rossiya va AQSh olimlari tomonidan birgalikda sintez qilingan.
▪️Sun’iy element: Tennessiy tabiatda mavjud bo‘lmaydi va faqat sun’iy ravishda sintez qilinadi. U og‘ir ionlar bir-biriga yuqori energiyada bombardimon qilinishi orqali olinadi.
▪️Cheklangan ma’lumotlar: Tennessiyning kimyoviy va fizik xususiyatlari hali to‘liq o‘rganilmagan, chunki uning izotoplari juda qisqa umrga ega. Eng barqaror izotopi bir necha millisoniyalarda parchalanadi.
▪️Radioaktivlik: Tennessiy kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari qisqa umrga ega, shuning uchun u asosan ilmiy tadqiqotlar uchun ishlatiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Tennessiy yadro fizikasi va kimyosini o‘rganishda, yangi transuran elementlarni sintez qilishda va yadro reaksiyalarini tushunishda muhim ahamiyatga ega.
▪️Sanoatda qo‘llanilmasligi: Tennessiy yuqori radioaktivligi va qisqa umrga ega bo‘lgani sababli sanoat yoki tibbiyotda qo‘llanilmaydi. U faqat ilmiy laboratoriyalarda yangi elementlarni sintez qilishda qo‘llaniladi.""")

        elif belgi.lower() == "og":
           print("""Oganesson (Og)
▪️Oganesson – davriy jadvalning 118-elementi bo‘lib, sun'iy elementlar qatoriga kiradi. Quyidagi qiziqarli faktlar oganesson haqida sizni qiziqtirishi mumkin:
▪️Yuri Oganesson sharafiga nomlangan: Oganesson elementi rossiyalik olim Yuri Oganesson sharafiga nomlangan. U 2002-yilda Rossiya va AQSh olimlari tomonidan birgalikda sintez qilingan.
▪️Sun’iy element: Oganesson tabiatda mavjud bo‘lmaydi va faqat sun’iy ravishda sintez qilinadi. U og‘ir ionlar bir-biriga yuqori energiyada bombardimon qilinishi orqali olinadi.
▪️Cheklangan ma’lumotlar: Oganessonning kimyoviy va fizik xususiyatlari hali to‘liq o‘rganilmagan, chunki uning izotoplari juda qisqa umrga ega. Eng barqaror izotopi bir necha millisoniyalarda parchalanadi.
▪️Super og‘ir element: Oganesson eng og‘ir elementlardan biri hisoblanadi. Uning atom massasi 294 ga teng va bu element transuran elementlarining oxirgi vakili bo‘lib, unchalik barqaror emas.
▪️Radioaktivlik: Oganesson kuchli radioaktiv element bo‘lib, alfa nurlanishini chiqaradi. Uning izotoplari qisqa umrga ega, shuning uchun u asosan ilmiy tadqiqotlar uchun ishlatiladi.
▪️Yadro tadqiqotlarida qo‘llanilishi: Oganesson yadro fizikasi va kimyosini o‘rganishda, yangi transuran elementlarni sintez qilishda va yadro reaksiyalarini tushunishda muhim ahamiyatga ega.
▪️Sanoatda qo‘llanilmasligi: Oganesson yuqori radioaktivligi va qisqa umrga ega bo‘lgani sababli sanoat yoki tibbiyotda qo‘llanilmaydi. U faqat ilmiy laboratoriyalarda yangi elementlarni sintez qilishda qo‘llaniladi.""")

        else:
           print("Bunday element mavjud emas!")

davriy_jadval()