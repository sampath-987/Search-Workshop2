# Interaction with Elasticsearch Cluster API 
Our containers for ElasticSearch and Kibana are up and running, so we will be doing the following 
things:
- Health check ElasticSearch.
- Create an Index.
- Perform insertion, retrieval and deletion.

## Before we start
Let's load up the Kibana Console UI in our browser.
- Kibana is running locally on our machine at the port 5601, click the url 
  <b> http://0.0.0.0:5601/app/kibana#/ </b> to open Kibana in our browser
- Click on the Hamburger Menu > Dev Tools to go to the Kibana Console, where we can write our 
  queries to perform operations.

## Health Check
Cluster Health API returns a simple status of the cluster.
#### Kibana Console
```
GET /_cluster/health
```
## Create An Index
We are going to create a simple index for customers which will store the name of the customer.
#### Kibana Console
```
PUT /customer?pretty
{
    "settings" : {
        "number_of_shards" : 2,
        "number_of_replicas" : 0
    },
    "mappings" : {
        "properties" : {
            "name" : { "type" : "text" }
        }
    }
}
```
## Index A Document﻿
Now, let's add a record to the above created index.
#### Kibana Console
```
PUT customer/_doc/1
{
  "name": "Mathew Stuart"
}
```

## Get the document from the Index
To get the record from the index,
#### Kibana Console
```
GET customer/_doc/1
```

## Delete A document
Finally, let's try to delete the entry that we added previously.
#### Kibana Console
```
DELETE customer/_doc/1
```




