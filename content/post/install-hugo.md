---
title: "HUGO로 깃헙 블로깅하기"
date: 2020-09-02T19:28:55+09:00
draft: false
tags: ["HUGO", "blog", "GitHub"]
categories: ["HUGO"]
---

# Hugo로 깃헙 블로깅 하기

HUGO(https://gohugo.io/)는 go 언어로 만들어진 static 웹 페이지 생성기이다. 

지인이신 정상혁님이 공유한 레트로 테마가 맘에 들어서 설치하기로 마음 먹었다.

## 설치

https://gohugo.io/getting-started/quick-start/ 을 참고해서 설치하면 된다.

맥, 윈도우, 리눅스, 도커 모두 간편하게 설치가 가능하다.

다만 맥의 brew, 윈도우는 chocolatey를 먼저 설치해야 한다.

### 맥

```
brew install hugo
```

### windows

```
choco install hugo -confirm
```

## 사이트 생성

my-blog라는 폴더를 생성하고 그 아래에 hugo를 셋업한다.

```
hugo new site my-blog
```

## 테마 설치

```
cd  my-blog
git init
git submodule add https://github.com/honux77/hugo.386k themes/hugo.386k
```

## 환경 설정

최상위 폴더에 config.toml로 테마와 타이틀 등을 설정한다.

깃헙 블로깅을 위해서 `publishdir = "./docs/"`를 추가하고 기타 설정을 해 줬다.

```
baseURL = "http://honux77.github.io/"
languageCode = "ko-kr"
title = "Honux Blog"
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

```

## 첫 번째 글쓰기

```
hugo new post/my-first-post.md
```

위 명령을 실행하면 content 폴더에 해당 파일이 생성된다. 

파일 내용을 편집하자.

```
---
title: "첫 번째 글"
date: 2020-08-31T11:35:58+09:00
tags: ["hello"]
categories: ["잡담"]
draft: false
---

# Hello, Hugo

## 첫번째 글

지인분이 공유해 주신 하이텔 시절 테마가 맘에 들어서 글을 하나 올려봤다.
```

## 로컬 서버 실행 및 테스트

```
hugo server -D
```

서버 실행 후에는 <http://localhost:1313>으로 접속해서 확인할 수 있다.

로컬에서 최종적으로 글을 수정하자.

## 빌드

깃헙에 올리기 위해서는 빌드가 필요하다.

```
hugo -D
```

빌드 후에는 `./docs` 폴더에 static 페이지들이 생성될 것이다.

## 깃헙에 올리기

깃헙에 올리는 방법은 여러가지가 있지만 간단하게 해 보자.

1. 내아이디.github.io 저장소 생성
2. `git remote add origin 내저장소주소` 실행
3. add, commit, push

## 깃헙 설정

깃헙 저장소의 설정 페이지(https://github.com/honux77/honux77.github.io/settings)에 가면 해당 저장소의 GitHub Pages 설정에서 브랜치와 폴더를 설정할 수 있다. 

master 브랜치와 docs 폴더로 설정을 하고 저장한다.

## 확인 

잠시 시간이 지나고 나면 `https://내아이디.github.io`로 접속이 되는 것을 확인할 수 있다.

## 참고 링크

- https://gohugo.io/getting-started/quick-start/
- https://gohugo.io/getting-started/installing/
- https://themes.gohugo.io//theme/hugo.386/
- https://gitlab.com/maxlefou/hugo.386/-/blob/master/exampleSite/config.toml
- https://discourse.gohugo.io/t/how-to-add-tag-and-category/3202

### 글쓴이

소프트웨어 교육기업 코드스쿼드(https://codesquad.kr)를 운영하고 있습니다.
