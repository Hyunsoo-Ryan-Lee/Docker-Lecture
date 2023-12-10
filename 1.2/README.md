# Execute Inside Container
---
## 1. execute command
  * `-i` 옵션 -> interactive옵션으로 입력을 지속할 수 있도록 해줌
  * `-t` 옵션 -> pseudo-TTY 옵션으로 컨테이너에 터미널 드라이버를 추가하여 컨테이너 내부에서 터미널처럼 사용 할 수 있도록.
  - docker exec
    ```sh
    docker exec -it nginx bash

    docker exec -it busybox sh

    docker exec -it nginx [linux 명령]
    ```
    ```sh
    docker exec -it nginx-container bash
    # in nginx-container
    echo "hello" > /usr/share/nginx/html/index.html
    exit
    ```

## 2. 일회성 작업
  * `--rm` 옵션 : 런타임 종료시 바로 컨테이너가 종료되는 옵션으로 일회성 작업 등에 사용
    ```sh
    docker run --rm -it nginx bash
    ```