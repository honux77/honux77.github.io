+++
categories = ["algorithm"]
date = 2020-11-06T01:56:58Z
description = "제목은 이상하지만 재미있는 문제"
tags = ["string", "kmp", "boj", "algorithm"]
title = "[알고리즘] BOJ 5525 IOIOI "

+++
## KMP를 이용한 문자열 패턴 매칭

[https://www.acmicpc.net/problem/5525](https://www.acmicpc.net/problem/5525 "https://www.acmicpc.net/problem/5525") 문제는 상당히 재미있는 문제였다.

### Try 1

언뜻 보면 단순 문자열 비교를 통해서 풀 수 있을 것 같은 문제라 그렇게 풀어 보았다.

생각해 보면 복잡도가 `O(n * m)` 이기 때문에 당연히 TE (시간초과) 가 발생한다.


```
using namespace std;

string pstr(int n) {
    string o = "IO";
    string ans = "";
    for (int i = 0; i < n; i++) {
        ans += o;
    }
    return ans + "I";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, l;
    int ans = 0;
    string s;
    cin >> n >> l;
    cin >> s;
    int psize = 2 * n + 1;
    string pn = pstr(n);
    
    for (int i = 0; i < s.size() - psize; i++) {
        if (s.substr(i, psize) == pn) ans++;        
    }

    cout << ans << "\n";
    return 0;
}
```

### Try 2

결국 문자열 비교의 정석 KMP를 변형해서 적용했다. 비교대상 문자열이 일정하기 때문에 원래의 KMP보다 구현이 쉽다. KMP는 종만북 20장 즈음에도 나왔던 것 같은데, 문자열 문제가 종종 코딩 테스트에도 나오므로 숙지하면 좋을 것 같다. 개인적으로 KMP 알고리즘은 어렵지 않은데 실패함수를 효율적으로 구현하는 게 더 어려운 느낌이다.

[KMP 참고링크](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)

```
using namespace std;

int match(string &s, int pos, int n, int jmp) {       
    int i = jmp; 
    for (;i < 2 * n + 1; i++) {
        if (i % 2 == 0 && s[pos + i] != 'I') return i;
        if (i % 2 == 1 && s[pos + i] != 'O') return i;        
    }
    return i;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;

    int i = 0;
    int ans = 0;
    int jmp = 0;

    while(i < s.size() - 2 * n + 1) {
        int w = match(s, i, n, jmp);
        if (w == 2 * n + 1) {
            ans++;
            i+= 2;
            jmp = 2 * n - 1;
        } else if (w == 0) {
            i++;
            jmp = 0;            
        } else {
            i+= w;
            jmp = 0;
        }        
    }

    cout << ans << "\n";
    return 0;
}

```

### Try 3

페이스북 매일코딩 그룹에서 H님과 J님의 코드를 보니 더 간단히 풀 수 있다는 것을 알았다. 

- [H님 소스](https://gist.github.com/jwvg0425/ca34f3472475d0ec9b3ec20bddeb6794)
- [J님 소스](https://www.acmicpc.net/source/share/95ca1c35e2534cc98c6cdd482c98dd71)

```
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    
    int ans = 0;

    for(int i = 0; i < s.size() - (2 * n  + 1); i++) {
        if (s[i] == 'I') {
            int p = 0;
            while (s[i + 1] == 'O' && s[i + 2] == 'I') {
                p++;
                i+=2;
            }
            if (p >= n) {
                ans += p - n + 1;             
            }
        }
    }
    
    cout << ans << "\n";
    return 0;
}

```

재밌는 문제를 풀어서 풀이를 정리해 봤다. 

오늘도 즐거운 코딩 라이프!
