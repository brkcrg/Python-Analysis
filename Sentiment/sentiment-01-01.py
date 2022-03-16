#TextBlob modülü yükleniyor
from textblob import TextBlob

#Türkçe cümle TextBlob nesnesine dönüşüyor.
turkce = TextBlob("CHP Grup Başkanvekili Özgür Özel de, Elvan'ın açıklamasına çok sert tepki gösterdi.")
#print(type(turkce))

#Türkçe TextBlob nesnesi 'translate' metodu sayesinde İngilizce'ye çevriliyor.
english = turkce.translate(to='en')
"""
#sentiment nesnesi ile cümlenin porality ve subjectivity analizi yapılıp değerleri alınıyor.
#polarity duygu değeridir. 1 en olumlu değeri, -1 en olumsuz değeri ifade eder.
#subjectivity öznel değerlendirme veya genel değerlendirme seviyesini belirtir.
#1 değeri duygu değerinin BEN merkezli, kişisel bir görüş olduğunu belirtir.
#-1 değeri ise duygunun genel bir değerlendirme görüşü olduğunu belirtir.
duygu = english.sentiment
#duygu = english.sentiment.polarity
#duygu = english.sentiment.subjectivity
print(duygu) 
"""
#olumsuz cümle örneği
turkce2 = TextBlob("Yağmurlu havadan nefret ediyorum.")
english2 = turkce2.translate(to='en')
duygu2 = english2.sentiment
#duygu2 = english.sentiment.polarity
#duygu2 = english.sentiment.subjectivity
print(duygu2)

#olumsuz cümle ve genel görüş örneği
turkce3 = TextBlob("Dışarıda çok fırtınalı bir hava var.")
english3 = turkce3.translate(to='en')
duygu3 = english3.sentiment
#duygu3 = english.sentiment.polarity
#duygu3 = english.sentiment.subjectivity
print(duygu3)

#pek olumlu olmayan cümle ve genel görüş örneği
turkce4 = TextBlob("Genel olarak yağmurlu havadan nefret edilir.")
english4 = turkce4.translate(to='en')
duygu4 = english4.sentiment
#duygu4 = english.sentiment.polarity
#duygu4 = english.sentiment.subjectivity
print(duygu4)