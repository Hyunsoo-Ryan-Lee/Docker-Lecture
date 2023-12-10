# Port, Volume setting

---

## 1. Port forwarding

- `-p` : {host_port}:{container_port}

- docker run
  ```sh
  docker run -d -p 80:80 --name nginx-container nginx
  docker run -d -p 8080:80 --name nginx-container nginx
  ```

## 2. Docker file copy
- docker cp
  ```sh
  # 로컬 -> 컨테이너

  docker cp [로컬 경로] [컨테이너 ID]:[컨테이너 내부 경로]
  docker cp ./nginx/index.html 502dc5ecc932:/usr/share/nginx/html/index.html 


  # 컨테이너 -> 로컬

  docker cp [컨테이너 ID]:[컨테이너 내부 경로] [로컬 경로]
  docker cp 502dc5ecc932:/usr/share/nginx/html/index.html ./indexxx.html   
  ```

## 3. Volume Mounting

### 3-1. 디렉토리끼리 직접 연결
- `-v` : {host_volume}:{container_volume}

- docker run
  ```sh
  docker run -d \
      -p 8080:80 \
      -v d/dockertest/nginx/:/usr/share/nginx/html/ \
      --name nginx-container nginx
  ```

### 3-2. Volume 생성하여 연결
```sh
docker volume create --name myvolume

docker run -d --name nginx-vol -v [볼륨 이름]:[컨테이너 내부 경로] nginx
docker run -d --name nginx-vol -v myvolume:/usr/share/nginx/html/ nginx
```

## 4. Nginx index.html 파일 수정하는 방법

#### 1. docker exec
#### 2. docker cp
#### 3. docker volume