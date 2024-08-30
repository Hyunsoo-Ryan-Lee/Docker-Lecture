# Run conatiner with advanced options
---

## 1. `-w` 옵션 : exec했을 때 컨테이너 실행되는 기본 작업 디렉토리 설정
```sh
docker run --name nginx-w -d -w /tmp/to/dir/ nginx
```

## 2. `-h` 옵션 : exec했을 때 컨테이너의 hostname을 지정
```sh
docker run -d --name nginx-h -h hyunsoo nginx
```

## 3. `-e` 옵션 : 컨테이너 내부 환경 변수 설정
```sh
docker run -d --name nginx-e -e MY_NAME=hyunsoo nginx
```

## 4. `-l` 옵션 : 컨테이너에 라벨링 할 수 있는 설정
```sh
docker run -d --name nginx-l --label version=1.0 nginx

docker ps --filter "label=version=1.0"
```