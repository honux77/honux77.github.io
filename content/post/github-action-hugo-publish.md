+++
categories = []
date = 2020-09-29T16:33:56Z
description = "깃헙 액션이 너무 좋다."
tags = []
title = "GitHub Action으로 Hugo Publish 쉽게 하기"

+++
# GitHub Action으로 Hugo Publish 쉽게 하기

## publish.yml 생성

- 아래 내용으로 `.github/workflws` 아래에 publish.yml을 생성한다.

```
name: github pages

on:
  push:
    branches:
      - master  # Set a branch to deploy

jobs:
  deploy:
    runs-on: ubuntu-18.04
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.75.1'
          # extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

## 저장소 설정

[배포를 위한 저장소 설정](https://github.com/peaceiris/actions-gh-pages#%EF%B8%8F-first-deployment-with-github_token) 을 참고해서 deploy key와 secret key를 설정한다.

### 공개키 및 비밀키 생성

```
ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f gh-pages -N ""
```

`gh-pages.pub`는 공개키이고 `gh-pages`는 비밀키이다.

### 배포키 등록

공개키 파일의 내용을 복사해서 배포 키에 붙여 넣는다. 이름은 적당히 지어주자.

### 비밀키 등록

비밀키도 등록한다. 이름은 `ACTIONS_DEPLOY_KEY` 로 하고 비밀키 내용을 붙여 넣는다.

## 최초 배포후 설정

master 브랜치에 커밋하고 push를 한다. 설정이 성공적으로 되었다면 `gh-pages` 브랜치가 만들어지고 정적 페이지들이 있는 것을 확인할 수 있다.

이후 깃헙 저장소 설정 - GitHub Pages 탭에서 gh-pages 브랜치와 root 폴더를 선택해 준다.

## 참고링크

- [GitHub Actions Hugo](https://github.com/peaceiris/actions-hugo)
- [배포를 위한 저장소 설정](https://github.com/peaceiris/actions-gh-pages#%EF%B8%8F-first-deployment-with-github_token)