# Updating and Upserting Documents


## Updating Documents
Elasticsearch provides two types of update queries: one for working on single documents and another for working on multiple documents:

- _update API will update a single document
- _update_by_query will modify multiple documents all at once

If we want to update with two additional fields: actors and director. We wrap the object consisting of these fields in a doc object and feed it via the update request, as the following code demonstrates:

    POST movies/_update/101
    {
      "doc": {
        "actors":["Marlon Brando","Al Pacino","James Cann"],
        "director":"Frances Ford Coppola"  
      }
    }
    
 If we need to change an existing field, we would follow the same process as above, but provide the new field value in a doc object.
 
    POST movies/_update/101
    {
      "doc": {
        "title":"Marlon Brando as The Godfather"
      }
    }
    
  ## Updating Documents Using Scripts
  
  If we wish to update a set of documents based on conditions and the conditions are set via scripts. Updates are wrapped in a script object as a request using the same _update endpoint. The script object will have source as the key with the updates as a value to this key. The values are set using a context variable declared as ctx. We use the ctx variable to fetch the original document’s attributes by calling ctx._source.<field_name>.
  
    POST movies/_update/101
    {
      "script": {
        "source": "ctx._source.title='The Godfather'"
      }
    }
    
The following code snippet adds a new field, imdb_user_rating, to the original document:

    POST movies/_update/101
    {
      "script": {
        "source": "ctx._source.imdb_user_rating = 9.2"
      }
    }
    
Removing a field - The code snippet shown here demonstrates how you can remove a field (imdb_user_rating) by invoking the remove.ctx._source function.

    POST movies/_update/101
    {
      "script": {
        "source": "ctx._source.remove('imdb_user_rating')"
      }
    }
    
Add multiple fields all at once by writing a script. The notable difference is that the source wraps the individual fields between triple quotes. 

    POST movies/_update/101
    {
      "script": {
        "source": """
        ctx._source.runtime_in_minutes = 175;
        ctx._source.boxoffice_gross_in_millions = 134.8;
        """
      }
    }
    
 Conditional Updates - If we want to flag a movie as a blockbuster when the gross earnings are above a certain threshold.
 
    POST movies/_update/101
    {
     "script": {
       "source": """
          if(ctx._source.boxoffice_gross_in_millions > 125) 
            {ctx._source.blockbuster = true}
          else 
            {ctx._source.blockbuster = false}
        """
      }
    }
    
## Upserts
An upsert (short for update and insert) will update a document if it exists or indexes a new document if it does not exist.

The following query shows upsert in action. It has two parts: a script and an upsert block. The script part is where you update the field of an existing document, while the upsert block consists of the new movie document information.

    POST movies/_update/201
    {
      "script": {
        "source": "ctx._source.boxoffice_gross_in_millions = 357.1"
      },
      "upsert": {
        "title":"The Shawshank Redemption",
        "boxoffice_gross_in_millions":100.0
      }
    }
