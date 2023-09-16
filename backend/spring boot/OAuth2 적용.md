### 구글 서비스 등록
- 새 프로젝트 생성
- OAuth 클라이언트 ID, 기본정보 입력
- 범위 추가 또는 삭제, email, profile, openid 선택
- OAuth 클라이언트 ID, 리다이렉션 URI 입력
- 클라이언트 ID, 클라이언트 보안 비밀번호 저장

### application.propertise
- spring.profiles.include=oauth 추가

### application-oauth.properties
```
spring.security.oauth2.client.registration.google.client-id={클라이언트 ID}
spring.security.oauth2.client.registration.google.client-secret={클라이언트 보안 비밀번호}
spring.security.oauth2.client.registration.google.scope= profile, email
```

### gradle.build
- implementation 'org.springframework.boot:spring-boot-starter-oauth2-client' 추가

### Config 클래스 작성
```java
@RequiredArgsConstructor
@EnableWebSecurity
@Configuration
public class SecurityConfig {

    private final CustomOAuth2UserService customOAuth2UserService;

    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
        httpSecurity
                .csrf().disable()
                .authorizeHttpRequests()
                .antMatchers({모두에게 허용할 url}).permitAll()
                .antMatchers({권한이 필요한 url}).hasRole(Role.USER.name())
                .anyRequest().authenticated()

                .and()
                .logout().logoutSuccessUrl("/")

                .and()
                .oauth2Login()
                .userInfoEndpoint()
                .userService(customOAuth2UserService);

        return httpSecurity.build();
    }
}
```

