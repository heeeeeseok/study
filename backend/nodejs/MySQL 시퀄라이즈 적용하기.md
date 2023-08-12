## 1. 패키지 설치
```bash
$ npm i sequelize sequelize-cli mysql2
```
- sequelize-cli : 시퀄라이즈 명령어를 실행하기 위한 패키지. 설정 자동 생성
- mysql2 : MySQL과 시퀄라이즈를 이어주는 드라이버. 데이터베이스 프로그램이 아니다.

## 2. 명령어 호출, 설정
```bash
$ npx sequelize init
```
- sequelize-cli에 의해 자동생성된 models/index.js 수정
- config/config.js에 db 정보 입력 (username, password, database ...)

## 3. MySQL 연결
```javascript
// app.js
...

const { sequelize } = require('./models'); // db

// 서버 실행 시 MySQL과 연동되도록 한다.
sequelize.sync({ force: true })
    .then(() => {
        console.log('데이터베이스 연결 성공');
    })
    .catch((err) => {
        console.log(err);
    });

...
```
## 4. 모델 정의하기
```javascript
// models/user.js

const Sequelize = require('sequelize');

class User extends Sequelize.Model {
    // 테이블 설정
    static initiate(sequelize) {
        // 첫 번째 인자 : 테이블 칼럼 설정
        User.init({
            name: {
                type: Sequelize.STRING(20),
                allowNull: false,
                unique: true,
            },

            age: {
                type: Sequelize.INTEGER.UNSIGNED,
                allowNull: false,
            },

            married: {
                type: Sequelize.BOOLEAN,
                allowNull: true,
            },

            comment: {
                type: Sequelize.TEXT,
                allowNull: true,
            },

            created_at: {
                type: Sequelize.DATE,
                allowNull: false,
                defaultValue: Sequelize.NOW,
            },
        }, 
        // 두 번째 인자 : 테이블 자체 설정
        {
            sequelize,
            timestamps: false, // true: createdAt, updatedAt 칼럼 추가
            underscored: false, // true: 테이블명과 칼럼명 스네이크 케이스로 적용
            modelName: 'User',
            tableName: 'uesrs',
            paranoid: false, // true: deletedAt 칼럼 생성
            charset: 'utf-8',
            collate: 'utf8_general_ci',
        });
    }

    // 다른 모델과의 관계
    static associate(db) {
        db.User.hasMany(db.Comment, { foreignKey: 'commenter', soureKey: 'id' });
    }
};

module.exports = User;
```
- 모델을 생성하고 models/index.js 수정
```javascript
// index.js

const Sequelize = require('sequelize');
const User = require('./user');
const Comment = require('./comment');
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const db = {};

// db 연결을 관리하기 위한 인스턴스
const sequelize = new Sequelize(config.database, config.username, config.password, config);
db.sequelize = sequelize;

// db 객체에 User, Comment 모델 추가. 이후에 db 객체를 require해서 User, Comment에 접근 가능
db.User = User;
db.Comment = Comment;

// 테이블과 모델 연결
User.initiate(sequelize);
Comment.initiate(sequelize);

// 테이블 간의 관계 설정
User.associate(db);
Comment.associate(db);

module.exports = db;
```

## 쿼리 작성
```javascript
INSERT INTO nodejs.users (name, age, married, comment) VALUES ('zero', 24, 0, '자기소개1');
const { User } = require('../models');
User.create({
    name: 'zero',
    age: 24,
    married: 0,
    comment: '자기소개1',
});

SELECT * FROM nodejs.users;
User.findAll({});

SELECT * FROM nodejs.uesrs LIMIT 1;
User.findOne({});

SELECT name, married FROM nodejs.users;
User.findAll({
    attribute: ['name', 'married'],
})

SELECT name, age FROM nodejs.users WHERE marrid = 1 AND age > 30;
const { Op } = require('sequelize');
const { User } = require('../models');
User.findAll({
    attributes: ['name', 'age'],
    where: {
        marrid: true,
        age: { [Op.gt]: 30 }, // (gt: 초과, gte: 이상, lt: 미만, lte: 이하, ne: 같지 않음)
    }
})

SELECT name, age FROM nodejs.users WHERE marrid = 1 OR age > 30;
const { Op } = require('sequelize');
const { User } = require('../models');
User.findAll({
    attributes: ['name', 'age'],
    where: {
        [Op.or]: [{ marrid: false }, { age: { [Op.gt]: 30 } }],
    }
})

SELECT id, name FROM users ORDER BY age DESC LIMIT 1 OFFSET 1;
User.findAll({
    attributes: ['id', 'name'],
    order: [['age', 'DESC']],
    limit: 1,
    offset: 1,
});

UPDATE nodejs.users SET comment = '바꿀 내용' WHERE id = 2;
User.update({
    comment: '바꿀 내용',
}, {
    where: { id: 2 },
});
// 첫 번째 인수는 수정할 내용 두 번째 인수는 where 옵션에 조건들을 적는다

DELETE FROM nodejs.users WHERE id = 2;
User.destroy({
    where: { id: 2 },
});
```
