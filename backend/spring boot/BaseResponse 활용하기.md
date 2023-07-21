# ResponseCode 작성
```java
@Getter
@RequiredArgsConstructor
public enum ResponseCode {
    OK(0, HttpStatus.OK, "Ok"),

    // user 관련
    SIGNUP_WITH_DUPLICATED_EMAIL(1000, HttpStatus.BAD_REQUEST, "중복된 이메일 입니다"),
    LOGIN_WITH_WRONG_EMAIL(1001, HttpStatus.BAD_REQUEST, "잘못된 이메일 입니다"),
    LOGIN_WITH_WRONG_PASSWORD(1002, HttpStatus.BAD_REQUEST, "비밀번호가 틀렸습니다"),

    ...

    private final Integer code;
    private final HttpStatus httpStatus;
    private final String message;

    public String getMessage(Throwable e) {
        return this.getMessage(this.getMessage() + " - " + e.getMessage());
        // 결과 예시 - "Validation error - Reason why it isn't valid"
    }

    public String getMessage(String message) {
        return Optional.ofNullable(message)
                .filter(Predicate.not(String::isBlank))
                .orElse(this.getMessage());
    }

    @Override
    public String toString() {
        return String.format("%s (%d)", this.name(), this.getCode());
    }
}
```

# ResponseException 작성

```java
@Getter
public class ResponseException extends RuntimeException{
    private final ResponseCode errorCode;

    public ResponseException(ResponseCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }
}
```

# BaseResponse<T> 작성

```java
@Getter
@ToString
public class BaseResponse<T> {

    private final Boolean success;
    private final Integer code;
    private final String message;
    private final T data;

    public BaseResponse(T data) {
        this.success = true;
        this.code = ResponseCode.OK.getCode();
        this.message = ResponseCode.OK.getMessage();
        this.data = data;
    }

    public BaseResponse(ResponseCode errorCode) {
        this.success = false;
        this.code = errorCode.getCode();
        this.message = errorCode.getMessage();
        this.data = null;
    }
}
```

# 사용 예시

``` java
@PostMapping("/login")
    public BaseResponse<LoginResponseDto> login(@RequestBody LoginRequestDto loginReq) {
        try {
            LoginResponseDto response = userService.login(loginReq);
            return new BaseResponse<>(response);
        } catch (ResponseException e) {
            LOGGER.info(e.getMessage());
            return new BaseResponse<>(e.getErrorCode());
        } catch (Exception e) {
            LOGGER.info(e.getMessage());
            return  new BaseResponse<>(ResponseCode.INTERNAL_ERROR);
        }
    }
```

