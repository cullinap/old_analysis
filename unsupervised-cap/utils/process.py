import pandas as pd
import gensim
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import bigrams

STEMMER = SnowballStemmer("english", ignore_stopwords=True)

def preprocess(text: pd.Series, bigrams=False, stem=False):
    text = text.apply(gensim.utils.simple_preprocess, min_len=3)
    sw = set(stopwords.words('english'))
    
    text = text.apply(lambda s: [w for w in s if w not in sw])
    text = text.apply(lambda s: [STEMMER.stem(w) for w in s if stem != False])
    text = text.apply(lambda s: ['_'.join(x) for x in nltk.bigrams(s) if bigrams != False] + s)

    return text