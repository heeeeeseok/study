## @Component
- 개발자가 직접 작성한 클래스를 Bean으로 등록하고자 할 경우 사용
- @Controller, @Service, @Repository 등의 어노테이션에서 상속
- @Component로 등록한 클래스는 다른 클래스에서 Bean으로 불러 사용 가능

## @Configuration
- @Configuration은 내부적으로 @Component를 상속한다
- 외부 라이브러리 또는 내장 클래스를 Bean으로 등록하고자 할 경우 사용<br/>(개발자가 직접 제어가 불가능한 클래스)
- 1개 이상의 @Bean을 제공하는 클래스의 경우 반드시 @Configuration을 사용<br/>즉, 해당 클래스에서 한 개 이상의 Bean을 생성하고 있을 때 선언 해주어야 함
- @Configuration은 등록한 Bean의 싱글톤을 보장하도록 해준다

- ## 정리
- - #### 개발자가 직접 제어 가능 : @Component
  - #### 개발자가 직접 제어 불가능 : @Configuration, @Bean
 

  출처 : [https://velog.io/@albaneo0724/Spring-Component%EC%99%80-Configuration%EC%9D%98-%EC%B0%A8%EC%9D%B4]
