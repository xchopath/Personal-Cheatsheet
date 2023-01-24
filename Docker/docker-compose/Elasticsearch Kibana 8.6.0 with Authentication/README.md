**docker-compose.yaml**
```
version: "3"
services:
  elasticsearch:
    image: "docker.elastic.co/elasticsearch/elasticsearch:8.6.0"
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=true
      - xpack.security.audit.enabled=true
      - ELASTIC_PASSWORD=changeme
    ports:
      - "9200:9200"
      - "9300:9300"
    volumes:
      - elasticsearch-data:/usr/share/elasticsearch/data
      - elasticsearch-config:/usr/share/elasticsearch/config
    networks:
      - elasticstacknetwork
  kibana:
    depends_on:
      - elasticsearch
    image: "docker.elastic.co/kibana/kibana:8.6.0"
    container_name: kibana
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_URL=http://elasticsearch:9200
      - ELASTICSEARCH_USERNAME=kibana_sys
      - ELASTICSEARCH_PASSWORD=changeme
    networks:
      - elasticstacknetwork
networks:
  elasticstacknetwork:
    driver: bridge
volumes:
  elasticsearch-data:
    driver: local
  elasticsearch-config:
    driver: local
```

docker-compose up
```
sudo docker-compose up -d
```

docker-compose exec to add kibana system user
```
sudo docker-compose exec elasticsearch sh -c "elasticsearch-users useradd kibana_sys -p changeme -r kibana_system"
```