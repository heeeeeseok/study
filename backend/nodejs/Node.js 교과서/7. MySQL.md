## 1. 데이터베이스 생성
    mysql> CREATE SCHEMA 'nodejs' DEFAULT CHARACTER SET utf8mb4 DEFUALT COLLATE utf8mb4_general_ci;

    uft8mb4 : 한글과 이모티콘 사용 가능
    COLLATE : CHARACTER SET을 어떤 형식으로 정렬할 것인지 의미

## 2. 테이블 생성
```SQL
-- users TABLE
CREATE TABLE nodejs.users(
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(20) NOT NULL,  -- VARCHAR은 가변길이, CHAR은 고정길이
    age INT UNSIGNED NOT NULL,
    married TINYINT NOT NULL,
    comment TEXT NULL,  -- TEXT는 긴 문자열. 보통 수 백자 이내는 VARCHAR을, 그 이상은 TEXT를 사용
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id), -- 기본 키 설정
    UNIQUE INDEX name_UNIQUE (name ASC)  -- 해당 값이 고유해야 하는지에 대한 옵션. name칼럼 ASC(오름차순)으로 기억
)
COMMENT '사용자 정보'  -- 테이블에 대한 보충 설명
ENGINE = InnoDB;

-- comments TABLE
CREATE TABLE nodejs.comments(
    id INT NOT NULL AUTO_INCREMENT,
    commenter INT NOT NULL,
    comment VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id),
    INDEX commenter_idx (commenter ASC),  -- commenter 열에 대한 인덱스 생성
    CONSTRAINT commenter_fk FOREIGN KEY (commenter)  -- 외래 키 참조
    REFERENCES nodejs.users(id)
    ON DELETE CASCADE  -- 외래 키가 삭제되거나 수정될 때 같이 삭제, 수정
    ON UPDATE CASCADE
)
COMMENT '댓글'
ENGINE = InnoDB;
```

## CRUD
    C : INSERT INTO users (name, age, married, comment) VALUES ('zero', 25, 0, '자기소개1');
    R : SELECT * FROM users WHERE married = 0 AND age > 30;
        SELECT name, age FROM users ORDER BY age DESC LIMIT 1 OFFSET 1;
    U : UPDATE users SET comment = '바꿀 내용' WHERE id = 1;
    D : DELETE FROM users WHERE id = 2;

## 시퀄라이즈 사용하기
    시퀄라이즈는 ORM(Object relational Mapping)으로 분류된다.
    시퀄라이즈는 자바스크립트 구문을 알아서 SQL로 바꿔준다. 따라서 JS만으로 MySQL을 조작할 수 있다.

    $ npm i sequelize sequelize-cli mysql2

    sequelize-cli는 시퀄라이즈 명령어를 실행하기 위한 패키지이고, mysql2는 MySQL과 시퀄라이즈를 이어주는 드라이버

    $ npx sequelize init

    
    
