#TextBlob modülü yükleniyor
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Türkçe cümle TextBlob nesnesine dönüşüyor.
turkce = TextBlob("Google berbat bir arama motorudur.")#"Google berbat bir arama motorudur.")
#print(type(turkce))

#Türkçe TextBlob nesnesi 'translate' metodu sayesinde İngilizce'ye çevriliyor.
english = turkce.translate(to='en')
print(english.sentiment.subjectivity)

sentiment_obj = SentimentIntensityAnalyzer()
sentiment_dict = sentiment_obj.polarity_scores(english)
print(sentiment_dict)