# -*- coding: utf-8 -*-
"""Sentiment_analysis_using_nltk,textblob.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-4-_fEN-87j0CCvnRO0hdYC2Pl_hw02A

Install Dependencies
"""

pip install newspaper3k

#importing modules
from textblob import TextBlob
import nltk
from newspaper import Article

#get the article
print("1.Url")
print("2.Text")
ip=input("Select 1 or 2: ")
ip=int(ip)
if ip==1:
   url=input('Enter the url of the Article to analyse: ')
   article=Article(url)
   #Applying NLP   
   article.download()
   article.parse()
   nltk.download('punkt')
   article.nlp()
   #Get the summary of the article   
   text=article.summary
elif ip==2:
   text=input("Enter the Text: ")
   text=str(text)
else:
   print(error)

print(text)

#create a TextBlob object
obj=TextBlob(text)
 
Sentiment=obj.sentiment.polarity #this give a value btwn -1 and 1
 
print(Sentiment)

if Sentiment==0:
     print('Neutral')
elif Sentiment>0:
     print('Postive')
else:
     print ('Negative')