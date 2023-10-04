### git workflow
- 브랜치를 어떻게 사용할 지에 대한 규칙을 workflow라 한다

### Git flow
- 브랜치의 역할이 명확하고 대규모 프로젝트에 적합
- 메인 브랜치: master, develop
  - master
    - 제품으로 출시하는 브랜치, 실제 배포 중인 상용 버전
  - develop
    - 다음 출시 버전을 개발하는 브랜치
    - 실제 작동 중인 버전의 다음 버전을 개발하기 위한 메인 스트림 
- 보조 브랜치: feature, release, hotfix
  - feature
    - 기능을 개발하는 브랜치
    - develop 브랜치에서 뻗어 나와 다시 develop 브랜치로 합쳐진다
    - 실제 개발 시 가장 많이 사용하는 브랜치
  - release
    - 새로운 버전을 배포하기 위한 브랜치, QA 용도
    - 주로 버그를 수정하는 디버깅만 커밋
  - hotfix
    - 상용 제품에서 버그가 발생 시 처리하는 브랜치
    - 버그 픽스를 위한 브랜치로 디버깅만 커밋, 보통 일회성으로 사용
   
### Github flow
- 하나의 메인 브랜치인 master 브랜치를 중점으로 운용하며 pull requset를 활용하는 방식
- 보통 feature 브랜치를 원격 저장소에 저장하여 운용

### Gitlab flow
- master와 develop 2개의 메인 브랜치로 관리
- 항상 최신 버전의 버전을 유지하지 않아도 되며 배포 버전과 개발 버전을 따로 둘 수 있다는 장점
- develop 브랜치는 github flow의 develop 브랜치 역할을 한다
