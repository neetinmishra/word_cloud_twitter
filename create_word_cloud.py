import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
file = open("./data.txt", "r+", encoding="utf-8")
dataset = file.read()
def create_word_cloud(string):
   maskArray = npy.array(Image.open("cloud.png"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("twitterWordCloud.png")
dataset = dataset.lower()
file.close()
create_word_cloud(dataset)