# NLP Preprocessing 

- Text preprocessing
- Data Augmentation
- NLP Albumentation
- Padding

## Data Augmentation

Data augmentation techniques are used to generate additional, synthetic data using the data you have. Augmentation methods are super popular in computer vision applications but they are just as powerful for NLP. 

  - Back translation : translate the text data to some language and then translate it back to the original language. This can help to generate textual data with different words while preserving the context of the text data. 
  - Synonym Replacement : Randomly choose n words from the sentence that are not stop words. Replace each of these words with one of its synonyms chosen at random. 
  - Random Insertion : Find a random synonym of a random word in the sentence that is not a stop word. Insert that synonym into a random position in the sentence. Do this n times. 
  - Random Swap : Randomly choose two words in the sentence and swap their positions. Do this n times. 
  - Random Deletion : Randomly remove each word in the sentence with probability p. 

#### Things to keep in mind while doing NLP data augmentation:

The main issue faced when training on augmented data is that algorithms, when done incorrectly, is that you heavily overfit the augmented training data.

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
