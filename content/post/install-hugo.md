---
title: HUGO로 깃헙 블로깅하기
date: 2020-09-02T19:28:55.000+09:00
tags:
- blog
- hugo
- github
categories:
- blog
description: HUGO를 설치하고 개발 블로그를 운영하려고 합니다.

---
# HUGO로 깃헙 블로깅 하기

[HUGO](https://gohugo.io/)는 go 언어로 만들어진 static 웹 페이지 생성기이다.

네이버 개발자 정상혁님이 공유해주신 레트로 테마가 맘에 들어서 설치하였다.

## 설치

[퀵스타트](https://gohugo.io/getting-started/quick-start/)를 참고해서 설치한다.

맥, 윈도우, 리눅스, 도커 모두 간편하게 설치가 가능하다.

다만 맥은 brew, 윈도우는 chocolatey를 먼저 설치해야 한다.

### 맥

    brew install hugo

### windows

    choco install hugo -confirm

## 사이트 생성

my-blog라는 폴더를 생성하고 그 아래에 hugo를 셋업한다.

    hugo new site my-blog

## 테마 설치

맘에 드는 테마를 설치한다.

나는 hugo.386 테마에서 한글 폰트를 변경하고 코드 블록을 녹색으로 바꾼 테마를 적용하였다.

    cd  my-blog
    git init
    git submodule add https://github.com/honux77/hugo.386k themes/hugo.386k

## 환경 설정

최상위 폴더에 config.toml로 테마와 타이틀 등을 설정한다.

깃헙 블로깅을 위해서 `publishdir = "./docs/"`를 추가하고 기타 설정을 해 줬다.

    baseURL = "http://honux77.github.io/"
    languageCode = "ko-kr"
    title = "Honux BBS"
    theme = "hugo.386k"
    publishdir = "./docs/"
    
    [taxonomies]
       tag = "tags"
       category = "categories"
    
    [params]
        # The name to display as main title in the home page
        mainpagetitle = "HONUX.386"
    
        # The subtitle to display under the title in the home page
        mainpagesubtitle = "응답하라 호눅스 90!" 
 
> 이후에 GitHub Action을 연동하게 되면 publishdir이 root 디렉토리가 되므로 이 부분을 다시 주석처리해 주어야 한다.

## 첫 번째 글쓰기

    hugo new post/my-first-post.md

위 명령을 실행하면 content 폴더에 해당 파일이 생성된다.

파일 내용을 편집하자.

    ---
    title: "첫 번째 글"
    date: 2020-08-31T11:35:58+09:00
    tags: ["hello"]
    categories: ["잡담"]
    draft: false
    ---
    
    # Hello, Hugo
    
    ## 첫번째 글
    
    지인분이 공유해 주신 하이텔 스타일 테마가 맘에 들어서 글을 하나 올려봤다.

## 로컬 서버 실행 및 테스트

    hugo server -D

서버 실행 후에는 [http://localhost:1313](http://localhost:1313)으로 접속해서 확인할 수 있다.

로컬에서 최종적으로 글을 수정하자.

## 빌드

깃헙에 올리기 위해서는 빌드가 필요하다.

    hugo -D

빌드 후에는 `./docs` 폴더에 static 페이지들이 생성될 것이다.

## 깃헙에 올리기

깃헙에 올리는 방법은 여러가지가 있지만 간단하게 해 보자.

1. 내아이디.github.io 저장소 생성
2. HUGO 디렉토리에서 터미널을 열고 `git remote add origin 내저장소주소` 실행
3. add, commit, push

## 깃헙 설정

깃헙 저장소의 [설정 페이지](https://github.com/honux77/honux77.github.io/settings)에 가면 해당 저장소의 GitHub Pages 설정에서 브랜치와 폴더를 설정할 수 있다.

master 브랜치와 docs 폴더로 설정을 하고 저장한다.

## 확인

잠시 시간이 지나고 나면 `https://내아이디.github.io`로 접속이 되는 것을 확인할 수 있다.

## 참고 링크

* [퀵스타트](https://gohugo.io/getting-started/quick-start/)
* [휴고 설치](https://gohugo.io/getting-started/installing/)
* [hugo.386 테마](https://themes.gohugo.io//theme/hugo.386/)
* [hugo.386 한글 테마](https://github.com/honux77/hugo.386k)
* [설정 파일 예제](https://gitlab.com/maxlefou/hugo.386/-/blob/master/exampleSite/config.toml)
* [태그 및 카테고리 설정 설정](https://discourse.gohugo.io/t/how-to-add-tag-and-category/3202)

### 글쓴이

호눅스: 소프트웨어 교육기업 [코드스쿼드](https://codesquad.kr)를 운영하고 있습니다.