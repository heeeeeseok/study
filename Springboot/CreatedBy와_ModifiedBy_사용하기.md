# 1. BaseEntitiy 구현
```java
@Getter
@MappedSuperclass // 여러 객체/테이블에 공통으로 들어가는 정보들이 있을때, 해당 Column들을 해당 객체/테이블들에 쉽게 생성할 수 있게 해주는 애노테이션
@EntityListeners(AuditingEntityListener.class)
public class BaseEntity {
    @CreatedDate
    @Column(updatable = false)
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime modifiedAt;

    @CreatedBy
    private Long createdId;

    @LastModifiedBy
    private Long modifiedBy;
}
```

# 2. AuditorAware을 구현하는 클래스 생성
```java
@RequiredArgsConstructor
@Component // 클래스를 직접 Bean으로 등록하기 위한 애너테이
public class LoginUserAuditorAware implements AuditorAware<Long> {

    private final HttpSession httpSession;

    @Override
    public Optional<Long> getCurrentAuditor() {
        SessionUserDTO user = (SessionUserDTO) httpSession.getAttribute("user");
        if(user == null)
            return null;

        return Optional.ofNullable(user.getUserId());
    }
}
```
# 3. 
