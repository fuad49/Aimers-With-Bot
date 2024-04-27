from tkinter import *
import tkinter as tk
import nltk
from newspaper import Article
import NewsGen as Ng
nltk.download('punkt')

tText = ''
def ReturnArticle(url):
    global tText
    article = Article(url)
    Ng.scrape_text(url)

    article.download()
    article.parse()
    article.nlp()
    tText = article.title
    return article.summary

def ReturnTitle():
    return tText