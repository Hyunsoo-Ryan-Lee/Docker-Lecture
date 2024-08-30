# Network setting

---

## 1. Network basics

- 1. Run nginx container

  ```sh
  docker run -d --name -p 8080:80 nginx-container nginx
  ```

- 2. Get Network info of `nginx-container`

  ```sh
  docker network inspect bridge
  # {nginx-container ip}='172.17.0.2'
  ```

- 2. Run linux(alpine) container

  ```sh
  # in host
  docker run -d -i --name alpine-container alpine

  # in alpine-container
  docker exec -it alpine-container sh
  wget {nginx-container ip} # wget 172.17.0.2
  cat index.html
  exit
  ```

## 2. Bridge Network Concept 실습

- https://velog.io/@newnew_daddy/DOCKER02

  1. network 목록 확인
  2. my-net 이름의 bridge network 생성
  3. my-net 내부에 container 2개 생성
  4. ping command로 컨테이너끼리 통신 확인
  5. ping command로 다른 network 내의 conatiner와 통신 확인

  ```sh
  docker network ls

  docker network create my-net

  docker network inspect my-net

  docker run -itd --name one busybox

  docker network connect my-net one
  docker network disconnect bridge one

  docker run -itd --name two --network my-net busybox

  docker exec one ping two
  ```
## 3. Wordpress-Mysql 연동 App 실습
* MYSQL
  ```sh
  docker run -d \
    --name db \
    --restart always \
    -e MYSQL_ROOT_PASSWORD=mysqlroot \
    -e MYSQL_DATABASE=wordpress \
    -e MYSQL_USER=wordpress \
    -e MYSQL_PASSWORD=wordpress \
    -v db_data:/var/lib/mysql \
    --expose 3306 \
    --expose 33060 \
    mariadb:10.6.4-focal \
    --default-authentication-plugin=mysql_native_password
  ```

* WORDPRESS
  ```sh
  docker run -d \
    --name wordpress \
    --restart always \
    -e WORDPRESS_DB_HOST=db \
    -e WORDPRESS_DB_USER=wordpress \
    -e WORDPRESS_DB_PASSWORD=wordpress \
    -e WORDPRESS_DB_NAME=wordpress \
    -p 8085:80 \
    --link db:db \
    wordpress:latest
  ```
