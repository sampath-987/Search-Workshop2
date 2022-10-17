# Mapping commands

## Create Dynamic mapping
An example to create a simple index with dynamic mapping:
```
PUT data/_doc/1 
{ "name": "john smith" }
```
- Creates the *data* index, the *_doc* mapping type, and a field called *count* with data 
  type *long*.

### Create Explicit mapping
- Creating the index simple_index
```
PUT /simple_index
{
    "mappings":{
      "properties":{
        "name":{
          "type": "text"
        }
      }
  }
}
```
- Indexing data to simple_index
```
POST simple_index/_doc
{
  "name": "james"
}
```