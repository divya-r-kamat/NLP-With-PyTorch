# NLP Preprocessing 

- Text preprocessing
- Data Augmentation
- NLP Albumentation
- Padding

## Text Preprocessing
The key step in any AI or ML usecases is to clean and preprocess the data:

1. Normalization - One of the key steps in processing language data is to remove noise so that the machine can more easily detect the patterns in the data. Text data contains a lot of noise, this takes the form of special characters such as hashtags, punctuation and numbers. All of which are difficult for computers to understand if they are present in the data. We need to, therefore, process the data to remove these elements.
2. Stopwords - Stop words are commonly occurring words that for some computational processes provide little information or in some cases introduce unnecessary noise and therefore need to be removed. However, there could be instances where the removal of stop words is either not advised or needs to be more carefully considered. 
3. Stemming or Lemmatization - They aim to reduce words to their root form
4. Part of Speech (POS) tagging and chunking - Part of speech (POS) tagging is a method to categorise words which gives some information relating to the way in which that word is used in speech. Chunking builds on POS tagging in that it uses the information from the POS tags to extract meaningful phrases from text.
5. Remove HTML Tags - If the reviews or texts are web scraped, chances are they will contain some HTML tags. Since these tags are not useful for our NLP tasks, it is better to remove them.
 
        def strip_html_tags(text):
          """remove html tags from text"""
          soup = BeautifulSoup(text, "html.parser")
          stripped_text = soup.get_text(separator=" ")
          return stripped_text
        
6. Convert Accented Characters 

        def remove_accented_chars(text):
          """remove accented characters from text, e.g. café"""
          text = unidecode.unidecode(text)
          return text
    
 7. Expand Contractions - Contractions are shortened words, e.g., don’t and can’t. Expanding such words to “do not” and “can not” helps to standardize text. We use the contractions module to expand the contractions.

         def expand_contractions(text):
            """expand shortened words, e.g. don't to do not"""
            text = contractions.fix(text)
            return text


below are few packages which could be handy while clean text data
- [clean-text](https://pypi.org/project/clean-text/)
- [texthero](https://pypi.org/project/texthero/)
- [scrubadub](https://pypi.org/project/scrubadub/)

## Data Augmentation

Data augmentation techniques are used to generate additional, synthetic data using the data you have. Augmentation methods are super popular in computer vision applications but they are just as powerful for NLP. 

  - Back translation : translate the text data to some language and then translate it back to the original language. This can help to generate textual data with different words while preserving the context of the text data. 
  - Synonym Replacement : Randomly choose n words from the sentence that are not stop words. Replace each of these words with one of its synonyms chosen at random. 
  - Random Insertion : Find a random synonym of a random word in the sentence that is not a stop word. Insert that synonym into a random position in the sentence. Do this n times. 
  - Random Swap : Randomly choose two words in the sentence and swap their positions. Do this n times. 
  - Random Deletion : Randomly remove each word in the sentence with probability p. 

#### Things to keep in mind while doing NLP data augmentation:

The main issue faced when training on augmented data is that, when done incorrectly, you heavily overfit the augmented training data.

Some things to keep in mind:
  - Do not validate using the augmented data.
  - If you’re doing K-fold cross-validation, always keep the original sample and augmented sample in the same fold to avoid overfitting.
  - Always try different augmentation approaches and check which works better.
  - A mix of different augmentation methods is also appreciated but don’t overdo it.
  - Experiment to determine the optimal number of samples to be augmented to get the best results.
  - Keep in mind that data augmentation in NLP does not always help to improve model performance.

## Reference

- https://github.com/jasonwei20/eda_nlp
- https://neptune.ai/blog/data-augmentation-nlp
- https://www.kaggle.com/shonenkov/nlp-albumentations
- https://nlpforhackers.io/
- https://gist.github.com/jiahao87/d57a2535c2ed7315390920ea9296d79f
