# Retrieving and Deleting Documents

## Overview of the _bulk API Endpoint

Elasticsearch provides a set of document APIs to help manage the data lifecycle. For example:

- PUT myindex/_doc/1 will index a new document
- PUT myindex/_update/1 will modify the existing document
- DELETE myindex/_doc/1 will delete the existing document

These operations are handy when working with small sets of documents. However, they become impractical when we start managing larger collections. For example, let's say we want to prime Elasticsearch with a million inserts, a thousand deletes, and a thousand updates. Although using the document APIs for this purposes is perfectly valid and would work, it isn't advisable due to the size of the data that we're dealing with. This is where the bulk feature comes in handy. Whenever we wish to index, create, remove, or update documents (or any combination of these), we can use the _bulk API.


## Indexing Sample Documents

    POST _bulk
    {"index":{"_index":"books","_id":"1"}}
    {"title": "Core Java Volume I – Fundamentals","author": "Cay S. Horstmann","edition": 11, "synopsis": "Java reference book that offers a detailed explanation of various features of Core Java, including exception handling, interfaces, and lambda expressions. Significant highlights of the book include simple language, conciseness, and detailed examples.","amazon_rating": 4.6,"release_date": "2018-08-27","tags": ["Programming Languages, Java Programming"]}
    {"index":{"_index":"books","_id":"2"}}
    {"title": "Effective Java","author": "Joshua Bloch", "edition": 3,"synopsis": "A must-have book for every Java programmer and Java aspirant, Effective Java makes up for an excellent complementary read with other Java books or learning material. The book offers 78 best practices to follow for making the code better.", "amazon_rating": 4.7, "release_date": "2017-12-27", "tags": ["Object Oriented Software Design"]}
    
POST _bulk makes the bulk API call. The body of the call comprises the lines that make up the documents and the actions that the API is expected to perform. Two lines are comprised for each of the document—the first line indicates the action, index, and ID of the document, while the second line is the document itself.

{"index":{"_index":"books","_id":"1"}} tells the bulk API that we want to "index" the attached document (in the next line) into the "books" index with an ID=1. The second line, {"title": "Core Java .."}, is the actual document.


## Retrieving by ID

Fetching the documents (retrieval) is easy. Elasticsearch provides two types of document APIs for retrieving documents:

- The single-document API that returns one document given an ID, and
- The multi-document API that returns multiple documents given an array of IDs

Elasticsearch exposes an endpoint to fetch a document given the document ID. The URL will be exactly same as the one we've used for indexing, except the HTTP action method is replaced with the GET method, like GET <index_name>/_doc/<id>.

GET is the HTTP method that indicates we are fetching a resource. The URL indicates the resource’s endpoint—in this case, the index_name followed by _doc and the ID of the document.
  
## Fetching Multiple Documents
  
We can also ask Elasticsearch for multiple documents by using the _mget API. The request will have a body with an array consisting of document identifiers. 

    GET books/_mget
    {
      "ids":["1","3","6","9"]
    }
  
 ## Source and Metadata
  
When we look at the JSON responses for the queries, we see two parts in the response:

- Metadata: consisting of _id, _version, and others
- Source data: the original document data under _source object at the bottom of the response
  
     {
      "_index" : "books",
      "_id" : "1",
      "_version" : 1,
      "_seq_no" : 0,
      "_primary_term" : 1,
      "found" : true,
      "_source" : {
        "title" : "Core Java Volume I – Fundamentals",
        "author" : "Cay S. Horstmann",
        "edition" : 11,
        "synopsis" : "Java reference book that offers a detailed explanation of various features of Core Java, including exception handling, interfaces, and lambda expressions. Significant highlights of the book include simple language, conciseness, and detailed examples.",
        "amazon_rating" : 4.6,
        "release_date" : "2018-08-27",
        "tags" : [
          "Programming Languages, Java Programming"
        ]
      }
    }
  
We can, however, omit the source completely if we want to. For example, retrieving a source with hundreds of fields consisting of large values may unnecessarily impact bandwidth. And sometimes we may not want some confidential info to be leaked.

We can set _source to false so the response will not include the original document, as shown in the following query:
  
    GET books/_doc/1?_source=false
  
## Retrieving Source Only
  
If we want to fetch just the source and ignore the metadata, we can swap_doc with the _source endpoint.
  
    GET books/_source/1
