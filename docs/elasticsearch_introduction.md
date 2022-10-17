# Introduction To ElasticSearch

## What is ElasticSearch?

Elastic search in its core is a document-oriented search engine. It is a document based database 
that lets you INSERT, DELETE , RETRIEVE and even perform analytics on the saved records like a 
general pupose database. But unlike databases, Elastic Search is designed specifically for SEARCHING.

Elastic search is essentially a search engine and offers an arsenal of features you can use to
retrieve the data stored in it, as per your search criteria. And that too, at lightning speeds. 
Yes. It’s extremely fast.

## How is ElasticSearch so fast?

let’s consider the index of a book as an analogy.
To search for a word or a term we go to the index of the book, which is a list of key terms in the 
book, along with the page numbers where the word can be found. This is exactly how Elastic Search works.

Elastic Search is built on top of Apache Lucene, a high-performance, full-featured text search 
engine library written in Java. The underlying data structure used in Lucene is called an Inverted Index.

## Basic Difference Between ElasticSearch and RDBMS

- ElasticSearch is a No sql Database.
- It has no relations, no constraints, no joins, no transactional behaviour.
- It is easier to scale when compared to RDBMS.

### Terminology
|         ElasticSearch         |          RDBMS           |
|:-----------------------------:|:------------------------:|
|             Node              |       DB Instance        |
|            Cluster            |        DB Cluster        |
|             Index             |         Database         |
|             Type              |          Table           |
|            Mapping            |          Schema          |
|             Shard             |    Physical Partition    |
|           Document            |           Row            |
|             Field             |          Column          |
| Elasticsearch DSL (Query DSL) |           SQL            |

## What is ElasticSearch used for?
The speed and scalability of Elasticsearch and its ability to index many types of content mean that
it can be used for a number of use cases:
- Application search
- Website search
- Enterprise search
- Logging and log analytics
- Infrastructure metrics and container monitoring
- Application performance monitoring
- Geospatial data analysis and visualization
- Security analytics
- Business analytics