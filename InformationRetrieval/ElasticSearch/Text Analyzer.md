# Text Analyzer

Elasticsearch does a lot of work behind the scenes on incoming textual data. It preps data so that it can be efficiently stored and searchable. It cleans the text fields, breaks the text data into individual tokens, and enriches the tokens before storing them in the inverted indices. When a search query is carried out, the query string is searched against the stored tokens and, accordingly, any matches are retrieved and scored. This process is known as text analysis and is usually expected to be performed on all text fields.


The analyzer is a software module essentially tasked with two functions—tokenization and normalization—so the text fields are thoroughly analyzed and stored in inverted indexes for advanced query matching. Analyzer performs actions on any incoming text.
- Tokenization is the process of splitting sentences into individual words, and it follows certain rules. For example, you can instruct the process to break sentences by a delimiter such as whitespace, a letter, a pattern, or other criteria. This process is carried out by a component called a "tokenizer,"" whose sole job is to chop sentences into individual words, called "tokens" by following certain rules when breaking the sentence into words.
- Normalization, on the other hand, is where the tokens (words) are massaged, transformed, modified, and enriched in the form of stemming, synonyms, stop words, and other features.
- Stemming is an operation where words are reduced (stemmed) to their root words (for example, “author” is the root word for “authors”, “authoring”, and “authored”).
- In addition to stemming, normalization also finds appropriate synonyms before adding them to the inverted index. For example, “author” may have additional synonyms, such as “wordsmith”, “novelist”, “writer”, and so on.

## Analyzer 
An analyzer module consists of essentially three software components:
- Character filters (optional): These filters are applied at the character level, and they remove unwanted characters from text strings. For example, purging HTML tags like <h1>, <href>, <src> from the input text.
- Tokenizers (mandatory): The tokenizers split sentences into words by using a delimiter, such as whitespace, punctuation, or some form of word boundaries.
- Token filters (optional): The token filters further process the tokens produced by the tokenizers. For example, the token can change case, create synonyms, provide the root word (stemming), or produce n-grams and shingles, and so on.
Of all these components, only tokenizers are mandatory.
- Elasticsearch exposes an endpoint called _analyze to test the text analysis process. 
- Elasticsearch provides over half a dozen out-of-the-box analyzers that we can use in the text analysis phase. These analyzers will most likely suffice for basic cases, but we can create a custom one if needed by instantiating a new analyzer module with the required components.
- Elasticsearch uses a "standard analyzer" for analyzing the text. There are a handful of such analyzers that work on text in multiple ways.
- We can also enable English stop words on the standard analyzer by adding a filter during index creation. 
- Other analyzers are 
  -  Simple Analyzer - tokenizes sentences at the occurrence of a non-letter: like a number, space, apostrophe, or hyphen.
  -  Keyword Analyzer - stores the text without any modifications or tokenization. That means the analyzer does not tokenize the text, nor does it apply filters or tokenizers. Instead, it is stored as a string representing a keyword data type 
  -  Whitespace Analyzer - splits the text into tokens when it encounters whitespaces
  -  Language Analyzer

