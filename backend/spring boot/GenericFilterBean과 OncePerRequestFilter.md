## GenericFilterBean과 OncePerRequestFilter
GenericFilterBean과 OncePerRequestFilter는 둘 다 대상을 필터로 등록해주는 인터페이스이다.<br/>
※ Filter는 DispatcherServlet 보다 먼저 클라이언트의 요청을 받는다.<br/><br/>


GenericFilterBean은 서블릿이 다른 서블릿으로 dispatch 되는 경우에 다시 한 번 Filter chain을 거치게 된다<br/>
이 때 한 번의 요청에 한 번의 인증 처리만 하면 되는데 불필요하게 여러번 중복되어 인증처리를 하게 된다.<br/>
이러한 문제를 해결하기 위해 한 번의 요청 당 한 번의 인증을 수행하는 OncePerRequestFilter를 사용한다.<br/>

```java
public abstract class OncePerRequestFilter implements Filter {

    @Override
    public final void doFilter(ServletRequest request, ServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
        // 요청 당 한 번만 실행되도록 보장하기 위한 중복 실행 체크
        if (shouldNotFilter((HttpServletRequest) request)) {
            filterChain.doFilter(request, response);
        } else {
            // doFilterInternal 메서드를 호출하여 실제 필터 로직 실행
            doFilterInternal(request, response, filterChain);
        }
    }

    protected abstract void doFilterInternal(
            ServletRequest request, ServletResponse response, FilterChain filterChain)
            throws ServletException, IOException;
    
    // 중복 실행 방지를 위한 shouldNotFilter 메서드 등을 정의할 수 있음.
    // ...
}

```
OncePerRequestFilter에서는 사용자가 doFilterInternal을 구현하도록 하고<br/>
내부적으로 doFilter을 수행하고 doFilterInternal을 수행하여 인증을 한 번만 할 수 있도록 한다.
