# Docker Container
---
## 1. Create container
* docker create
    ```sh
    docker create nginx
    docker start [컨테이너 ID]
    docker stop [컨테이너 ID]
    docker restart [컨테이너 ID]
    ```
* handling all containers
    ```sh
    # stop all containers
    docker stop $(docker ps -aq)

    # remove all containers
    docker rm $(docker ps -aq)

    ```

## 2. Run container
* docker run
    ```sh
    docker run nginx
    ```

## 3. Delete container
* docker rm
    ```sh
    docker rm [컨테이너 ID]
    ```

## 4. Run conatiner with option

### 4-1. `--name` 옵션 : 컨테이너에 이름 부여
```sh
docker run --name nnginx nginx
```

### 4-2. `-d` 옵션 : 백그라운드에서 실행
```sh
docker run -d --name nnginx nginx
```

### 4-3. `-p` 옵션
```sh
docker run -d -P nginx

docker run -d -p 5000:80 nginx
```

## 5. show logs of container

- docker logs
  ```sh
  docker logs nginx-container
  ```