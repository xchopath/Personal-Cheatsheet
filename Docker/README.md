# Basic Command

## Image
View all images:
```
sudo docker images -a
```

Build image from `Dockerfile`:
```
sudo docker build -t "name:tag" /path-to/dockerfile/
```

Remove image:
```
sudo docker rmi <image>
```

Show all dangle/unused images:
```
sudo docker images -a --filter "dangling=true"
```

## Container

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

Docker run debug (will deleted when finished):
```
sudo docker run -a STDERR -a STDOUT --name <container-name> --rm -ti <image-id>
```

## Deletion

Remove all system (prune):
```
sudo docker system prune -a
```
