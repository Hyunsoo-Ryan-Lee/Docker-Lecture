# Dockerfile & Build
---
## 1. Running Container -> Image 생성
* docker commit
    ```sh
    docker commit [컨테이너 ID] [이미지 이름]
    docker commit [컨테이너 ID] [docker hub ID]/[image name]:[tag]
    ```

## 2. About Dockerfile
- https://velog.io/@newnew_daddy/DOCKER01

## 3. nginx image build 실습
* build image
    ```sh
    docker build -t [이미지 이름] [Dockerfile 경로]

    docker build -t nginx-img nginx
    ```

* run nginx container
    ```sh
    docker run -d -p 8080:80 --name nginx-container nginx-img
    ```

* check network bridge status
    ```sh
    docker network inspect bridge # nginx-container IP = 172.17.0.2
    ```

## 2. ubuntu image build 실습
* build image
    ```sh
    docker build -t ubuntu-img ubuntu
    ```

* run ubuntu container
    ```sh
    docker run -d -i --name ubuntu-container ubuntu-img
    docker exec -it ubuntu-container bash curl {nginx-container ip} # curl 172.17.0.2
    ```