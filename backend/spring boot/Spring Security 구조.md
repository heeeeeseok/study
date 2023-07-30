# Spring Security란?
    spring 기반의 애플리케이션의 보안(인증과 권한, 인가 등)을 담당하는 스프링 하위 프레임워크.
    spring security는 인증과 권한에 대한 부분을 Filter의 흐름에 따라 처리
    Filter는 Dispatcher Servlet으로 가기 전에 적용되므로 가장 먼저 URL 요청을 받지만,
    Interceptor는 Dispatcher와 Controller 사이에 위치한다는 점에서 적용 시기의 차이가 있다.

    Client(request) → Filter → DispatcherServlet → Interceptor → Controller

## Spring Security Architecture
<image src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbeDENY%2FbtrBs0cquNc%2FPkwRQzgyzhoy1ecQrlQOJk%2Fimg.png">

    1. 사용자가 로그인 정보와 함께 인증 요청을 한다. (Http Request)
    2. AuthenticationFilter가 요청을 가로채고, 가로챈 정보를 통해 UsernamePasswordAuthenticationToken의
        인증용 객체를 생성한다.
    3. AuthenticationManager의 구현체인 ProviderManager에게 생성한 UsernamePasswordToken 객체를 전달한다.
    4. AuthenticaionManager는 등록된 AuthenticationProvider을 조회하여 인증을 요구한다.
    5. 실제 DB에서 사용자 인증정보를 가져오는 UserDetailsService에 사용자 정보를 넘겨준다.
    6. 넘겨받은 사용자 정보를 통해 DB에서 찾은 사용자 정보인 UserDetails 객체를 만든다.
    7. AuthenticationProvider은 UserDetails를 넘겨받고 사용자 정보를 비교한다.
    8. 인증이 완료되면 권한 등의 사용자 정보를 담은 Authentication 객체가 반환된다.
    10. Authentication 객체를 SecurityContext에 저장한다.

    최종적으로 SecurityContextHolder는 세션 영역에 있는 SecurityContext에 Authentication 객체를 저장한다.

## Authentication
    현재 접근하는 주체의 정보와 권한을 담는 인터페이스.
    SecurityContext에 저장되며, SecurityContextHolder를 통해 SecurityContext에 접근하고,
    SecurityContext를 통해 Authentication에 접근할 수 있다.

## UsernamePasswordAuthenticationToken
    Authentication을 implements한 AbstractAuthenticationToken의 하위 클래스로,
    User의 ID가 Principal의 역할, Password가 Credential의 역할을 한다.

## AuthenticationProvider
    실제 인증에 대한 부분을 처리한다.
    인증 전의 Authentication 객체를 받아서 인증이 완료된 객체를 반환하는 역할을 한다.
    
