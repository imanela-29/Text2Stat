# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk
import re
import pyaramorph
from nltk.corpus import stopwords
import spacy



class Arabycia:
    

	def __init__(self):
		self.analyzer = pyaramorph.Analyzer()
		self.stemmer = nltk.ISRIStemmer()
		self.lemmatizer = nltk.WordNetLemmatizer()
		self.segmenter = nltk.data.load("tokenizers/punkt/english.pickle")
    
	def tokenization(self, txt):
		"""
			tokenization a certain arabic text
			:param txt: string : arabic text
			:return: tokens : array : array contain Tokens
		"""
		tokens = nltk.word_tokenize(txt)
		return tokens

	def stemming(self, txt):
		"""
			Apply Arabic Stemming without a root dictionary, using nltk's ISRIStemmer.
			:param txt: string : arabic text
			:return: stems : array : array contains a stem for each word in the text
		"""
		stems = [self.stemmer.stem(w) for w in self.tokenization(txt)]
		return stems

	def lemmatization(self, txt):
		"""
			Lemmatize using WordNet's morphy function.
			Returns the input word unchanged if it cannot be found in WordNet.
			:param txt: string : arabic text
			:return: lemmas : array : array contains a Lemma for each word in the text.
		"""
		lemmas = str([self.lemmatizer.lemmatize(w) for w in self.tokenization(txt)])
		return lemmas

	def set_raw_text(self, text):
		self.raw_text = text

	def segmentation(self, txt):
		"""
			Apply NLTK Sentence segmentation.
			:param txt: string : arabic text
			:return: sents : array : array contains Sentences.
		"""
		sents = self.segmenter.tokenize(txt)
		return sents

	@staticmethod
	def transliteration(str):
		"""
			Buckwalter Word transliteration.
			:param str: string : arabic word
			:return: trans : string : Word transliteration.
		"""
		trans = pyaramorph.buckwalter.uni2buck(str)
		return trans

	@staticmethod
	def reverse_transliteration(str):
		"""
			convert Word transliteration to the original word.
			:param str: string : Word transliteration.
			:return: trans : string : original word
		"""
		trans = pyaramorph.buckwalter.buck2uni(str)
		return trans

	def stem(self, word):
		"""
			Get word stem (NLTK ISRIStemmer)
			:param word: string : Word.
			:return: stem : string : stem
		"""
		stem = str(self.stemmer.stem(word))
		return stem

	def analyze_text(self):
		"""
			apply some analysis to a text ('raw_data') using pyaramorph lib
			:return: sents : array : the analysis data
		"""
		if len(self.raw_text):
			self.full_analyzed_data = self.analyzer.analyze_text(self.raw_text)
			return self.full_analyzed_data

	def text_search(self, key):
		"""
			Search for word that have the same root as 'key' (Text Search)
			:param key: string : Search keyword.
			:return: result: array : original words from the text with the same root.
		"""
		result = []
		text = self.raw_text.split()

		for word in text:
			if key == self.stem(word):
				result.append(word)

		return list(set(result))

#     def find_index(self, word):
# 		text = self.raw_text.split()
# 		return text.index(word)
       
	def search(self, text, key):
		return [sent for sent in text if re.search(key, sent)]

	def get_subsentences(self, sents, key):
		subsentences = []
		for sent in sents:
			words = sent.split()
			for i in range(0, len(words)):
				if key in words[i] and i >= 0 and i < len(words) - 1:
					subsentences.append(words[i + 1])
		return subsentences
    
 
	def split(self, str, returnval="pos"):
		str = str.split('/')
		if returnval =="pos": return str[1]
		else: return str[0]
        
        

	def prob(self, word1, word2):
		"""
			compute the probability of the given two words.
			prob = count(w1 | w2) / count(w1)
			:param w1:
			:param w2:
			:return:
		"""
		w1 = self.split(word1, "pos")
		w2 = self.split(word2, "pos")
		count_word2 = len(self.search(self.corpus, self.split(word2, "word")))
		filter = self.search(self.corpus, w1)
		count_w1 = self.get_subsentences(filter, w1)
		count_w1_w2 = self.search(count_w1, w2)


		prob = len(count_w1_w2) / float(len(count_w1))
		if w1 == w2: prob /= 2

		return prob, count_word2

	def print_result(self):
		"""
			Reformat the output & print it.
			:return:
		"""
		print('Sentence :')
		print(self.raw_text)
		print('With Diacritics :')
		print(self.diacritized_text)
		print('POS :')
		print(self.diacritized_text_pos)

		for result in self.analyzed_text_result:
			word  = '\nWord  : \t' + '\t'.join(filter(None, result['word']))
			root  = '\nRoot  : \t' + self.stemming(result['word'][0])[0]
			gloss = '\nGloss : \t' + result['gloss'][1]
			pos   = '\nPOS   : \t' + '\t'.join(filter(None, result['pos']))
			print(word, root, pos, gloss)

		return self.analyzed_text_result
def remove_stopwords(words): 
        """Remove stop words from list of tokenized words""" 
        new_words = [] 
        stopword = stopwords.words('arabic') + stopwords.words('french')
        for word in words: 
            if word not in stopword : 
               new_words.append(word) 
        return new_words
    
def remove_non_ascii(words): 
    """Remove non-ASCII characters from list of tokenized words""" 
    new_words = [] 
    for word in words: 
        new_word = words.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') 
        new_words.append(new_word) 
    return new_words 

def to_lowercase(words): 
    """Convert all characters to lowercase from list of tokenized words""" 
    new_words = [] 
    for word in words: 
        new_word = word.lower() 
        new_words.append(new_word) 
    return new_words 

def remove_punctuation(words): 
    """Remove punctuation from list of tokenized words""" 
    new_words = [] 
    for word in words: 
        new_word = re.sub(r'[^\w\s]', '', word) 
        new_word = re.sub(r'[0-9]+', '',new_word)
        new_word=new_word.replace(" ","")
        if new_word!='':
            new_words.append(new_word)
    return new_words 


# Cleaning the text
# processed_article = lines.lower()
# processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
# processed_article = re.sub(r'\s+', ' ', processed_article)

# punctuation='''!()-[]{};:'"\,<>./?&@#$%^*_~'''
#if new_words in punctuation:
#            new_words=new_words.replace(new_words,"")
# Preparing the dataset
# all_sentences = nltk.sent_tokenize(processed_article)

# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# # Removing Stop Words
# from nltk.corpus import stopwords
# for i in range(len(all_words)):
#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]
      






