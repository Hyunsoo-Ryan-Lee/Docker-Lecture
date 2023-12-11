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

    ```sh
    version: "3"
    services:
    mysql:
        image: mysql
        container_name: mysql-container
        networks:
        - wordpress-network
        volumes:
        - mysql-volume:/var/lib/mysql
        restart: always
        environment:
        MYSQL_ROOT_PASSWORD: P@ssw0rd
        MYSQL_DATABASE: wordpress
        MYSQL_USER: wpadm
        MYSQL_PASSWORD: P@ssw0rd
        command: ['mysqld', '--character-set-server=utf8mb4', '--collation-server=utf8mb4_unicode_ci', '--default-authentication-plugin=mysql_native_password']
        cpus: 0.5
        mem_limit: 1000m
    wordpress:
        depends_on:
        - mysql
        image: wordpress
        container_name: wordpress-container
        networks:
        - wordpress-network
        volumes:
        - wordpress-volume:/var/www/html
        ports:
        - 8085:80
        restart: always
        environment:
        WORDPRESS_DB_HOST: mysql
        WORDPRESS_DB_NAME: wordpress
        WORDPRESS_DB_USER: wpadm
        WORDPRESS_DB_PASSWORD: P@ssw0rd
        cpus: 0.5
        mem_limit: 500m
    networks:
    wordpress-network:
    volumes:
    mysql-volume:
    wordpress-volume:
    ```
