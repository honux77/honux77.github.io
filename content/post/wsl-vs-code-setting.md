---
title: "WSL2와 VS 코드를 이용한 개발환경 설정"
date: 2020-09-24T10:28:21+09:00
draft: false
tags: ["windows", "wsl2", "vscode"]
categories: ["개발팁"]
description: "윈도우에서도 가벼운 코딩이 가능해졌다."

---

WSL2가 나온 이후로 윈도우에서 간단한 개발환경 세팅하기가 너무 좋아졌다.

윈도우즈 터미널로 ubuntu zsh을 바로 띄울 수 있고, vscode의remote 기능을 이용하면 네이티브인 것 처럼 개발이 가능하다.

## Git Bash 설치

WSL보다 가볍게 bash를 사용할 수 있으므로 git 작업과 간단한 작업을 할 때 유용하다. https://git-scm.com/ 에서 설치 가능

## 윈도우즈 터미널 설치

[MS 스토어](https://www.microsoft.com/ko-kr/p/windows-terminal/9n0dx20hk701)를 이용해서 설치하는 것이 가장 편하다.

설치 후에는 윈도우즈 터미널에서 파워셸, 명령창, git-bash, WSL 모두 띄우게 설정하면 편하게 사용할 수 있다.

### 참고: 터미널에 git-bash 추가

아래 내용은 내가 사용하고 있는 내용인데 터미널 설정 파일에 이 부분을 추가하면 된다. 자세한 내용은
[스택 오버플로 링크](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal) 를 참고.

```
{
    "acrylicOpacity" : 0.75,
    "background" : "#000000",
    "closeOnExit" : true,
    "colorScheme" : "Campbell",
    "commandline" : "\"%PROGRAMFILES%\\git\\bin\\bash.exe\" --login -i -l",
    "cursorColor" : "#FFFFFF",
    "cursorShape" : "bar",
    "fontFace" : "Consolas",
    "fontSize" : 14,
    "guid" : "{00000000-0000-0000-0000-000000012345}",
    "historySize" : 9001,
    "icon" : "%PROGRAMFILES%\\git\\mingw64\\share\\git\\git-for-windows.ico",
    "name" : "Git Bash",
    "padding" : "0, 0, 0, 0",
    "snapOnInput" : true,
    "useAcrylic" : true
    }
}
```

## WSL2 설치

검색을 통해 설치했는데 중간에 여러번 오류가 발생했다. 오류 메시지 검색 등을 통해 해결하자.
잘 안 된다면 스토어에서 ubuntu 20.04 최신버전을 설치해 볼 것.

- [WSL 2 설치 참고 링크](https://www.44bits.io/ko/post/wsl2-install-and-basic-usage)

## VS CODE 연동

윈도우즈 터미널을 통해 Ubuntu를 열고 원하는 디렉토리로 이동해서 `code ./` 명령을 입력하면 필요한 확장 프로그램을 설치하고 쉽게 VS Code 연동이 된다.

- [vs code + wsl2 가이드](https://simongs.tistory.com/59)

## 소감

알고리즘 문제를 풀 때 cpp을 사용하려면 조금 불편했는데, vs code + wsl 연동으로 개발환경을 간단히 설정하면 매우 편하다. 굿!
