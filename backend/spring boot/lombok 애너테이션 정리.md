## @Builder
    produce complex builder APIs
    @Builder는 class, contsrtuctor, method에 위치할 수 있다. 보통 class, constructor에 사용
    특정 필드가 build session에서 사용되지 않을 경우에는 @Builder.Defauilt 활용 가능

## @SuperBuilder
    부모와 자식 클래스 양쪽에 @SuperBuilder 애너테이션 추가.
    자식 클래스를 생성하면서 빌더를 통해 부모와 자식클래스의 필드 모두 작성 가능

## @NoArgsConstructor / @RequiredArgsConstructor / @AllArgsConstructor
    @NoArgsConstructor는 파라미터가 없는 생성자 생성.
    불가능하다면 (final fields 존재), 컴파일 에러 발생.
    @NoArgsConstructor(force = true)로 설정 시 final fields가 0 / false / null로 초기화됨.

    @RequiredArgsConstructor는 미리 초기화되지 않은 final field나 @NonNull로 지정된 feild를 초기화

    @AllArgsConstructor 어노테이션은 모든 필드 값을 파라미터로 받는 생성자를 생성

## @Data
    @ToString, @EqualsAndHashCode, @Getter / @Setter, @RequiredArgsConstructor 포함
    callsuper, includeFiledNames, exclude 등의 속성 사용 불가
    
## @Getter/ @Setter
    자동으로 default getter / setter 생성
    AccessLevel 지정 안하면 자동으로 public. [PUBLIC, PROTECTED, PACKAGE, PRIVATE, NONE] 사용 가능

## @ToString
    all non-static 필드들 출력. @ToString.Exclude 애너테이션으로 특정 필드 생략 가능
    callSuper 속성을 true로 설정하면, superclass의 toString의 출력 포함 가능
