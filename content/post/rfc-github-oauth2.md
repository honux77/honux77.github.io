+++
categories = ["programming"]
date = 2020-11-16T12:35:47Z
description = "RFC 그림은 너무 귀엽다."
draft = true
tags = ["javascript", "node", "oauth", "github"]
title = "RFC 읽고 GitHub Oauth2 인증 구현해 보기"

+++
최근 강의 준비를 위해 [RFC6749](https://tools.ietf.org/html/rfc6749)를 읽었다.

생각보다 설명이 잘 되어 있고 읽기가 편한 편이다.

시험 삼아 별도 모듈 없이 직접 node.js + express로 구현을 해 봤다. 다행히 잘 된다.

## 인증 과정 요약

1. **GitHub(Authentication Server)** 에서 제공하는 url을 통해 **사용자(resource owner)**는 **서비스(client)**가 scope로 미리 정의한 요청 권한을 직접 확인하고 grant한다. 결과물로 **authorization code**가 나온다.
2. 서비스는 callback URL을 통해 사용자로부터 전달받은 code에 client id, secret을 함께 묶어서 인증 서버로 보내면 **access token**을 얻을 수 있다.
3. 얻은 token을 이용해  'Authorization: bearer 토큰값' 헤더를 설정하고 `GET https://api.github.com/user` 요청을 하면 정상적으로 **GitHub(resource server)**로 부터 정보를 얻을 수 있다.

## 인증 과정

         +----------+
         | Resource |
         |   Owner  |
         |          |
         +----------+
              ^
              |
             (B)
         +----|-----+          Client Identifier      +---------------+
         |         -+----(A)-- & Redirection URI ---->|               |
         |  User-   |                                 | Authorization |
         |  Agent  -+----(B)-- User authenticates --->|     Server    |
         |          |                                 |               |
         |         -+----(C)-- Authorization Code ---<|               |
         +-|----|---+                                 +---------------+
           |    |                                         ^      v
          (A)  (C)                                        |      |
           |    |                                         |      |
           ^    v                                         |      |
         +---------+                                      |      |
         |         |>---(D)-- Authorization Code ---------'      |
         |  Client |          & Redirection URI                  |
         |         |                                             |
         |         |<---(E)----- Access Token -------------------'
         +---------+       (w/ Optional Refresh Token)
    
       Note: The lines illustrating steps (A), (B), and (C) are broken into
       two parts as they pass through the user-agent.
    
                      Authorization Code Flow (출처: RFC6749)

## 깃헙 소스

* [간단 예제 구현 저장소](https://github.com/honux77/oauth2-node)