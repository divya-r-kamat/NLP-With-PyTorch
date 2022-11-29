# Search

Elasticsearch supports simple searches as well as advanced searches, such as fuzzy, geo-spatial, shape, and many other queries. There are two variants of search in the world of Elasticsearch: structured search and unstructured search.
- Structured search, supported by term-level search functionality, returns results with no relevance scoring associated.
- Unstructured search, supported by full-level search functionality, returns results with relevance scoring associated.

Elasticsearch provides RESTful APIs to query the data in the form of a search endpoint.  GET/POST is used to invoke this endpoint, passing query parameters along with the request or with a request body. There are two methods for performing a search: The first is called the URI request method, and the latter is Elasticsearch's special domain query language, known as Query DSL. Although both are useful in their own way, Query DSL is powerful and feature-rich.

## URI Requests
One of the easiest way to perform a search on an Elasticsearch engine is by using the URI request method. We invoke the search endpoint by passing the required parameters to the url

    GET movies/_search?q=title:Godfather 
    GET movies/_search?q=title:Godfather Knight Shawshank
    GET movies/_search?q=title:Godfather actors:(Niro OR Pacino) rating:(>=9.0 AND <=9.5)&from=0&size=10&default_operator=AND
    
The _search endpoint is invoked on your index (or multiple indices) with a query in the form of q=<name:value>. Note that the query is appended after the _search endpoint with a question mark (?) delimiter.

## Query DSL
Query DSL is a sophisticated, powerful, and expressive language that helps efficient querying. The syntax and format goes this:

    GET books/_search 
    { 
      "query": { 
        "match": { 
             <<your match criteria>>
        }
      }
    }
    
Invoke the _search endpoint with a query object (represented as JSON), passed in as the body of the request.

## Term Level Search

A term-level search is a structured search where the queries return results for exact matches. They search for structured data such as dates, numbers, and ranges. With this type of search, you don't care about how well the results match (like how well the documents correspond to the query) but that it returns the data (or not) if the query is matched.

A term-level search produces a "Yes" or "No" binary result similar to the database’s WHERE clause. The basic idea is that the results are binary: the query results are fetched if the condition is met; otherwise, nothing is returned.

Although the documents have a score associated with them, the scores really don't matter. The documents are returned if they match the query but not with relevancy. In fact, you can run term-level queries with a constant score. They can be cached by the server, thus, gaining a performance benefit should the same query be rerun. A traditional database search is like this kind of search.

### Term Query
One of the most common types of query in term-level searches is the term query. The term query's job is to fetch documents that exactly match a given field. The field is not analyzed; instead, it is matched against the value that’s stored as-is in the inverted index during indexing.

    GET movies/_search
    {
      "query": {
        "term": {
          "title": "inception"
        }
      }
    }
    
term queries are not analyzed; that is, the query criteria will be matched exactly with the values stored in the inverted indices. The reason for this is that Elasticsearch analyzes text fields during indexing as well as when searching but term-level queries are not analyzed.
We shouldn't run term queries over text fields. If we want to use a term query to search text fields, make sure the text field has data in the form of enumerations or constants, instead of using title, use the title.keyword field. Keyword-typed fields will not be analyzed during indexing. So, when we indexed this movie, the field's value was stored as-is ("The Dark Knight") in the inverted index against the title.keyword

    GET movies/_search
    {
      "query": {
        "term": {
          "title.keyword": "The Dark Knight"
        }
      }
    }
    
### Range Queries
To search through data that falls within a range: book sales during a particular period, movies with ratings in a certain boundary, and so on. You can use a range query for this type of searching.

    GET movies/_search
    {
      "query": {
        "range": {
          "rating": {
            "gte": 9.0,
            "lte": 9.5
          }
        }
      }
    }
    
### IDs Queries
The IDs query fetches matching documents given a set of document IDs. It’s a much simpler way to fetch documents in one go.

    GET movies/_search
    {
      "query": {
        "ids": { 
          "values": [1,3,6,9]
          } 
        }
    }
    
### Exists Queries

Use the exists query to fetch documents for a given field if the field exists. If the respective fields exist in the documents Elasticsearch returns the matched documents else the returned results will be empty.

The following query checks whether the movies index has documents with a field title as well as certificate:

This query searches if the title field exits

    GET movies/_search
    {
      "query": {
        "exists": {
          "field": "title"
        }
      }
    }

This query searches if the certificate field exits

    GET movies/_search
    {
      "query": {
        "exists": {
          "field": "certificate"
        }
      }
    }


Note:
- Elasticsearch returns the top ten results by default. We can modify this number by setting the size parameter on the query. The query in the next listing sets size as 5, returning the top five results in one go.

      GET movies/_search
      {
        "size": 5, 
        "query": {
          "match_all": {}
        }
        
- Elasticsearch also has a from parameter, which helps skipping (offsetting) the results. For example, if from is set to 199, the first 199 documents that resulted from the query are ignored. The results from 200 onward will be returned.
- Elasticsearch has an inbuilt highlighting feature that emphasizes the matched words within the results. We need to add a highlight block at the same level as the query block and indicate the fields where highlighting should be applied.

      GET movies/_search
      {
        "query": {
          "match": {
            "synopsis": "redemption"
          }
        },
        "highlight": {
          "fields": {
            "synopsis": {}
          }
        }
      }
      }
  
### Terms Queries

The terms (note that this term is plural) query searches multiple criteria against a single field. If we have to search for all movies with a set of actors, like brando, pacino, and cann. The terms query expects a list of search words to be queried against a field, passed in as an array to the terms object. The array values will be searched against the existing documents.

    GET movies/_search
    {
      "query": {
        "terms": {
          "actors": [
            "brando",
            "pacino",
            "cann"
          ]
        }
      }
      
### Prefix Queries
If we wish to query for words using a prefix (the beginning of the word), we can use the prefix query.

    GET movies/_search
    {
      "query": {
        "prefix": {
          "title": {
            "value": "god"
          }
        }
      }
    }
    
### Fuzzy Queries


The fuzzy query below searches for a title beginning with "night" as the input value, Elasticsearch employs a Levenshtein distance (or edit distance) algorithm for searching similar terms.

    GET movies/_search
    {
      "query": {
        "fuzzy": {
          "title": "night"
        }
      }
    }
Elasticsearch applies fuzziness=1 (as in the above code), meaning only one letter can be swapped, replaced, deleted, and so on. The fuzziness values are 0, 1, and 2. If we have more than a one letter, say two letters missing, we may need to set the fuzziness to 2.


    GET movies/_search
    {
      "query": {
        "fuzzy": {
          "title": {
            "value":"ight",
            "fuzziness": 2
          }
        }
      }
    }

## Full-Text Queries

Elasticsearch provides the capability to search unstructured data in the form of full-text search queries. A full-text search tries to fetch relevant documents—documents that are pretty close to what the user is searching for!

### Match-All Query

This query fetches all documents available in the index in one go.

    GET movies/_search
    {
      "query": {
        "match_all": { }
      }
    }
    
The same query can be rewritten in a shorter format, like this: GET movies/_search. Behind the scenes, Elasticsearch executes a match_all query.

### Match Query
The match query is a very common query that searches for a set of words in a text field. The query will be text-analyzed by the appropriate analyzer and searched. The results will be associated with the _score value called relevancy scoring. A positive number indicating how close the results are to the user's query. The relevancy algorithm uses Term Frequency (TF), Inverse Document Frequency (IDF), and Field Length Norm to calculate a score.

    GET movies/_search
    {
      "_source": ["title"],  #suppressing all fields except title by setting the required fields in the _source attributes.
      "query": {
        "match": {
          "title": "Godfather"
        }
      }
    }
    
When we provide multiple words in a match query, by default they are queried individually. That is, if search is for "Godfather Knight" in a title field, Elasticsearch searches for all documents consisting of "Godfather" or "Knight" in the title field. However, if intention is to fetch a movie where title has both words "Godfather" and "Knight", the query should have an AND operator.

    GET movies/_search
    {
      "query": {
        "match": {
          "title": {
            "query": "Godfather Knight",
            "operator": "and"
          }
        }
      }
    }
    
### Match with Fuzziness
The query is set with fuzziness as 1, meaning one-letter edits are permissible. Elasticsearch will find one-letter combinations and permutations.

    GET movies/_search
    {
      "query": {
        "match": {
          "title": {
            "query": "Night Club",
            "operator": "and", 
            "fuzziness": 1
          }
        }
      }
      
### Match Phrase Queries

 The match_phrase query, finds documents that match a given phrase exactly. The idea behind the match phrase is to search for a phrase (group of words) in a given field in the same order. For example, if you are looking for the phrase “ability to fight injustice” in the synopsis of a movie, documents are searched with those words in that order.
 
 
     GET movies/_search
    {
      "_source": ["title","synopsis"], 
      "query": {
        "match_phrase": {
          "synopsis": "ability to fight injustice"
        }
      }
    }
    
### Match Phrase Query with Slop

Slop allows a certain number of words to be dropped from the phrase.Adding a slop as 1 fetches the results even though the phrase has a missing word


    GET movies/_search
    {
      "_source": ["title","synopsis"], 
      "query": {
        "match_phrase": {
          "synopsis": {
            "query": "ability fight injustice",
            "slop": 1
          }
        }
        
### Multi-Match Query
The multi_match query searches the criteria across multiple fields. For example, if we want to search for "Rings" across the two fields (title and synopsis)


    GET movies/_search
    {
      "query": {
        "multi_match": {
          "query": "Rings",
          "fields": ["title","synopsis"]
        }
      },
      "highlight": {
        "fields": {
          "title": {},
          "synopsis": {}
        }
      }
    }
    
## Request URL Search

Here we provide query criteria on the query itself, however ,  it is a bit error prone, when the query gets a bit more advanced.

    # Searching for actor Brad Pitt's movies
    GET movies/_search?q=actors:pitt

    # Search for movies with "Godfather" in the title and starred by "Pitt"
    GET movies/_search?q=actors:pitt title:Godfather&default_operator=AND
    
### Query String Queries
The query_string type lets construct a query similar to Kibana Query Language (KQL) using operators such as AND or OR, > (greater than), <= (less than or equal to), * (contains in), and others.

    GET movies/_search
    {
      "query": {
        "query_string": {
          "query": "actors:Freeman AND certificate:R AND genre:Drama"
        }
      }
    }
    
The query_string query expects a query parameter that contains the search criteria. The query is constructed as name-value pairs. The query_string query is strict on syntax, and input errors are not forgiven. The simple_query_string query is a variant of the query_string query with a simple and limited syntax. We can use operators such as +, -, |, *, ~, and so forth for constructing the query.

## Compound Queries
Compound queries involve advanced searches with conditional clauses that satisfy multiple search criteria. They are made of individual leaf queries wrapped in conditional clauses and other constructs.

### Boolean (bool) Query
The Boolean (bool) query combines criteria using Boolean and conditional clauses. It is the most common and flexible compound query you can use to create a set of complex criteria for searching data.

Each conditional clause can be defined with a leaf query made of term-level or full-text queries. These clauses has a typed occurrence of must, must_not, should, or filter clauses.
