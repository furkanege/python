print ("Merhaba, lütfen soruları istenilen şekilde cevaplayınız.")
isim = input("İsminiz?: ")
print ("İsminiz {}.".format(isim))

while True:
    cinsiyet = input("Cinsiyetiniz:(erkek/kadın): ")
    yas = int (input("Yaşınız: "))

    if (yas >= 1 and yas < 18 and cinsiyet.lower() == "erkek"):
        print("Evet {}, soruları cevaplamaya devam edelim.".format(isim,))
        break
    if (yas >= 1 and yas < 18 and cinsiyet.lower() == "kadın"):
        print("Evet {}, soruları cevaplamaya devam edelim.".format(isim,))
        break
    elif (yas >= 18 and cinsiyet.lower() == "erkek"):
        print("Evet {} bey, soruları cevaplamaya devam edelim.".format(isim))
        break
    elif (yas >= 18 and cinsiyet.lower() == "kadın"):
        print("Evet {} hanım, soruları cevaplamaya devam edelim.".format(isim))
        break
    else: print("Sn. {}, hatalı girişte bulundunuz.".format(isim))
    continue

seyehat = input("Yakın zamanda özellikle çin ve uzak doğu ülkeleri başta olmak üzere veya başka herhangi bir ülkeye seyehat ettiniz mi?(evet/hayır): ")

if (seyehat.lower() == "hayır"):
    print("Maalesef 11.03.2020 tarihli açıklamaya göre ülkemizde CORONAVIRUS, yani 'Covid-19' vakası görüldüğü açıklandı. \nTüm soruları 10 üzerinden rakam olarak cevaplayınız.")
    yurtici_soru0 = int(input("Aktif olarak toplu taşıma kullanıyor musunuz?(0-10): "))
    yurtici_soru1 = int(input("Kendinizi halsiz hissediyor musunuz?(0-10): "))
    yurtici_soru2 = int(input("Burun akıntınız var mı?(0-10): "))
    yurtici_soru3 = int(input("Boğaz ağrınız var mı?(0-10): "))
    yurtici_soru4 = int(input("Öksürüğünüz var mı?(0-10): "))
    yurtici_soru5 = int(input("Ateşiniz var mı?(0-10): "))
    yurtici_soru6 = int(input("Nefes almakta zorlanıyor musunuz?(0-10): "))
    yurtici_soru7 = int(input("İnsanlarla çok sık şekilde tokalaşıyor musunuz?(0-10): "))
    yurtici_soru8 = int(input("Herhangi bir insan ile dudak temasınız oldu mu?(0-10): "))
    yurtici_soru9 = int(input("Son günlerde yurtdışından gelmiş biri ile temasınız oldu mu?(0-10): "))
    yurtici_soru10 = int(input("Koronavirüs taşıyan herhangi biri ile temasınız oldu mu?(0-10): "))
    yurtici_soru_toplam = (yurtici_soru0*0.8) + (yurtici_soru1*0.3) + (yurtici_soru2*0.4) + (yurtici_soru3*0.5) + (yurtici_soru4*0.6) + (yurtici_soru5*0.7) + (yurtici_soru6*0.8) + (yurtici_soru7*0.9) + (yurtici_soru8*1) + (yurtici_soru9*1.5) + (yurtici_soru10*2.5)

    if (yurtici_soru_toplam >= 79 and yurtici_soru_toplam <= 100):
        print("Sn. {}, 100 üzerinden {} puan aldınız. \nTestimize göre yüksek ihtimalle hastasınız(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nLütfen mümkün olan en kısa sürede ve telaş yapmadan size en yakın sağlık kuruluşuna (hastane, sağlık ocağı vs.) başvurunuz!".format(isim,yurtici_soru_toplam))
    elif (yurtici_soru_toplam >= 62 and yurtici_soru_toplam < 79):
        print("Sn. {}, hasta olma ihtimaliniz çok yüksek, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nTelaşlanmadan size en yakın sağlık kuruluşuna (hastane, sağlık ocağı vs.) başvurunuz!".format(isim,yurtici_soru_toplam))
    elif (yurtici_soru_toplam >= 50 and yurtici_soru_toplam < 62):
        print("Sn. {}, hasta olma ihtimalinizin az olması ile birlikte, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz.".format(isim,yurtici_soru_toplam))
    elif (yurtici_soru_toplam >= 40 and yurtici_soru_toplam < 50):
        print("Sn. {}, hasta olma ihtimalinizin çok az olması ile birlikte, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz.".format(isim,yurtici_soru_toplam))
    elif (yurtici_soru_toplam >= 0 and yurtici_soru_toplam <20):
        print("Sn. {}, testimiz sonucuna göre Koronavirüs, yani 'Covid-19' şüpheniz bulunmamakla birlikte, 100 üzerinden {} puan aldınız \n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz. Sağlıklı günler dileriz.".format(isim,yurtici_soru_toplam))
    else:
        print("Sn. {}, hatalı girişte bulundunuz.".format(isim))

if (seyehat.lower() == "evet"):
    print("Sn. {}, düşük olmakla birlikte salgına yakalanmış olma ihtimaliniz bulunmakta. Tüm soruları 10 üzerinden rakam olarak cevaplayınız.".format(isim))
    yurtdisi_soru0 = int(input("Burun akıntınız var mı?(0-10): "))
    yurtdisi_soru1 = int(input("Boğaz ağrınız var mı?(0-10): "))
    yurtdisi_soru2 = int(input("Öksürüğünüz var mı?(0-10): "))
    yurtdisi_soru3 = int(input("Ateşiniz var mı?(0-10): "))
    yurtdisi_soru4 = int(input("Nefes almakta zorlanıyor musunuz?(0-10): "))
    yurtdisi_soru5 = int(input("Seyatinizde toplu taşıma kullandınız mı?(0-10): "))
    yurtdisi_soru6 = int(input("Seyahtinizde toplu alanlara (spor müsabakaları, konser alanları, festivaller) girdiniz mi?(0-10): "))
    yurtdisi_soru7 = int(input("Peki kendinizi bu seyahetten sonra olağan dışı şekilde yorgun hissettiniz mi?(0-10): "))
    yurtdisi_soru8 = int(input("Seyatinizde insanlarla çok sık şekilde tokalaştınız mı?(0-10): "))
    yurtdisi_soru9 = int(input("Seyatinizde herhangi bir insan ile dudak temasınız oldu mu?(0-10): "))
    yurtdisi_soru10 = int(input("Seyatinizde Koronavirüs taşıyan herhangi biri ile temasınız oldu mu?(0-10): "))
    yurtdisi_soru_toplam = (yurtdisi_soru0*0.2) + (yurtdisi_soru1*0.3) + (yurtdisi_soru2*0.4) + (yurtdisi_soru3*0.5) + (yurtdisi_soru4*0.6) + (yurtdisi_soru5*0.9) + (yurtdisi_soru6*1.1) + (yurtdisi_soru7*1.2) + (yurtdisi_soru8*1.3) + (yurtdisi_soru9*1.5) + (yurtdisi_soru10*2.0)

    if (yurtdisi_soru_toplam >= 79 and yurtdisi_soru_toplam >= 100):
        print("Sn. {}, 100 üzerinden {} puan aldınız. \nTestimize göre yüksek ihtimalle hastasınız(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nLütfen mümkün olan en kısa sürede ve telaş yapmadan size en yakın sağlık kuruluşuna (hastane, sağlık ocağı vs.) başvurunuz!".format(isim,yurtici_soru_toplam))
    elif (yurtdisi_soru_toplam >= 62 and yurtdisi_soru_toplam < 79):
        print("Sn. {}, hasta olma ihtimaliniz çok yüksek, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nTelaşlanmadan size en yakın sağlık kuruluşuna (hastane, sağlık ocağı vs.) başvurunuz!".format(isim,yurtici_soru_toplam))
    elif (yurtdisi_soru_toplam >= 50 and yurtdisi_soru_toplam < 62):
        print("Sn. {}, hasta olma ihtimalinizin az olması ile birlikte, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz.".format(isim,yurtici_soru_toplam))
    elif (yurtdisi_soru_toplam >= 40 and yurtdisi_soru_toplam < 50):
        print("Sn. {}, hasta olma ihtimalinizin çok az olması ile birlikte, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz.".format(isim,yurtici_soru_toplam))
    elif (yurtdisi_soru_toplam >= 0 and yurtdisi_soru_toplam <20):
        print("Sn. {}, testimiz sonucuna göre Koronavirüs, yani 'Covid-19' şüpheniz bulunmamakla birlikte, 100 üzerinden {} puan aldınız\n(Testimizin resmi bir test olmaması ve sadece sorulara dayalı yanıtlar verdiği gerçeğini sakın unutmayın.). \nEğer mümkün ise herhangi bir sağlık kuruluşuna (hastane, sağlık ocağı vs.) danışıp hastalık ile ilgili daha detaylı bilgi alabilirsiniz. Sağlıklı günler dileriz.".format(isim,yurtici_soru_toplam))
    else:
        print("Sn. {}, hatalı girişte bulundunuz.".format(isim))


"""
isim = input("İsminiz?: ")
cinsiyet = input("Cinsiyetiniz(erkek veya kadın:)")
yas = int (input("Şimdi de yaşınızı giriniz: "))
if (yas >= 1 and yas < 18 and cinsiyet.lower()=="erkek"):
    print("Peki {}, soruları cevaplamaya devam edelim.".format(isim,))
"""