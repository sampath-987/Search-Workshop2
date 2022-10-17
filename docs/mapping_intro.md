# Elasticsearch Schema/Mapping

## What is an ES Mapping?
Within a search engine, mapping defines how a document is indexed and how it indexes and stores 
its fields. We can compare mapping to a database schema in how it describes the fields and 
properties that documents hold, the datatype of each field (e.g., string, integer, or date), and 
how those fields should be indexed and stored by Lucene. It is very important to define the 
mapping after we create an index—an inappropriate preliminary definition and mapping may result 
in the wrong search results.


## About Mapping
Mapping is intended to define the structure and field types as required based on the answers to 
certain questions. For example:

- Which string fields should be full text and which should be numbers or dates 
  (and in which formats)?
- When should you use the _all field, which concatenates multiple fields to a single string and 
  helps with analyzing and indexing?
- What custom rules should be set to update new field types automatically as they are added 
  (e.g., the dynamic mapping type, which we will discuss further later on)?

### Dynamic mapping
One of the most important features of Elasticsearch is that it tries to get out of your way and 
lets you start exploring your data as quickly as possible. To index a document, you don’t have to 
first create an index, define a mapping type, and define your fields — you can just index a 
document and the index, type, and fields will display automatically:

### Explicit mapping
while dynamic mapping can be useful to get started, at some point you will want to specify your 
own explicit mappings.

### Field Data Types
Each field has a field data type, or field type. This type indicates the kind of data the field 
contains, such as strings or boolean values, and its intended use. For example, you can index 
strings to both text and keyword fields. However, text field values are analyzed for full-text 
search while keyword strings are left as-is for filtering and sorting.
- For more about field types please refer - 
  https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html#mapping-types

### Mapping parameters
There are certain mapping parameters that is used as configuration for each field.
- Please go through the mapping parameters that are mentioned here - 
  https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-params.html
  

### Mapping commands
Please find the mapping commands [here](mapping_cmd.md)



