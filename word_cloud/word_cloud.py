import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
wordslist=[]
wordcloud_size=50
words=""
possible_sizes=[10,20,15,5,30,25]
possible_colours=["blue","green","red","yellow"]
orientation=[1,2,3,4]

class word():
    def __init__(self,colour,size,word,orentation,x,y):
        self.word=colour

def get_words():
    file_name="word_list"
    file=open(file_name,"r")
    global words
    words=file.read()
    global wordslist
    wordslist=words.split("\n")

get_words()
mask=np.array(Image.open("mask1.jpg"))


#convert list to string and generate
word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS, mask=mask).generate(words)
plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
plt.imshow(word_cloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

