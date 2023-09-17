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
# google
spring.security.oauth2.client.registration.google.client-id={클라이언트 ID}
spring.security.oauth2.client.registration.google.client-secret={클라이언트 보안 비밀번호}
spring.security.oauth2.client.registration.google.scope= profile, email
```

### gradle.build
- implementation 'org.springframework.boot:spring-boot-starter-oauth2-client' 추가

### SecurityConfig
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

### CustomOAuth2UserService
```java
@Service
@Slf4j
@RequiredArgsConstructor
public class CustomOAuth2UserService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {

    private final UserRepository userRepository;
    private final HttpSession httpSession;

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {

        OAuth2UserService<OAuth2UserRequest, OAuth2User> delegate = new DefaultOAuth2UserService();
        OAuth2User oAuth2User = delegate.loadUser(userRequest);

        // OAuth2 서비스 id (google, kakao, naver ...)
        String registrationId = userRequest.getClientRegistration().getRegistrationId();
        log.info("registrationId: {}", registrationId);

        // OAuth2 로그인 진행 시 키가 되는 필드 값(PK), 어떤 속성을 이용하여 식별할지
        String userNameAttributeName = userRequest.getClientRegistration().getProviderDetails()
                .getUserInfoEndpoint().getUserNameAttributeName();
        log.info("userNameAttributeName: {}", userNameAttributeName);

        // OAuth2 서비스에서 전달해준 정보
        log.info("oAuth2User.getAttributes(): {}", oAuth2User.getAttributes().toString());
        OAuthAttributes attributes = OAuthAttributes.of(registrationId, userNameAttributeName,
                oAuth2User.getAttributes());

        // 넘겨받은 정보를 바탕으로 User 인스턴스 수정 or 추가
        User user = saveOrUpdate(attributes);

        // 세션에 sessionUser 정보 추가
        httpSession.setAttribute("user", new SessionUser(user));
        log.info("user sesseion: {}", httpSession.getAttribute("user").toString());

        return new DefaultOAuth2User(Collections.singletonList(new SimpleGrantedAuthority(user.getRoleKey())),
                attributes.getAttributes(),
                attributes.getNameAttributeKey());
    }

    private User saveOrUpdate(OAuthAttributes attributes) {
        User user = userRepository.findByEmail(attributes.getEmail())
                .map(userEntity -> userEntity.update(attributes.getName(), attributes.getPicture()))
                .orElse(attributes.toEntity());

        return userRepository.save(user);
    }
}
```

### OAuthAttributes
```java

@Getter
@Builder
@Slf4j
public class OAuthAttributes {
    private Map<String, Object> attributes; // OAuth2 반환하는 유저 정보 Map
    private String nameAttributeKey;
    private String name;
    private String email;
    private String picture;

    public static OAuthAttributes of(String registrationId, String userNameAttributeName, Map<String, Object> attributes){
        // 여기서 네이버와 카카오 등 구분 (ofNaver, ofKakao)
        if (registrationId.equals("google")) {
            return ofGoogle(userNameAttributeName, attributes);
        } else {
            log.info("registrationId Not Found");
            return null;
        }
    }

    private static OAuthAttributes ofGoogle(String userNameAttributeName, Map<String, Object> attributes) {
        return OAuthAttributes.builder()
                .name((String) attributes.get("name"))
                .email((String) attributes.get("email"))
                .picture((String) attributes.get("picture"))
                .attributes(attributes)
                .nameAttributeKey(userNameAttributeName)
                .build();
    }

    public User toEntity(){
        return User.builder()
                .name(name)
                .email(email)
                .picture(picture)
                .role(Role.GUEST) // 기본 권한 GUEST
                .build();
    }
}
```
