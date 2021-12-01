import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
import codecs
import arabic_reshaper #pip install arabic_reshaper
from bidi.algorithm import get_display #pip install python-bidi

os.chdir(sys.path[0])

#read text
f = open('out_fr_actu.txt' , mode='r', encoding='utf-8')
text = arabic_reshaper.reshape(f.read())
text = get_display(text)

#page = wikipedia.page("Natural Languge Processing")
stopwords = STOPWORDS
stopwords.update(['de','le','et','à','la','des','les','l','d','في', 'الجامعة','الأول','oujda','président','région','cette','afin','université','mohammed','premier','comme','monsieur','savoir','maroc','ump']) #éliminer les mots
clean_text = str([word for word in text.split() if word not in stopwords])


wc = WordCloud(
        font_path='Fonts/DUBAI-REGULAR.TTF', #le nom du font arabe
        background_color='white',
        stopwords=stopwords,
        height = 600,
        width=400,
        #min_font_size=14,
)

wc.generate(text)

#store to file
wc.to_file('wordcloud_output.png')
