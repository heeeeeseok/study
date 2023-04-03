- # [Layouts](https://developer.android.com/develop/ui/views/layout/declaring-layout#java)

  - ### layout 상의 모든 요소들은 **View** 와 **ViewGroup** 객체의 계층구조 안에서 만들어진다
    - #### **View** : 사용자가 볼 수 있고 상호작용이 가능한 요소 (Button, TextView, ... )
    - #### **ViewGroup** : View와 ViewGroup의 layout 구조를 위한 invisible container (LinearLayout, ... )
    

  ![이미지](https://developer.android.com/static/images/viewgroup_2x.png)

  - ## layout의 선언
    
    - ## 1. XML 이용
    
       - 각 layout 파일은 하나의 root element만을 포함해야 함
       
       - **res/layout/** 디렉토리 상에 저장
       
       - **Activity.onCreate()** 콜백의 **setContentView()** 를 통해 View들을 load 함
        ```java
        public void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.main_layout);
        }
        ```
      - ## Layout Parameters
      
        ![이미지](https://developer.android.com/static/images/layoutparams.png)
        
        - XML 속성 중 layout_ 으로 시작하는 속성들은 위치한 ViewGroup에 맞는 **layout parameter** 들을 가진다
        
        - 모든 ViewGroup 클래스는 nested 클래스인 **ViewGroup.LayoutParams** 를 implemnets 한다
        
          이 서브 클래스는 자식 view에 대한 property types의 정의를 포함한다
          
          모든 자식 view들은 부모 ViewGroup에 맞는 LayoutParams를 정의해야 함

      
    - ### 2. runtime에 layout 인스턴스화

      ```java
      public void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          
          LinearLayout rootLinear = new LinearLayout(this);
          rootLinear.setOrientation(LinearLayout.VERTICAL);
          
          ContentFrameLayout.LayoutParams rootLP =
              new ContentFrameLayout.LayoutParams(
                  ContentFrameLayout.LayoutParams.MATCH_PARENT,
                  ContentFrameLayout.LayoutParams.MATCH_PARENT);
                  
          rootLP.setMargins(20, 20, 20, 20);
        }
      ```

    
