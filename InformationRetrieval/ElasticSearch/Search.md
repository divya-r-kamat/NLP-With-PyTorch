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

# This query searches if the title field exits
    GET movies/_search
    {
      "query": {
        "exists": {
          "field": "title"
        }
      }
    }

# This query searches if the certificate field exits
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
