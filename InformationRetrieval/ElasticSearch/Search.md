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
      
## Term Level Search

A term-level search is a structured search where the queries return results for exact matches. They search for structured data such as dates, numbers, and ranges. With this type of search, you don't care about how well the results match (like how well the documents correspond to the query) but that it returns the data (or not) if the query is matched.

A term-level search produces a "Yes" or "No" binary result similar to the database’s WHERE clause. The basic idea is that the results are binary: the query results are fetched if the condition is met; otherwise, nothing is returned.

Although the documents have a score associated with them, the scores really don't matter. The documents are returned if they match the query but not with relevancy. In fact, you can run term-level queries with a constant score. They can be cached by the server, thus, gaining a performance benefit should the same query be rerun. A traditional database search is like this kind of search.
