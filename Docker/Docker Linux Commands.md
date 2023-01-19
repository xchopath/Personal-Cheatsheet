# Image
View all images:
```
sudo docker images -a
```

Build image from `Dockerfile`:
```
sudo docker build -t "imagename:Dockerfile" /path-to/
```

Remove image:
```
sudo docker rmi <image>
```

Show dangle images:
```
sudo docker images -a --filter "dangling=true"
```

# Container

View all containers:
```
sudo docker ps -a
```

Remove container:
```
sudo docker rm <container>
```

Run container via image:
```
sudo docker run --name <container> -dit <images>
```

Access container shell:
```
sudo docker exec -ti <container> /bin/sh
```

# Miscellaneous

Remove all (prune):
```
sudo docker system prune -a
```
