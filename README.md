# ✏️ 리뷰 서비스앱 Review Spot

![readme_mockup2](https://github.com/dedel009/review-spot/blob/master/title_image.jpg?raw=true)

- 배포
  - 프론트 URL : https://review-spot.vercel.app/reviews
  - 백엔드 swagger URL : http://3.39.234.40/swagger/
  - 백엔드 admin URL : https://3.39.234.40/admin/
- 협업 툴
  - 노션 URL : https://www.notion.so/Review-Spot-09666bbf65314932b8f01f0c960cbf2a
    

<br>

## 프로젝트 소개

- Review Spot은 다양한 사람들이 여러 물건을 사용하고 리뷰를 남기는 사이트입니다.
- 다양한 물건을 사용한 경험을 공유해주세요!👍

<br>

## 팀원 구성

<div align="center">

|                                                           **김도윤(INFP)**                                                            |                                                           **김호현(ESFP)**                                                            |                                                       **김창권(ISFJ)**                                                        |                                                         **유종철(ISFJ)**                                                          |
| :-----------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://avatars.githubusercontent.com/u/57212041?v=4" height=150 width=150> <br/> @dedel009](https://github.com/dedel009/) | [<img src="https://avatars.githubusercontent.com/u/122351733?v=4" height=150 width=150> <br/> @Khohyeon](https://github.com/Khohyeon) | [<img src="https://avatars.githubusercontent.com/u/99378862?v=4" height=150 width=150> <br/> @Kevin](https://github.com/oggn) | [<img src="https://avatars.githubusercontent.com/u/51194504?v=4" height=150 width=150> <br/> @Logan](https://github.com/whdcjf96) |

</div>

<br>

## 1. 개발 환경

- Front : Next 14.2.5, React ^18, Typescript ^5, Node ^20
- Back-end : Django 5.0.7, Python 3.12.3
- 버전 및 이슈관리 : Github, Github Issues, Github Project
- 협업 툴 : Notion, gather
- IDE : Pycharm, vsCode
- 서비스 배포 환경 : GCP를 사용한 ubuntu 서버(nginx, gunicorn, django) / 무료 기간 만료로 인해 AWS 클라우드 서버로 이전(도커 컴포즈를 이용해 환경세팅)
  <br>

## 2. 채택한 개발 기술과 브랜치 전략

### Nextjs, Tailwind

- Next
  - 컴포넌트화를 통해 추후 유지보수와 재사용성을 고려했습니다.
  - App 라우팅을 사용하여 폴더구조와 파일 기반의 라우팅을 채택하였으며, RSC와 RCC의 사용을 적절히 조합하여 SEO 개선을 고려했습니다.
- Tailwind
  - 조건부 스타일링을 활용하여 상황에 맞는 스타일을 적용할 수 있었습니다.
  - 유틸리티 클래스 기반의 접근 방식을 통해 스타일링 속도가 빨라지고, 불필요한 CSS 코드를 줄일 수 있었습니다.
  - 클래스 네이밍에 대한 고민 없이 직관적인 Tailwind CSS의 클래스를 사용하여 개발 비용을 절약했습니다.

### Django, PostgreSQL

- Django
  - 장고 프레임워크를 사용하면 짧은 시간안에 애플리케이션을 구축할 수 있기때문에 사이드 프로젝트에 적합하다고 판단하였습니다.
    - 장고에서 기본적으로 제공하는 관리자 페이지를 통해 백엔드 구조를 쉽게 파악할 수 있고, 쉽게 데이터를 수정, 삭제 가능합니다.
    - 개발 시 자동으로 코드 변경을 감지하여 재부팅해줌으로써 시간을 절약할 수 있습니다.
  - 파이썬을 사용하기 때문에 추후 데이터 수집, 업무 자동화 등 파이썬 라이브러리를 적극 활용하여 개발할 수 있습니다.
  - 기본적으로 ORM을 제공해주기때문에 SQL 쿼리를 직접 작성하지 않고도 스키마를 생성, 수정 등 할 수 있기때문에 DB 세팅에 유리합니다.
  - DRF의 CBV 구조를 사용함으로써 코드의 재사용성을 높였고, 보다 유연하게 커스터마이징하여 개발하였습니다.
- PostgreSQL
  - 장고는 PostgreSQL의 고유한 기능들을 최대한 활용하고 이를 쉽게 사용할 수 있도록 설계되었습니다.
  - 장고와 PostgreSQL 모두 넓은 커뮤니티를 보유하고 있기때문에 참고할 문서가 많습니다.
  - PostgreSQL에서 지원하는 복잡한 데이터 처리와 트랜잭션 관리를 장고의 ORM을 통해 쉽게 접근하고 구현할 수 있습니다.

### 브랜치 전략

- Git-flow 전략을 기반으로 master, develop 브랜치와 feature 보조 브랜치를 운용했습니다.
- master, develop, Feat 브랜치로 나누어 개발을 하였습니다.
  - **master** 브랜치는 배포 단계에서만 사용하는 브랜치입니다.
  - **develop** 브랜치는 개발 단계에서 git-flow의 master 역할을 하는 브랜치입니다.
  - **Feat** 브랜치는 기능 단위로 독립적인 개발 환경을 위하여 사용하고 merge 후 각 브랜치를 삭제해주었습니다.
- commit 전략
  - 이슈 라벨명:커밋내용(#이슈번호)

<br>

## 3. 프로젝트 구조
초기에는 프론트와 백엔드 소스를 한 레포에서 관리하였는데, 프론트에서 버셀에 배포하는 과정에서 문제점이 발생, 서버 실행 시 디렉토리 이동 등 번거로움이 많아 따로 관리를 하도록 변경
```
├── README.md
└── review_spot_backend
     ├── ...

```

<br>

## 4. 역할 분담

### 🍀김도윤(Backend Developer)

- **기능**
  - 전체적인 백엔드 API 개발 및 아키텍처 설계, 배포 서버 구축 등

<br>

### 💪유종철(Frontend Developer)

- **기능**
  - 팔로우 & 언팔로우, 로그아웃, 하단 모달창, 댓글 삭제, 게시글 삭제, 상품 삭제, 사용자 게시글 앨범형 이미지, 탑 배너 뒤로가기 버튼, Alert 모달

<br>

## 5. 개발 기간 및 작업 관리

### 일정 관련 히스토리

- 전체 개발 기간(2달) : 2025-03-29 ~ 미정
- 주제 회의 : 미정
- 기획 회의 : 미정
- 기능 구현 : 미정

<br>

### 작업 관리

- GitHub Projects와 Issues를 사용하여 진행 상황을 공유했습니다.
- 주간회의를 진행하며 작업 순서와 방향성에 대한 고민을 나누고 GitHub Wiki에 회의 내용을 기록했습니다.

<br>

## 6. 신경 쓴 부분

- [접근제한 설정](https://github.com/likelion-project-README/README/wiki/README-6.%EC%8B%A0%EA%B2%BD-%EC%93%B4-%EB%B6%80%EB%B6%84_%EC%A0%91%EA%B7%BC%EC%A0%9C%ED%95%9C-%EC%84%A4%EC%A0%95)

- [Recoil을 통한 상태관리 및 유지](https://github.com/likelion-project-README/README/wiki/README-6.%EC%8B%A0%EA%B2%BD-%EC%93%B4-%EB%B6%80%EB%B6%84_Recoil%EC%9D%84-%ED%86%B5%ED%95%9C-%EC%83%81%ED%83%9C%EA%B4%80%EB%A6%AC-%EB%B0%8F-%EC%9C%A0%EC%A7%80)

<br>

## 7. 페이지별 기능

<br>

## 8. 트러블 슈팅

<br>

## 9. 개선 목표

<br>

## 10. 프로젝트 후기

### 🍀김도윤(Backend Developer)

<br>

### 💪유종철(Frontend Developer)
