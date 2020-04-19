from flask import Flask
"""Flask indirmemiz bitti projemize import ettik. Yani artık bu projede Flask'ı kullanabileceğiz."""
"""Bazı durumlarda 'pip install --user Flask' ile de kurmanız gerekebilir. Permission denied hatası verdiği görülmüştür."""

"""Flask kütüphanemizin flask sınıfını kullanarak bir nesne oluşturalım. Mantığını öğretmekle zamanınızı çalmayacağım. 
Zaten biliyorsunuzdur yayına alma safhasıan geldiyseniz."""
app = Flask(__name__)

#Şimdi de kök dizinimizi, yani ana URL'mizi tanımlayalım. localhost'da aktif olacaktır.
@app.route('/') #URL tanımlama kısmımız
def mesaj(): #mesaj adlı bir fonksiyon tanımlıyoruz.
    return 'Selamin Aleykum' #Ve ekrana dönecek olan değeri yazıyoruz. Biz ekrana selam döndürelim.

#Bu kodlar ise bizim dosyamızı çalıştırmamızı, yani ayıklayıp yayınlamamızı sağlıyor.
"""
if __name__ == '__main__':
    app.debug = True
    app.run(host= 'localhost', port= 5000)
""" 
#Localde çalıştıracağımız için host'u localhost seçiyoruz ve portu 5000 yapıyoruz.
#Web'de bu 80'dir ve bu kodlara gerek yoktur.
