import re
import nltk
import string
import random
import googletrans
from googletrans import Translator
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer


def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.
    -----
    Parameters:
        text: text part of the phrase or segments dataset
        
    Returns:
        cleaned text 
    
    '''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


def text_preprocessing(text):
    """
    A wrapper fucntion for Cleaning and parsing the text.
    -----
    Parameters:
        text: text part of the phrase or segments dataset
        
    Returns:
        cleaned and parsed text 

    """
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    nopunc = clean_text(text)
    tokenized_text = tokenizer.tokenize(nopunc)
    #remove_stopwords = [w for w in tokenized_text if w not in stopwords.words('english')]
    combined_text = ' '.join(tokenized_text)
    return combined_text

def get_top_n_words(corpus,ngram_range=(1,1), n=None):
    """
    List the top n words in a vocabulary according to occurrence in a text corpus.
    
    -----
    Parameters:
        corpus: text corpus from the phrase or segments dataset
        ngram_range: type of n gram range - unigram, bigram, trigram etc
            (1,1) default --> unigram
            (2,2)  - bigram
            (3,3) - trigram
        n : the number of top words to be displayed
        
    Returns:
        Top n words, based on the word frequency
    """
    vec = CountVectorizer(ngram_range=ngram_range,stop_words = 'english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]

def random_deletion(words, p=0.5): 
    """
    random deletion deletes words from a sentence. 
    Given a probability parameter p, it will go through the sentence and decide whether to delete a word 
    or not based on that random probability.
    
    -----
    Parameters:
        words : tokenized words in a sentence
        p : probability parameter
        
    Returns:
        returns remaining words after random deletion
    """
    remaining = list(filter(lambda x: random.uniform(0,1) > p,words)) 
    if len(remaining) == 0: # if not left, sample a random word
        return [random.choice(words)] 
    else:
        return remaining
    
def random_swap(sentence, n=5): 
    """
    random swap augmentation takes a sentence and then swaps words within it n times, 
    with each iteration working on the previously swapped sentence. Here we sample two random numbers 
    based on the length of the sentence, and then just keep swapping until we hit n.
    
    -----
    Parameters:
        sentence : input sentence
        n : number of times to swap
        
    Returns:
        returns sentence after random swap
    """
    length = range(len(sentence)) 
    for _ in range(n):
        idx1, idx2 = random.sample(length, 2)
        sentence[idx1], sentence[idx2] = sentence[idx2], sentence[idx1] 
    return sentence


def back_translate(sentence,trans_lang):
    """
    Back translate Involves translating a sentence from our target language into one or more other languages 
    and then translating all of them back to the original language.
    
    -----
    Parameters:
        sentence : input sentence
        trans_lang : target language to translate
        
    Returns:
        returns sentence after back_translate
    """
    translator = Translator()
    translations = translator.translate(sentence, dest=trans_lang)

    translations_en_random = translator.translate(translations.text, src=trans_lang, dest='en') 
    return translations_en_random.text

def synonym_word(word):
    """
    Finds the synonym of a given word from nltk wordnet library 
    
    -----
    Parameters:
        word : input word
        
    Returns:
        returns synonym of a given word
    """
    synonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())
    if len(synonyms) <=0:
        return word
    return random.sample(synonyms, 1)[0]

def synonym_sentence(sentence, prob=0.5):
    """
    Given a probability parameter p, Randomly choose words from the sentence that are not stop words. 
    Replace each of these words with one of its synonyms chosen at random.
    
    -----
    Parameters:
        sentence : input sentence
        p : probability parameter
        
    Returns:
        returns sentence after synonym replacement
    """
    words =  sentence.split()
    synonym_words = []
    for word in words:
        if random.random() < prob:
            synonym_words.append(synonym_word(word))
        else:
            synonym_words.append(word)
    return " ".join(synonym_words)
