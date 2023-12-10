# Docker Image
---
## 0. 환경 설정
* docker desktop 실행
* docker hub 계정 생성 후 로그인
* 시작  ->  `Windows 기능 켜기/끄기`  ->  `NFS용 서비스` -> `NFS용 클라이언트` 체크  ->  확인 

## 1. Docker Login
```sh
docker login
```

## 2. Docker Search
```sh
docker images

docker search busybox

docker search -f stars=10 busybox

docker search -f is-official=true nginx

docker search -f is-official=true --no-trunc nginx
```

## 3. Manage Docker Image resources 

### 3-1. image list
* docker images
    ```sh
    docker images
    ```

### 3-2. get image from DockerHub
* docker pull
    ```sh
    docker pull nginx # nginx:latest
    ```

### 3-3. delete image
* docker rmi
    ```sh
    docker rmi nginx # nginx:latest
    ```

* delete all images
    ```sh
    docker rmi $(docker images -aq)
    ```

### 3-4. push image
* docker push
    ```sh
    docker login
    docker push {YOUR_CUSTOM_IMAGE}:{TAG}
    docker push [docker hub ID]/[image name]:[tag]
    ```