# NginX LoadBalancing & 실습
---
## 1. compose up
* docker-compose up
    ```sh
    docker-compose up -d --build
    ```

## 2. keep watching compose logs
* docker-compose logs
    ```sh
    docker-compose logs -f
    ```

## 3. compose down
* docker-compose down
    ```sh
    docker-compose down
    ```
    
## 4. Docker Compose로 변환 실습
- 1.5의 `Wordpress-Mysql 연동 App 실습` 코드를 Docker compose로 변환

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
