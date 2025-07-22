def ekvalentlik():    #Funksiya yaratish
    """Bu funksiya kimyo fanidagi ekvivalentlik mavzusi va undagi masalalar ni tezlik bilan javobini chiqarib beradi. """
    faollashtiruv = True
    while faollashtiruv:     #while ni faollashtirish
     qiymat = input("Oddiy moddalarning ekvalentligini topish uchun '1'ni \nKislota yoki Asos ning ekvalentligi topish '2'ni \nOksid yoki Tuzning ekvalentligini topish '3'ni \nDasturni to'xtatish uchun 'exit' deb yozing \n>>>")
     if qiymat == "exit":           #qiymat 'exit'ga teng bo'lganda dasturni to'xtatish
        break
     
     if qiymat == "1":            #Foydalanuvchi '1'ni kiritsa oddiy moddaning ekvalentligini xisoblash
        print("Muhim eslatma: Gazlarning ekvalentligini xisoblashda gazlarning atom massalari olinadi.")
        nomi = input("Oddiy moddaning nomini kiriting:")
        massa = int(input("Oddiy moddaning massasini kiriting:"))
        valentlik = int(input("Oddiy moddaning valentligini kiriting:"))
        print(f"{nomi.title()}ning ekvalentligi {massa/valentlik}ga teng.")
        print('='*50)  #Natijani '=' bilan ajratish

     elif qiymat =="2":            #Foydalanuvchi '2'ni kiritsa murakkab moddaning ekvalentligini xisoblash 
        print("Muhim eslatma: Kislota larning ekvalentligi vodorod(H) soni , asoslarning enkvalentligi ohash(OH) soni yordamida topiladi. ")
        nomi2 = input("Kislota yoki Asos nomini kiriting:")
        massa1 = int(input("Kislota yoki Asos massasini kiriting:"))
        h_yoki_oh = int(input("Kislota bo'lsa H sonini, Asos bo'lsa OH sonini kiriting:"))
        print(f"{nomi2.title()}ning ekvalentligi {massa1/h_yoki_oh}ga teng.")
        print('='*50)  #Natijani '=' bilan ajratish

     elif qiymat == "3":          #Foydalanuvchi '3'ni kiritsa murakkab moddaning ekvalentligini xisoblash
        print("Muhim eslatma: Bu dastur o'rta tuzlarning ekvalentligini hisoblaydi.")
        nomi3 = input("Oksid yoki Tuzning nomini kiriting:")
        massa3 = float(input("Oksid yoki Tuz nng massasini kiriting:"))
        metal_s = int(input("Oksid yoki Tuzdagi metal atomi sonini kiriting:"))
        metal_v = int(input("Metalning valentligini kiriting:"))
        print(f"{nomi3.title()}ning valentligi {massa3/(metal_s+metal_v)}ga teng.")
        print('='*50)  #Natijani '=' bilan ajratish

    else:
       print("Xato belgi kiritdinggiz.")   

ekvalentlik()      #Funksiyani faollashtirish 