# Indexing Documents in Bulk

## Bulk API Syntax
The _bulk API consists of a specific syntax with a POST method invoking the API call.

The following is a sample query that indexes two movies into a new index called movies:

    POST _bulk
    {"index":{"_index":"movies","_id":"1"}}
    {"title": "Top Gun Maverick","actors": "Tom Cruise"}
    {"index":{"_index":"movies","_id":"2"}}
    {"title": "Mission Impossible","actors": "Tom Cruise"}
    
The request body consists of two lines for every document that needs to be stored:

- The first line indicates the action and the metadata. In this case we are indexing a document (hence "index") with ID 1 into an index called movies. We can also perform other actions, such as create, update, and delete.
- The second line is the document itself—NDJSON (short for "new line delimited JSON") representation of the data. The document is formatted in JSON and added in the new line to the request.

Both metadata and source lines are delimited with new line (\n) separators expressed in JSON (hence, newline-delimited JSON).

## Bulk Indexing Documents with No Identifiers

It is entirely up to the user to decide whether a document should have an ID or not. Following query demonstrates indexing a bunch of documents using the _bulk API, without IDs

    POST classics/_bulk
    {"index":{}} 
    {"title": "Mission Impossible","release_date": "1996-07-05"}
    {"index":{}} 
    {"title": "Mission Impossible II","release_date": "2000-05-24"}
    {"index":{}} 
    {"title": "Mission Impossible III","release_date": "2006-05-03"}
    {"index":{}} 
    {"title": "Mission Impossible - Ghost Protocol","release_date": "2011-12-26"}
    
In addition to using the POST action, we've also removed the "_index" field from the first lines; hence, you see the first line to be rather empty: {"index":{}}. Instead, the URL (POST classics/_bulk) declares the index (classics) name. The request has an index name (classics) mentioned in the URL rather than from the first line. No ID is provided for the document.

In addition to the "index" action, the _bulk API helps us with a few more options: create, delete, and update actions.

## Create Action
The create action allows an additional check when indexing the document; that is, the action doesn't replace an existing document. If we try to execute the same query again, it will not succeed. We get a "version conflict, document already exists" error because overwriting the documents is not permissible with the create method.

    POST _bulk
    {"create":{"_index":"tv_shows","_id":"1"}} 
    {"title": "Man vs Bee","actors":"Rowan Atkinson","release_date": "2022-06-24"}
    {"create":{"_index":"tv_shows","_id":"2"}} 
    {"title": "Killing Eve","actors":["Jodie Comer","Sandra Oh"],"release_date": "2018-04-08"}
    {"create":{"_index":"tv_shows","_id":"3"}} 
    {"title": "Peaky Blinders","actors":"Cillian Murphy","release_date": "2013-09-12"}
    
## Update Action
Updating the document follows a similar pattern. The only exception is that we must wrap the fields to update in a doc object.

The following code snippet updates the Man Vs Bee tv show with a streaming_on attribute.

    POST _bulk
    {"update":{"_index":"tv_shows","_id":"1"}} 
    {"doc":{"title": "Man vs Bee","actors":"Rowan Atkinson","release_date": "2022-06-24", "streaming_on":"Netflix"}}
    
## Delete Action
The format is slightly different—we don’t need a second line for this operation.

The following code demonstrates deleting a tv show with ID 1:

    POST _bulk
    {"delete":{"_index":"tv_shows","_id":"1"}}
    
    
## Indexing into Multiple Indices
We can use the bulk API to index (or update or delete) a number of documents into multiples indices.

For example, there a few things that the following code is doing:

- Indexing two new documents into the top_tv_shows index
- Creating a new movie, Dr Strange, in the movies index
- Updating the Killing Eve show with additional field of seasons
- Deleting the Peaky Blinders show (ID=3) from tv_shows index

    POST _bulk
    {"index":{"_index":"top_tv_shows","_id":"1"}} 
    {"title": "Stranger Things","imdb_rating": 8.7}
    {"index":{"_index":"top_tv_shows","_id":"2"}} 
    {"title": "The boys","imdb_rating": 8.7}
    {"create":{"_index":"movies","_id":"4"}} 
    {"title": "Dr Strange in the Multiverse of Madness"}
    {"update":{"_index":"tv_shows","_id":"2"}} 
    {"doc":{"seasons":4}}
    {"delete":{"_index":"tv_shows","_id":"3"}}

## Bulk Loading Documents from a File
Invoke the bulk API and provide the file. The following query loads the document from file:

    curl -H "Content-Type: application/x-ndjson" -XPOST https://da098f7e67414eab942cfa0d625a754e-3232237573-9200-host10nc.environments.katacoda.com/_bulk --data-binary "@bulk_tv_shows.json"
    
The --data-binary flag expects the file name with a @ prefix; for example, like this: "@bulk_tv_shows.json".
