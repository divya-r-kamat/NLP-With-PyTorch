# Managing Index

An index is a logical collection of the data backed up by shards (both primary and replicas). Shards (Apache Lucene instances) are the software components that help store data in memory as well as flush to the data store. A newly created index is associated with a set number of shards and replicas, a mapping schema, and aliases. We can create an index to fit the needs and requirements.

- When a document is indexed for the first time, Elasticsearch will create the index for us automatically.
- We can read index details by issuing a GET <index_name> command.
- The index holds mapping definitions, settings, and aliases.
- Elasticsearch provides a convenient way to delete an index as well as it's entire contents in one go, using DELETE <index_name> command
- While deleting an index may be an irreversible operation, closing an index only ensure that an index can't be used. No operations are allowed on a closed index; hence, we cannot access an index, issue search queries or index any more documents into it when it is in a closed state. - POST <index_name>/_close
-  return a closed index to a "live" state by simply opening it. POST <index_name>/_open
-  We can also create indices explicitly with predefined configurations, such as settings, mapping schema, and aliases.
-  We can also predefine the mapping schema when creating an index. Since we know the shape and form of the data that sits in index, we can create a suitable schema with field names and appropriate data types.
-  Aliases are alternate names given to an index. The following code will create an alias called departments for the two indices it_department and hr_department:

        PUT it_department
        {
          "aliases": {
            "departments": {}
          }
        }
        PUT hr_department
        {
          "aliases": {
            "departments": {}
          }
        }
