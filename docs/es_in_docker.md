# Using ElasticSearch In Dockers
Just like everything else, ElasticSearch can also be dockerized.

## Content
- Create the docker-compose
- Get the containers for ElasticSearch and Kibana up and running
- Health check with 
  - Kibana Console UI
  - curl Command
- Create a simple document
- Perform insertion, updatation, retreival and deletion.


## Docker-compose File
To begin with, we will be creating a docker-compose file which
will bring up ElasticSearch running in single node configuration.

### docker-compose.yml
```yaml
version: "3"

services:
    elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:7.14.2
        container_name: elasticsearch
        environment:
            - discovery.type=single-node
        volumes:
            - esdata:/usr/share/elasticsearch/data
        ports:
            - 9200:9200
        networks:
            - elastic
        labels:
            - co.elastic.logs/module=elasticsearch
            - co.elastic.metrics/module=elasticsearch
    kibana:
        image: docker.elastic.co/kibana/kibana:7.14.2
        container_name: kibana
        ports:
            - 5601:5601
        depends_on:
            - elasticsearch
        environment:
            ELASTICSEARCH_URL: http://elasticsearch:9200
            ELASTICSEARCH_HOSTS: http://elasticsearch:9200
        networks:
            - elastic
networks:
    elastic:
      driver: bridge
volumes:
    esdata:
      driver: local
```
### ElasticSearch
1. The line pulls the ElasticSearch image of version 7.14.2
    ```yaml
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.2
    ```
2. Custom name for the container.
    ```yaml
    container_name: elasticsearch
    ```
3.  To run in single node, we set the container environment. 
    ```yaml
            environment:
            - discovery.type=single-node
    ```
4. To maintain persistancy of data on restarting the container and to not loose the data,
   we create a host volume <b>esdata</b> and a container volume 
   /usr/share/elasticsearch/data. Host Volume will maintain the data for multiple restarts of 
   the container.
    ```yaml
        volumes:
            - esdata:/usr/share/elasticsearch/data
    ```
5. Elasticsearch will use port 9200 for requests.
    ```yaml
        ports:
            - 9200:9200
    ```
6. To maintain the security from the other networks in docker we have created a common 
   network for both kibana and elasticsearch
    ```yaml
        networks:
            - elastic
    ```

### Kibana
1. We have to use the same version of kibana as elasticsearch
    ```yaml
    image: docker.elastic.co/kibana/kibana:7.14.2
    ```
2. Custom name for the container.
    ```yaml
    container_name: kibana
    ```
3.   Kibana will connect to the container of elasticsearch with this service name and port.
    ```yaml
                    environment:
            ELASTICSEARCH_URL: http://elasticsearch:9200
            ELASTICSEARCH_HOSTS: http://elasticsearch:9200
    ```
4. This property tells Kibana service to run after the ElasticSearch container is up.
    ```yaml
        depends_on:
            - elasticsearch
    ```
5. Kibana will use port 9200 for visualising the elasticsearch
    ```yaml
        ports:
            - 5601:5601
    ```
   
## Getting The Container Up And Running 
Lets execute the docker-compose.yml to bring up ElasticSearch and Kibana containers.
```commandline
docker-compose --compatibility up
```



   



