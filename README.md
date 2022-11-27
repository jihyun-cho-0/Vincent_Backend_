# 이미지 변환 서비스
**프론트엔드 Gti Hub** https://github.com/Carrotww/Vincent_Frontend

## 팀 소개

### LOL(Laugh Out Loud) 즐겁게 코딩을 하자

## 작업 분배

- 로그인/회원가입 `하경수님`
- 머신러닝 `유형석님` `조지현님`
- 개인 페이지 `김준식님`
- 이미지 필터 목록 페이지 `이태은님`
- 게시글 `조지현님`
- 프론트엔드 `이태은님`

## 서비스 소개

해당 서비스는 다양한 이미지 필터를 제공하여
사용자가 업로드한 이미지를 사용자가 선택한 필터 이미지 스타일에 맞게 변형해
새로운 이미지를 도출합니다.

만약 원하는 필터가 존재하지 않을 때는 사용자가 직접 필터로 사용할 이미지를 업로드하고
필터 게시판에 등록하여 사용할 수 있습니다.

추가적으로 결과값 이미지를 활용하여 게시글과 댓글을 작성하는 커뮤니티 공간을 제공합니다.

### 머신러닝 구현 방식

[‘Neural-Style-Transfer’](https://github.com/deepeshdm/Neural-Style-Transfer)라는 사전에 학습된 모델을 가져와 적용

## 개발환경

**개발언어** `JavaScript` `python 3.8`

**머신러닝 모델** `Neural-Style-Transfer`

**데이터베이스** `SQLite3`

**개발환경** `djangorestframework 3.14.0`

## 주요 서비스 흐름도

1. 회원가입
2. 로그인
3. 메인(게시글 목록 페이지)에서 ‘이미지 업로드 버튼’ 클릭
4. 모달창 출력
    
    a. 기존 필터 사용 시
    
    - 컨텐츠 이미지 업로드
    - 필터 선택
    - 컨텐츠 이미지, 선택한 필터 이름을 back으로 전송
    
    b. 기존 필터를 사용하지 않고 사용자가 필터 추가하여 사용 시
    
    - 컨텐츠 이미지 업로드
    - 필터로 사용할 스타일 이미지 업로드
    - 위의 2개 이미지를 back으로 전송
5. 머신러닝 실행
6. 머신러닝 결과값을 front로 전송
7. 머신러닝 결과값을 확인하는 4번 모달창에서 ‘글 작성하기 버튼’ 클릭 시 제목, 내용 작성 칸 출력
8. 작성된 제목, 내용을 back으로 전송한 뒤 머신러닝 결과 이미지와 함께 DB에 저장
9. DB에 저장 후 메인(게시글 목록 페이지)로 이동

## 부가기능

- 메인(게시글 목록 페이지)에서 ‘필터 목록 보기’ 텍스트 클릭 시 필터 이미지 목록을 출력
- 메인(게시글 목록 페이지)에서 이미지 클릭 시 해당 게시글 상세보기
- 메인(게시글 목록 페이지)에서 최신순, 좋아요 순으로 게시글 정렬 가능
## Wireframe
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a92d2388-2bfe-4d86-bbfe-d7dc6e945eeb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221127T134959Z&X-Amz-Expires=86400&X-Amz-Signature=ed6970d380e943125f23b8a787efc6eafce50952d4cde1cd0b6cfbc38711798c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)


    
## API
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb437c1c-1560-4187-89ed-a77f0d291fb5/www.notion.so_b80d36a514ff4702ace51b43ce0903ca_v6672750d03804c9fb3dc825ee595a700_%EB%B3%B5%EC%82%AC.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221127T140736Z&X-Amz-Expires=86400&X-Amz-Signature=80649a9848a3a088ec1b4235d6fc6c5e60b423aa5eeb4722a44977d3fafc74ed&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22www.notion.so_b80d36a514ff4702ace51b43ce0903ca_v%253D6672750d03804c9fb3dc825ee595a700%2520%25EB%25B3%25B5%25EC%2582%25AC.png%22&x-id=GetObject)


## ERD
![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/42ef692a-3d31-40f2-9d6d-7be466102398/A6.LOL___%EC%9C%A0%ED%99%94%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221127T134640Z&X-Amz-Expires=86400&X-Amz-Signature=df4098ff11590ef19c63758a131411c99ed5ba2064fa91396d41eb1702d086cc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22A6.LOL%2520_%2520%25EC%259C%25A0%25ED%2599%2594%25ED%2594%2584%25EB%25A1%259C%25EC%25A0%259D%25ED%258A%25B8.png%22&x-id=GetObject)
    


    
    
## 시연영상

https://vimeo.com/775485950
