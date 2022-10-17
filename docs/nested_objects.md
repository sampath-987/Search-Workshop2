# Nested objects
The nested type is a specialised version of the object data type that allows arrays of objects to be indexed in a way that they can be queried independently of each other
. It flattens object hierarchies into a simple list of field names and values.

Creating a simple index with text, keywords, nested type fields.
```
PUT my-index-nested
{
  "mappings": {
    "properties": {
      "courseId": {
        "type": "keyword"
      },
      "courseName": {
            "type":"text"
          },
      "Subject": {
        "type": "nested",
        "properties": {
          "subjectId": {
            "type": "keyword"
          },
          "subjectName": {
            "type": "text"
          }
        }
      }
    }
  }
}
```
In the above example, Subject is a nested type field and it has two properties, subjectName and subjectId

**Adding data to index**. \
In the following example we are adding a list of objects to the nested type field **Subject**
```
PUT my-index-nested/_doc/1
{
  "courseId": "c001",
  "courseName": "MCA",
  "Subject": [
    {
      "subjectId": "s001",
      "subjectName": "Python"
    },
    {
      "subjectId": "s002",
      "subjectName": "Artificial inteligence"
    }
  ]
}
```

```
PUT my-index-nested/_doc/2
{
  "courseId": "c002",
  "courseName": "Msc-BigData",
  "Subject": [
    {
      "subjectId": "s003",
      "subjectName": "Data mining"
    },
    {
      "subjectId": "s004",
      "subjectName": "Statistics"
    }
  ]
}
```

**Query to nested fields**. \
nested - Query you wish to run on nested objects\
path - Path to the nested object you wish to search
```
GET my-index-nested/_search
{
  "query": {
    "nested": {
      "path": "Subject",
      "query": {
        "match": {
          "Subject.subjectName": "python"
        }
      }
    }
  }
}
```

**Object type vs Nested type** \
Elasticsearch has no concept of inner objects. Therefore, it flattens object hierarchies into a simple list of field 
names and values. For example,
```
PUT my-object-index/_doc/1
{
  "group" : "fans",
  "user" : [ 
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}
```
The above user field is dynamically added as a field of type object. \
The previous document would be transformed internally into a document that looks more like this:
```
{
  "group" :        "fans",
  "user.first" : [ "alice", "john" ],
  "user.last" :  [ "smith", "white" ]
}
```

The user.first and user.last fields are flattened into multi-value fields, and the association between alice and white is lost. This document would incorrectly match a query for alice AND smith:

```
GET my-object-index/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "user.first": "Alice" }},
        { "match": { "user.last":  "Smith" }}
      ]
    }
  }
}
```

If you need to index arrays of objects and to maintain the independence of each object in the array, use the nested data type instead of the object data type.
Internally, nested objects index each object in the array as a separate hidden document, meaning that each nested object can be queried independently of the others with the nested query.
One more example for nested type:
```
PUT nested-object-index
{
  "mappings": {
    "properties": {
      "user": {
        "type": "nested" 
      }
    }
  }
}
```
```
PUT nested-object-index/_doc/1
{
  "group" : "fans",
  "user" : [
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}
```
```
GET nested-object-index/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "Smith" }} 
          ]
        }
      }
    }
  }
}
```
For the above query, we won't get any results since none of the user object have first value as 
_Alice_ and last as _Smith_
```
GET nested-object-index/_search
{
  "query": {
    "nested": {
      "path": "user",
      "query": {
        "bool": {
          "must": [
            { "match": { "user.first": "Alice" }},
            { "match": { "user.last":  "White" }} 
          ]
        }
      },
      "inner_hits": { 
        "highlight": {
          "fields": {
            "user.first": {}
          }
        }
      }
    }
  }
}
```
For the above query you will get matched document, since there is an user object in which 
value of first is _Alice_ and value of last is _White_