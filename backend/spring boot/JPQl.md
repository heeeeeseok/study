### 객체지향 쿼리 언어
- JPA는 다양한 쿼리 방법을 지원한다 : JPQL, Querydsl, JDBC API, Mybatis

### JDBC 문법
- 엔티티와 속성은 대소문자 구분
- 키워드는 구분하지 않음
- 테이블 이름이 아닌 엔티티 이름 사용
- 별칭 지정 필수
  - select m from Member (as) m where sum.age > 18

### TypeQuery, Query
- TypeQuery: 변환 타입이 명확할 때
- Query: 변환 타입이 명확하지 않을 때

### 결과 조회
```java
private final EntityManager em;

TypeQuery<Member> query = em.createQuery(“select m from Member m”, Member.class);
List resultlist = query.getResultList(); // 결과가 없다면 빈 컬렉션 반환

Query query = em.createQuery("SELECT m.username, m.age from Member m");
```

### 파라미터 바인딩
```java
// 이름 기반 바인딩
Query query = em.createQuery("select m from Member m where m.username = :username")
                  .setParameter("username", "usernameParam");

// 위치 기반 바인딩
Query query = em.createQuery("select m from Member m where m.username =? 1")
                .setParameter(1, usernameParam);
```
- JPA Repository에서 사용
```java
// @Param("{바인딩 파라미터}") 지정 필수
@Query("select i from Item i where i.itemName like :itemName and i.price <= :price")
List<Item> findItems(@Param("itemName") String itemName, @Param("price") Integer price);
```
### 페이징
```java
em.createQuery(“select m from member m order by m.age desc”)
	.setFirstResult(1)
	.setMaxResult(10)
	.getResult();
```
