# Hello Compose!
---
## 1. Basic commands
* compose up
    ```sh
    docker compose up

    docker compose up -d

    docker compose -f [경로] up

    docker compose up --build
    ```

* compose down
    ```sh
    docker compose down

    docker compose stop <service>

    docker compose start <service>

    docker copmose restart <service>
    ```

* check status
    ```sh
    docker compose ps

    docker-compose ps -a

    docker compose logs <service>

    docker compose logs <service> -f

    docker compose logs -f
    ```

* execute command
    ```sh
    # docker-compose exec {service_name} {command}
    docker-compose exec app /bin/sh
    ```

## 2. docker run -> docker compose
* docker run
  ```sh
  docker run -d --name fastapi -p 5000:80 hyunsoolee0506/k8s-fastapi:0.3
  ```

* docker compose
  ```docker-compose
  services:
  fastapi:
      image: hyunsoolee0506/k8s-fastapi:0.3
      container_name: fastapi
      ports:
      - '5000:80'
  ```
