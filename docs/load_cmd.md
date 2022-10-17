<h3>Load data to Elastic Search </h3>

You index data into Elasticsearch by sending JSON objects (documents) through the REST APIs.  
Whether you have structured or unstructured text, numerical data, or geospatial data, 
Elasticsearch efficiently stores and indexes it in a way that supports fast searches. 

**Load a Single Document Into ES**\
To add a single document to an index, submit an HTTP post request that targets the index. 


```
POST /customer/_doc/1
{
  "firstname": "Jennifer",
  "lastname": "Walters"
}
```


This request automatically creates the `customer` index if it doesn't exist, 
adds a new document that has an ID of 1, and 
stores and indexes the `firstname` and `lastname` fields.

The new document is available immediately to search. 
You can retrieve it with a GET request that specifies its document ID: `GET /customer/_doc/1`
----
**Load a Single Document Into ES** 

To add multiple documents in one request, use the `_bulk` API.
Bulk data must be newline-delimited JSON (NDJSON). 
Each line must end in a newline character (`\n`), including the last line.

```
PUT customer/_bulk 
{ "create": { } }
{ "firstname": "Monica","lastname":"Rambeau"}
{ "create": { } }
{ "firstname": "Carol","lastname":"Danvers"}
{ "create": { } }
{ "firstname": "Wanda","lastname":"Maximoff"}
{ "create": { } }
{ "firstname": "Jennifer","lastname":"Takeda"}
```
----

**Search**

Indexed documents are available for search in near real-time. 
The following search matches all customers with a first name of _Jennifer_ 
in the `customer` index.

```
GET customer/_search
{
  "query" : {
    "match" : { "firstname": "Jennifer" }  
  }
}
```
----
