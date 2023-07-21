# DTO란?
> DTO(Data Transfer Object)란 계층간 데이터 교환을 위해 사용하는 객체(Java Beans)

# MVC 패턴
> MVC 패턴은 어플리케이션을 개발할 때 그 구성 요소를 Model과 View 및 Controller 등 세 가지 역할로 구분하는 디자인 패턴

> 비지니스 로직(Model)과 UI영역(View)은 서로의 존재를 인지하지 못하고, Controller가 중간에서 Model과 View의 연결을 담당

> Controller는 View로부터 들어온 사용자 요청을 해석하여 Model을 업데이트 하거나 Model로부터 데이터를 받아 View로 전달하는 작업 등을 수행
  
> MVC 패턴의 장점은 Model과 View를 분리함으로써 서로의 의존성을 낮추고 독립적인 개발을 가능하게 함

> Cotroller는 View와 도메인 Model의 데이터를 주고 받을 때 별도의 DTO를 주로 사용
> 도메인 객체를 직접 전달할 수 있지만, 민감한 도메인 비지니스 기능이 노출될 수 있으며 Model과 View 사이에 의존성이 생김

# 도메인 Model을 바로 넘겨주었을 때의 문제점?
> 도메인 Model의 모든 속성이 외부에 노출됨
 
> 화면마다 사용하는 Model의 정보는 상이하지만, Model객체는 UI에서 사용하지 않을 불필요한 데이터까지 포함함
 
> UI 계층에서 Model의 매서드를 호출하거나 상태를 변경시킬 위험이 존재함
 
> Model과 View가 강하게 결합되어, View의 요구사항 변화가 Model에 영향을 끼치기 쉬움

> 또한 Entitiy 속성이 변경되면, View가 전달받을 JSON및 프론트엔드 JS 코드에도 변경을 유발함

# DTO 사용시
> 앞서 말한 문제점을 해결할 수 있음. 도메인 Model을 캠슐화하고, UI 화면에서 사용하는 데이터만 선택적으로 보낼 수 있음

> 클라이언트 요청에 포함된 데이터를 담아 서버 측에 전달하고, 서버 측의 응답 데이터를 담아 클라이언트에 전달하는 계층간 전달자 역할을 함
