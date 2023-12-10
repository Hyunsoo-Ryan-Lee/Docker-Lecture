# Dockerfile 실습

---

## 1. fastapi
## 2. express app + nginx web server
## 3. Jupyter Notebook Dockerfile 생성 실습

1. 사용할 dockerfile 인자들 : COPY, FROM, USER, WORKDIR, EXPOSE
2. Base 이미지는 jupyter/minimal-notebook 사용
3. 기본 작업 디렉토리는 '/workspace'
4. requirements.txt 파일이 있는 경로를 컨테이너 내부 '/workspace' 경로로 복사
5. 사용자는 root
6. 8888번 포트 노출

- Dockerfile template
    ```dockerfile
    [인자1]

    [인자2]

    [인자3]

    [인자4]

    RUN apt-get update
    RUN apt-get install -y python3-pip
    RUN pip install -r requirements.txt

    [인자5]

    CMD ["jupyter", "notebook","--ip", "0.0.0.0", "--port", "8888", "--allow-root", "--NotebookApp.token='password'"]
    ```

## 4. 재미있는/유용한 Docker Image

```sh
# portainer
docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce

# whalesay
docker run docker/whalesay cowsay "hahaha"

# funbox image
https://hub.docker.com/r/wernight/funbox

# supermario image
https://hub.docker.com/r/pengbai/docker-supermario/

# 2048 game image
public.ecr.aws/kishorj/docker-2048:latest

hyunsoolee0506/game2048:latest

```

