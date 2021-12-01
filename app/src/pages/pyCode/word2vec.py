import spacy
import re
import nltk

# Load the spacy model that you have installed
nlp = spacy.load('en_core_web_sm')
# process a sentence using the model
file = open("ar_actu.txt","r",encoding="utf-8") 
text = file.read(386000000)
 
doc=nlp(text)
# It's that simple - all of the vectors and words are assigned after this point
# Get the vector for 'text':
for token in doc:
    print(token)
    print(token.vector)

# Get the mean vector for the entire sentence (useful for sentence classification etc.)
print(doc.vector)