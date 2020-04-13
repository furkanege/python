# LİSTELER NOT: LİSTE ELEMANLARI 0'INCI ELEMANDAN BAŞLAR. (0),(1),(2),(3),...,(n)
# LİSTE OLUŞTURMA
from typing import List

programlar: List[str] = ['python','java','html','css']
# LİSTEYE ELEMAN EKLEME
programlar.append('arduino')
# LİSTEYİ YAZDIRMA
programlar
# EKRAN ÇIKTISI
['python', 'java', 'html', 'css', 'arduino']
# İLK ELEMANDAN İKİNCİ ELEMANA KADAR LİSTE ELEMANLARINI GÖRÜNTÜLEME
programlar[:2]
['css']
# İKİNCİ ELEMANDAN SON ELEMANA KADAR LİSTE ELEMANLARINI GÖRÜNTÜLEME
programlar[1:]
['java', 'html']
# İLK ELEMANDAN ÜÇÜNCÜ ELEMANA KADAR LİSTE ELEMANLARINI GÖRÜNTÜLEME
programlar[0:2]
['python', 'java', 'html']
# İSTENİLEN ELEMANIN LİSTEDE KAÇ DEFA KULLANILDIĞINI GÖRMEK NOT: YOKSA EKRANA "0" YAZAR
programlar.count('pythonx')
0
programlar.count('python')
1
# LİSTEYE ELEMAN EKLEMENİN YOLLARI -1
programlar.extend(['csharp'])
programlar
# EKRAN ÇIKTISI
['python', 'java', 'html', 'css', 'arduino', 'csharp']
# LİSTEYE ELEMAN EKLEMENİN YOLLARI -2
programlar + ['perl', 'php']
['python', 'java', 'html', 'css', 'arduino', 'csharp', 'perl', 'php']
# ELEMANIN LİSTEDE Kİ KONUMUNU EKRANA YAZAR
programlar.index('python')
0
# LİSTEYE İSTENİLEN BİR KONUMDAN EKLEME YAPMA NOT: İNDEKS VERİP SONRASINA EKLETİR
programlar.insert(3,'prolog')
programlar
['python', 'java', 'html', 'prolog', 'c++', 'css', 'arduino', 'csharp']
# LİSTEDEN EN SON ELEMANI ÇIKARMA
programlar.pop()
'csharp'
# LİSTEDEN İSTENİLEN ELEMANI ÇIKARMA
programlar.remove('c++')
# LİSTENİN ELEMANLARINI SONDAN BAŞA DOĞRU YAZDIRMA
programlar.reverse()
# LİSTEDEN ÖNCE SAYI ELEMANLARINI EKRANA YAZDIRMA
programlar.append(123)
programlar.append(456)
programlar.sort()
# LİSTENİN KAÇ ELEMANDAN OLUŞTUĞUNU BULMA
len(programlar)
# LİSTEYİ TAM SAYI İLE ÇARPMAK
programlar*2