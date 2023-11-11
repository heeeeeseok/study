### docker image 생성
1. commit container - 백업
2. dockerfile - 생성

```
FROM ubuntu:20.04

RUN apt update && apt install -y python3 // build 시점의 명령어
WORKDIR /var/www/html  // 컨테이너에서 해당 디렉토리가 없다면 생성, pwd로 지정
COPY "index.html" "."  // host의 파일을 workdir로 copy
CMD [ "python3", "-u", "-m", "http.server" ]  // 컨테이너 실행 시점의 명령어
```
