# `Dockerizing` 실습

## 1. build and run app-container

- build image

  ```sh
  docker build -t fastapi-img .
  ```

- run app-container

  ```sh
  docker run -d --name fastapi-container -p 5000:80 fastapi-img
  ```
