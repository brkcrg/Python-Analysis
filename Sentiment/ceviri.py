from textblob import TextBlob

english = TextBlob("Python is a high-level, general-purpose programming language.")

turkce = english.translate(to='tr')
print(turkce)

""" turkce = TextBlob("Python, üst düzey, genel amaçlı bir programlama dilidir.")
english = turkce.translate(to='en')
print(english) """