from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def bag_of_words():
	return CountVectorizer(analyzer = "word",   
                           tokenizer = None,    
                           preprocessor = None, 
                           stop_words = None,   
                           max_features = 5000
                        )

def tfidf(max_df,min_df):
	return TfidfVectorizer(max_df=max_df, 
                           min_df=min_df, 
                           lowercase=True, 
                           use_idf=True,
                           norm=u'l2', 
                           smooth_idf=True 
                         )