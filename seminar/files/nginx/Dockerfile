FROM nginx:alpine
RUN echo "hello world" > /home/hello.txt
ENV CODEIT Sprint
WORKDIR /usr/share/nginx/html
COPY index.html /usr/share/nginx/html/index.html