## Spring Bean이란?
- Spring IOC 컨테이너가 관리하는 자바 객체를 Bean이라고 부른다
- IOC는 Inversion Of Control의 약자로 사용자의 제어권을 다른 주체에게 넘기는 것을 말한다.

## Spring Bean을 Spring IOC Container에 등록하기
- ### 2.1 자바 어노테이션 사용
  - @Component (@Service, @Controller, @Repository는 내부적으로 @Component를 포함)
  - @Configuration, @Bean

참고 : [@Component와 @Configuration의 차이]()
출처 : [https://melonicedlatte.com/2021/07/11/232800.html]
