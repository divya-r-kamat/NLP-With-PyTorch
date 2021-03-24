Stanford Sentiment Treebank V1.0

# Goal
The goal is to build a sentiment analysis model using  StanfordSentimentAnalysis Dataset.
- Use "Back Translate", "random_swap" and "random_delete" to augment the data you are training on
- Download the StanfordSentimentAnalysis Dataset from this link  (http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip) 
  Use "datasetSentences.txt" and "sentiment_labels.txt" files from the zip you just downloaded as your dataset. This dataset contains just over 10,000 pieces of Stanford data from HTML files of Rotten Tomatoes. The sentiments are rated between 1 and 25, where one is the most negative and 25 is the most positive.

# Dataset 

This is the dataset of the paper:

Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank
Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher Manning, Andrew Ng and Christopher Potts
Conference on Empirical Methods in Natural Language Processing (EMNLP 2013)

This file includes:
1. original_rt_snippets.txt contains 10,605 processed snippets from the original pool of Rotten Tomatoes HTML files. Please note that some snippet may contain multiple sentences.

2. dictionary.txt contains all phrases and their IDs, separated by a vertical line |

3. sentiment_labels.txt contains all phrase ids and the corresponding sentiment labels, separated by a vertical line.
Note that you can recover the 5 classes by mapping the positivity probability using the following cut-offs:
[0, 0.2], (0.2, 0.4], (0.4, 0.6], (0.6, 0.8], (0.8, 1.0]
for very negative, negative, neutral, positive, very positive, respectively.
Please note that phrase ids and sentence ids are not the same.

4. SOStr.txt and STree.txt encode the structure of the parse trees. 
STree encodes the trees in a parent pointer format. Each line corresponds to each sentence in the datasetSentences.txt file. The Matlab code of this paper will show you how to read this format if you are not familiar with it.

5. datasetSentences.txt contains the sentence index, followed by the sentence string separated by a tab. These are the sentences of the train/dev/test sets.

6. datasetSplit.txt contains the sentence index (corresponding to the index in datasetSentences.txt file) followed by the set label separated by a comma:
	1 = train
	2 = test
	3 = dev

Please note that the datasetSentences.txt file has more sentences/lines than the original_rt_snippet.txt. 
Each row in the latter represents a snippet as shown on RT, whereas the former is each sub sentence as determined by the Stanford parser.

For comparing research and training models, please use the provided train/dev/test splits.


# Model Architecture

	classifier(
	  (embedding): Embedding(20896, 300)
	  (encoder): LSTM(300, 100, num_layers=2, batch_first=True, dropout=0.2)
	  (fc): Linear(in_features=100, out_features=3, bias=True)
	)
	The model has 6,510,703 trainable parameters


# Data Augmentation

Augmented the data using
- random swap - The random swap augmentation takes a sentence and then swaps words within it n times, with each iteration working on the previously swapped sentence. 
- random delete - As the name suggests, random deletion deletes words from a sentence. Given a probability parameter p, it will go through the sentence and decide whether to delete a word or not based on that random probability. 
- back translation using google translate - This involves translating a sentence from our target language into one or more other languages and then translating all of them back to the original language.

