## @Controller vs @RestController
### @Controller
      전통적인 Spring MVC의 컨트롤러로 주로 View를 반환하기 위해 사용
 ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb3McJC%2Fbtrx1IGcnGs%2F2iHFmw3bbqasfCJzwCKYuK%2Fimg.png)
 ***
 - 1. Client가 URI 형식으로 웹 서비스에 요청을 보낸다.
 - 2. DispatcherServlet이 요청을 처리할 대상을 찾는다.
   
      스프링 프레임워크가 제공하는 Servlet 클래스.   
      클라이언트의 요청을 처음으로 받는 클래스.   
      Dispatcher가 받은 요청을 HandlerMapping으로 넘긴다.   
      HandlerMapping에서 Handler를 결정한다.
      
 - 3. HandlerAdpater를 통해 요청을 Controller로 위임한다.
    
 - 4. 결정된 Controller는 요청을 처리하고 ViewName을 반환한다.
    
 - 5. DispatcherServlet은 ViewResolver를 통해 ViewName에 해당하는 View를 찾아 반환한다.
   
      Controller가 반환한 뷰의 이름으로부터 View를 랜더링하기 위해서는 ViewResolver가 사용된다.
***

  Spring MVC 컨트롤러를 사용하면서 Data를 반환해야 하는 경우도 있다.
  
  컨트롤러에서는 데이터를 반환하기 위해 @ResponseBody 어노테이션을 활용해야 한다. 
  
  이를 통해 Controller도 Json 형태로 데이터를 반환 할 수 있다.

  컨트롤러를 통해 객체를 반환할 때 viewResolver 대신에 HttpMessageConverter가 동작한다.

  Spring은 클라이언트의 HTTP Accept 헤더와 서버의 반환 타입 정보를 활용해 적절한 Converter을 선택한다

## @RestController
    @RestController는 @Controller에 @ResponseBody가 추가된 것.
    주 용도는 Json형태로 객체 데이터를 반환하는 것
    데이터를 응답으로 제공하는 REST API를 개발할 때 주로 사용한다.
    

출처 : [https://mangkyu.tistory.com/49]
