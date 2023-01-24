Docker-compose up
```
sudo docker-compose up -d
```

Docker-compose exec to add kibana_system
```
sudo docker-compose exec elasticsearch sh -c "elasticsearch-users useradd kibana_sys -p changeme -r kibana_system"
```
