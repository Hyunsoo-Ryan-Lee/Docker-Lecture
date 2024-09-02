### 0. 초기 세팅
- brew install watch
- watch -n 1 docker ps
### 1. Docker Hub 로그인
- docker login
- docker search nginx
### 2. Docker 기본 명령어
- docker images
- docker pull [이미지 이름]:[tag]
  - docker pull nginx
  - docker pull nginx:1.13.0
- docker rmi [이미지 이름]
- docker ps
- docker ps -a
### 3. Docker Container Basics
- docker create nginx
- docker start [컨테이너 ID]
- docker stop [컨테이너 ID]
- docker rm [컨테이너 ID]
- docker run nginx
- docker rm -f [컨테이너 ID]
### 4. Docker Container with Options -1
1. `--name`
   - docker run --name nginx_cnt nginx
2. `-d`
   - docker run -d --name nginx_cnt nginx
3. `docker logs`
    - docker logs nginx_cnt
    - docker logs -f nginx_cnt
4. `-p`
   - docker run -d -p 80:80 --name nginx_cnt nginx
### 5. Docker Container with Options -2
1. `-it`
   - docker exec -it nginx_cnt bash
     - cat /usr/share/nginx/html/index.html
     - echo "hello" > /usr/share/nginx/html/index.html
1. `-v` 
   - docker run -d -p 80:80 -v [host 경로]:/usr/share/nginx/html/ --name nginx_cnt nginx
2. `-e`
   - docker run -d --name fastapi -p 5000:80 -e ENV=codeit hyunsoolee0506/fastapi-img:0.5
### 6. Docker Before&After
- 컴퓨터에 MYSQL 설치
  - BEFORE
    - https://www.codeit.kr/topics/data-analysis-using-sql/lessons/3142
  - AFTER
    ```bash
    docker run --name mysql_cnt \
      -e MYSQL_ROOT_PASSWORD=codeit \
      -e MYSQL_USER=hyunsoo \
      -e MYSQL_PASSWORD=910506 \
      -d -p 3307:3306 mysql
    ```
### 7. Dockerfile
- [Dockerfile 옵션들 설명](https://velog.io/@newnew_daddy/DOCKER01)
- docker build -t [이미지 이름] [Dockerfile 경로]
  - docker build -t nginx-img nginx
  - docker run -d -p 80:80 --name nginx_img_cnt nginx-img
  - docker build -t ubuntu-img ubuntu
  - docker run -d --name ubuntu_img_cnt ubuntu-img
### 8. Docker Compose
- docker compose up
- docker compose up -d
- docker compose ls
- docker compose ps
- docker compose down

`docker run -d -p 80:80 -v [host 경로]:/usr/share/nginx/html/ --name nginx_cnt nginx`
```yaml
services:
  nginx:
    image: nginx
    container_name: nginx_cnt
    ports:
      - "80:80"
    volumes:
      - [host 경로]:/usr/share/nginx/html/
```
`docker run --name mysql_cnt -e MYSQL_ROOT_PASSWORD=codeit -d -p 3307:3306 mysql`
```yaml
services:
  mysql:
    image: mysql
    container_name: mysql_cnt
    environment:
      - MYSQL_ROOT_PASSWORD=codeit
      - MYSQL_USER=hyunsoo
      - MYSQL_PASSWORD=910506
    ports:
      - "3307:3306"
```
통합
```yaml
services:
  nginx:
    image: nginx
    container_name: nginx_cnt
    ports:
      - "80:80"
    volumes:
      - [host 경로]:/usr/share/nginx/html/

  mysql:
    image: mysql
    container_name: mysql_cnt
    environment:
      - MYSQL_ROOT_PASSWORD=codeit
      - MYSQL_USER=hyunsoo
      - MYSQL_PASSWORD=910506
    ports:
      - "3307:3306"
```
### 9. Docker Compose 실습
1. Wordpress-MariaDB
    ```yaml
    services:
    db:
        image: mariadb:10.6.4-focal
        command: '--default-authentication-plugin=mysql_native_password'
        volumes:
        - db_data:/var/lib/mysql
        restart: always
        environment:
        - MYSQL_ROOT_PASSWORD=mysqlroot
        - MYSQL_DATABASE=wordpress
        - MYSQL_USER=wordpress
        - MYSQL_PASSWORD=wordpress
        expose:
        - 3306
    wordpress:
        image: wordpress:latest
        ports:
        - 8085:80
        restart: always
        environment:
        - WORDPRESS_DB_HOST=db
        - WORDPRESS_DB_USER=wordpress
        - WORDPRESS_DB_PASSWORD=wordpress
        - WORDPRESS_DB_NAME=wordpress
    volumes:
    db_data:
    ```
2. Airflow
  - [Airflow 로컬에 설치(windows)](https://vivekjadhavr.medium.com/how-to-easily-install-apache-airflow-on-windows-6f041c9c80d2)
  - [Airflow Docker-Compose로 설치](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
### 10. 추가 참고 자료
- [도커 네트워크 관련](https://accesto.com/blog/docker-networks-explained-part-2/)


