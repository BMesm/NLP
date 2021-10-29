import re
from emoji_translate.emoji_translate import Translator
import emoji
from nltk.corpus import stopwords
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer


def text_processing(tweet):
    
    #Generating the list of words in the tweet (hastags and other punctuations removed)
    def form_sentence(tweet):
        tweet_blob = TextBlob(tweet)
        return ' '.join(tweet_blob.words)
    
    #Removing stopwords and words with unusual symbols
    def clean_tweet(tweet):
        emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', ':-(': 'sad', ':-<': 'sad',
              ':P': 'raspberry', ':O': 'surprised', ':D': 'smile', 'XD': 'laughing',
              ':-@': 'shocked', ':@': 'shocked', ':-$': 'confused', ':\\': 'annoyed', ':#': 'mute', ':X': 'mute',
              ':^)': 'smile', ':-&': 'confused',
              '$_$': 'greedy', '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
              '<(-_-)>': 'robot', 'd[-_-]b': 'dj',
              ":'-)": 'sad smile', ';)': 'wink', ';-)': 'wink', 'O:-)': 'angel', 'O*-)': 'angel', '(:-D': 'gossip',
              '=^.^=': 'cat'}
        
        tweet_list = [ele for ele in tweet.split() if ele != 'user']
        clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
        clean_s = ' '.join(clean_tokens)
        clean_mess = [word for word in clean_s.split() if word.lower() not in stopwords.words('english')]
        return clean_mess
    
    
    #Normalizing the words in tweets 
    def normalization(tweet_list):
        lem = WordNetLemmatizer()
        normalized_tweet = []
        for word in tweet_list:
            normalized_text = lem.lemmatize(word,'v')
            normalized_tweet.append(normalized_text)
        return normalized_tweet

    new_tweet = form_sentence(tweet)
    no_punc_tweet = clean_tweet(new_tweet)
    return normalization(no_punc_tweet)