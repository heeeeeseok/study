### docker image 생성
1. commit container - 백업
2. dockerfile - 생성

### Dockerfile 예시
```
FROM ubuntu:20.04  // base image

RUN apt update && apt install -y python3 // build 시점의 명령어
ADD ./test /test  // host 환경의 현재 디렉토리의 test를 컨테이너 환경의 루트 디렉토리에 배치
WORKDIR /var/www/html  // 컨테이너에서 해당 디렉토리가 없다면 생성, pwd로 지정
COPY "index.html" "."  // host의 파일을 workdir로 copy
CMD [ "python3", "-u", "-m", "http.server" ]  // 컨테이너 실행 시점의 명령어
```

### Dockerfile로 이미지 빌드, 실행
```
docker build -t [build image name]
docker rm --force [build container name] // 해당 이름으로 실행 중인 컨테이너 종료, delete
docker run [option] --name [build image name] [build container name]
```
