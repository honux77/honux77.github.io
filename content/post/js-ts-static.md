+++
categories = ["programming"]
date = 2020-12-15T16:11:07Z
description = "JS에서 static method와 static 변수는 어떻게 선언하면 될까요?"
tags = ["typescript", "javascript"]
title = "JS 클래스와 TS static 키워드에 대한 짧은 고찰"

+++
요즘 인프런 캡틴 팡요님의 TS강의를 듣고 있다가 생각나서 짧게 정리해 보았다.

예전에 ES6의 클래스 문법을 사용하면서, 기존 자바에서 사용하던 static 메소드와 static 변수를 사용하고 싶었는데, 잘 되지 않았던 기억이 있었다.

이 문제를 해결하기 위한 아이디어가 갑자기 떠올랐는데, TS로 코딩을 하고 컴파일을 해서 생성된 코드를 보는 것이다!

먼저 TS에는 당연히 static 메소드와 static 변수가 있으니까 이를 이용해서 코드를 짜 보았다.

```
class Dog {
    public name: string;
    private age: number;
    public static numTail: number;

    constructor(name, age) {
        this.name = name;
        this.age = age;
        Dog.numTail = 1;
    }

    hi(): void {
      console.log(`Hello I am ${this.name} and I am ${this.age} years old`);  
    }

    static wow(): void {
        console.log(`We are Dogs and We have ${Dog.numTail} tail(s)!`);
    }
}

function foo(d: Dog) : void {
    d.hi();
}

const d1 = new Dog('Nabi', 3);
const d2 = new Dog('Zelda', 10);

foo(d1);
d2.hi();
Dog.wow();

```

이제 컴파일하고 실행을 해 보자.
```
$ tsc example.ts
$ node examle.js
Hello I am Nabi and I am 3 years old
Hello I am Zelda and I am 10 years old
We are Dogs and We have 1 tail(s)!  

```

잘 된다. 그럼 마지막으로 변환된 코드를 확인해 보았다.

```
var Dog = (function () {
    function Dog(name, age) {
        this.name = name;
        this.age = age;
        Dog.numTail = 1;
    }
    Dog.prototype.hi = function () {
        console.log("Hello I am " + this.name + " and I am " + this.age + " years old");
    };
    Dog.wow = function () {
        console.log("We are Dogs and We have " + Dog.numTail + " tail(s)!");
    };
    return Dog;
})();
function foo(d) {
    d.hi();
}
var d1 = new Dog('Nabi', 3);
var d2 = new Dog('Zelda', 10);
foo(d1);
d2.hi();
Dog.wow();

```

당연한 결과겠지만, prototype과 생성자 함수를 이용해서 클래스를 생성하는 것을 확인할 수 있었다. JS에 대한 지식이 +0.1 되었다.