## ./gradlew build 무한로딩 현상
    EC2에서 git clone으로 서버 파일을 clone후에
    ./gradlew build 실행 시 76%에서 무한 로딩 현상 발생

    무한 로딩 문제는 메모리 부족 문제일 수도 있다고 했다.
    EC2 프리티어에서 사용 가능한 t2.micrio의 램이 1GB밖에 되지 않아 메모리 과부화로 인해 무한로딩

## 해결 방법 : Swap 메모리 사용
    Swap 메모리 : RAM의 메모리가 부족하므로, 리눅스의 HDD 공간을 RAM처럼 사용하는 것
    이를 통해 부족한 RAM을 증설한 것처럼 사용할 수 있다.

- dd 명령어를 통해 swap 메모리를 할당한다. (2GB)
```bash
$ sudo dd if=/dev/zero of=/swapfile bs=128M count=16
```
- 스왑 파일에 대한 읽기 및 쓰기 권한을 업데이트
```bash
$ sudo chmod 600 /swapfile
```
- Linux 스왑 영역 설정
```bash
$ sudo mkswap /swapfile
```
- 스왑 공간에 스왑파일을 추가하여 스왑파일을 즉시 사용할 수 있도록 만든다.
```bash
$ sudo swapon /swapfile
```
- /etc/fstab 파일을 편집하여 부팅 시 스왑 파일을 활성화한다.
```bash
$ sudo vi /etc/fstab
```
- 파일 끝에 다음 줄을 새로 추가하고 파일을 저장한 뒤 종료한다.
```bash
/swapfile swap swap defaults 0 0
```

출쳐 : [https://sundries-in-myidea.tistory.com/102]

