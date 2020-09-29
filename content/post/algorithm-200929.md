---
title: "알고리즘 - BOJ 10814 나이순 정렬"
date: 2020-09-29T13:13:00+09:00
draft: false
tags: ["algorithm", "boj", "silver"]
categories: ["algorithm"]
description: "cpp에서 stable_sort()는 안정 정렬이다."
---

## BOJ 

[BOJ 10814 나이순 정렬](https://www.acmicpc.net/problem/10814) 문제는 간단한 정렬문제이다.

다만 기본 정렬인 퀵정렬은 불안전 정렬이기 때문에 안정정렬을 사용해야 한다.

## 실패 분석

- 출력이 많은데 endl을 사용하면 시간초과가 발생한다.
- 그 사실을 모르고 복잡도 때문인지 알고 카운팅 소트를 구현해서 사용했다.

## 안정 정렬 구현 코드

```
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
using i64 = long long int;

struct People {
        int age;
        string name;
};

bool cmp(const People &a, const People &b) {
        return a.age < b.age;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
        vector <People> a(n);
        for (int i = 0; i < n; i++) {
                People p;
                cin >> p.age >> p.name;
                a[i] = p;
        }
        stable_sort(a.begin(), a.end(), cmp);

        for (int i = 0; i < n; i++) {
                cout << a[i].age << " " << a[i].name << '\n';
        }
    return 0;
}%   
```

## 카운팅 소트 구현 코드

```
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
using i64 = long long int;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
        vector <vector <string>> v(201);

        for (int i = 0; i < n; i++) {
                int age;
                string name;
                cin >> age >> name;
                v[age].push_back(name);
        }

        for (int i = 1; i <= 200; i++) {
                if (v[i].size() != 0) {
                        for (auto &name: v[i]) {
                                cout << i << " " << name << "\n";
                        }
                }
        }
    return 0;
}

```

### 난이도

- 체감 난이도 2점. 쉬운 편이다.
- BOJ 난이도: 실버 5. 쉬운 편
