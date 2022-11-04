# ElasticSearch

## Documents
- In Elasticsearch, data is represented in JSON (JavaScript Object Notation) format—a simple text format that creates a visual representation of data in name-value pairs. We'll call a valid JSON file carrying some data a "document." 

For example, the following is a JSON document representing a student:

    {
        "name":"John Smith",
        "age":23,
        "address":{
            "house_number":28,
            "street_name":"Nevermind Street",
            "country":"Neverland"
        }
        "phone_numbers:{
            "home":"1234567890,
            "mobile":"1234567890
        }
    }

- These documents sit in a logical bucket called an "index." The index is a collection of similar types of documents, like students, cars, books, and so on.
- Persisting the documents into these indexes is known as "indexing." It means storing or persisting the records (aka documents) into Elasticsearch.


## Document Identifiers

Every document must have identifiers; some can be randomly generated by the system, while others can be assigned specifically by us. For example, the document for the student John Smith can be given an identifier (say, id = 1), and the student Grace Smith can be given another identifier (id = 2).

We use the single document index API to index the document using HTTP’s PUT or POST actions. The syntax for this method is as follows:

    PUT <index_name>/_doc/<identifier>
    
The <index_name> is the name of the index where the document lives, and _doc is the endpoint that must be present when indexing a document. The <identifier> is the document’s identity, which is a mandatory path parameter if using the HTTP PUT method. If we use the POST action, an identifier will be generated by the system automatically.
  
## Communicating with Elasticsearch
  
We can use any client that supports RESTful APIs—for example, cURL, Postman, or even native clients written in programming languages such as Java, C#, Python, and so on.

There's also a UI tool called Kibana that talks to Elasticsearch seamlessly. Kibana is a web application with a rich user interface that works with the search engine, and it helps write search and aggregation queries in a rich text editor. 

To index documents using Kibana, we invoke an endpoint and attach a payload to it. The syntax looks like this:

      PUT <your_index>/_doc/<your_document_id>
      {
        "name":"provide-name",
        "age":"provide-age-of-the-student",
        "location": "provide-location"
      }

## Indexing a Document Using cURL
    
The following is a sample student document representing our first student, John Smith. Executing the following command cURL script will index the document:

        curl -XPUT --header 'Content-Type: application/json' https://4b034f0fdb6a461f817c8803c352b0e6-2887150597-9200-host08nc.environments.katacoda.com/students/_doc/1 -d '{
            "name":"John Smith",
            "age":23
        }'|json_pp
    
- -XPUT is a HTTP PUT instruction to the server.
- Content-Type sets the document's format as JSON.
- The URL preceding students/_doc/1 is the Elasticsearch server's address.
    
Following is the response:
    
        {
           "_id" : "1",
           "_index" : "students",
           "_primary_term" : 1,
           "_seq_no" : 0,
           "_shards" : {
              "failed" : 0,
              "successful" : 1,
              "total" : 2
           },
           "_version" : 1,
           "result" : "created"
        }
    
- The result attribute indicates the operation’s action: created indicates that the document was successfully indexed as a new document into Elasticsearch’s store.
- The _index, _type, and _id attributes are derived from our incoming request and assigned to the document.
- The _version indicates the current version of this document; the value 1 here means the first version for the document. The number is incremented if we modify the document and reindex it. Every time we execute the query the version gets updated.

    
## Reference
- https://learning.oreilly.com/scenarios/elasticsearch-indexing-documents/9781098133931/