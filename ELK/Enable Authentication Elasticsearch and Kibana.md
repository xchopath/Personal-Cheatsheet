# Elasticsearch

### Enable xpack on Elasticsearch Configuration

Edit `/etc/elasticsearch/elasticsearch.yml`:
```
xpack.security.enabled: true
discovery.type: single-node
```

Restart Elasticsearch Service:
```
sudo systemctl elasticsearch kibana
```

### Add Superuser on Elasticsearch
```
sudo /usr/share/elasticsearch/bin/elasticsearch-users useradd <username> -p <password> -r superuser
```

----------

# Kibana

### Add Auth on Kibana Configuration

Add user that were created in `/etc/kibana/kibana.yml`:
```
elasticsearch.username: "<username>"
```

Add password via CLI:
```
sudo /usr/share/kibana/bin/kibana-keystore add elasticsearch.password
```

Restart Kibana:
```
sudo systemctl restart kibana
```
