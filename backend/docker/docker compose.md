### Docker Compose
- 단일 서버에서 여러 개의 컨테이너를 하나의 서비스로 정의하여 컨테이너 묶음으로 관리할 수 있도록 하는 관리 도구
- docker compose 파일의 내용을 바탕으로 순차적으로 컨테이너를 생성
- docker compose 생성 시 자동으로 network가 만들어지고 생성한 컨테이너들은 해당 network에 연결된다

```
version: "3.7"  // yaml 파일 포맷 버전. 가급적 최신 버전 사용

services: // 생성하고자 하는 컨테이너 명시
  db: // 컨테이너 명
    image: mysql:5.7
    volumes:
      - ./db_data:/var/lib/mysql    // host의 db_data와 컨테이너의 /var/lib/mysql 연결
    restart: always
    environment:    // 환경변수
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress_user
      MYSQL_PASSWORD: 123456
  
  app:
    depends_on:   // 해당 컨테이너의 의존성
      - db
    image: wordpress:latest
    volumes:
      - ./app_data:/var/www/html
    ports:    // host의 8080 port와 컨테이너의 80 port 연결
      - "8080:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wordpress_user
      WORDPRESS_DB_PASSWORD: 123456
```

### docker compose yaml 파일 옵션
- version
  - yaml 파일 포맷 버전
- services
  - 생성될 컨테이너들을 묶어놓은 단위
- image
  - 컨테이너를 생성할 이미지의 이름
- links
  - docker run --link 와 동일
  - 서비스명으로 접근 가능
- environment
  - docker run -e 와 동일
  - 컨테이너 내부의 환경변수 지정
- command
  - 컨테이너가 실행될 때 수행할 명령어를 설정
- depends_on
  - 특정 컨테이너에 대한 의존관계
  - 명시된 컨테이너가 먼저 생성되고 실행된다
- port
  - docker run -p 와 동일
  - 호스트환경의 port와 컨테이너 환경의 port를 연결
- build
  - build 항목의 dockerfile에서 이미지를 빌드하여 컨테이너 생성
  - image: 옵션과 함께 새롭게 빌드될 이미지의 이름을 지정
