+++
categories = ["programming"]
date = 2020-11-17T02:36:47Z
description = "JVM으로 자바 코드를 실행해 보자."
tags = ["jvm", "study", "java"]
title = "백기선 자바 스터디 1: JVM과 자바 실행"

+++
## Java Virtual Machine (JVM)

* [위키 링크]([https://en.wikipedia.org/wiki/Java_virtual_machine_](https://en.wikipedia.org/wiki/Java_virtual_machine)
* 자바 프로그램을 실행할 수 있는 가상 머신
* 바이트코드로 컴파일할수 있는 다른 프로그래밍 언어(Kotlin, Groovy) 도 실행할 수 있다.
* JVM 위에서 돌아가는 프로그래밍 언어도 만들 수 있을 것 같다. [유튜브 링크](https://www.youtube.com/watch?v=14hqB7Q0I58)

## .java 컴파일

* 터미널에서 컴파일하는 방법이 가장 간단

```
javac <옵션> <소스파일>
```

### 유용한 옵션

`javac --help` 로 옵션을 확인할 수 있다.

```
 --class-path <path>, -classpath <path>, -cp <path>
        Specify where to find user class files and annotation processors
  -d <directory>               Specify where to place generated class files
  -g                           Generate all debugging info
  --help, -help, -?            Print this help message
  --source <release>, -source <release>
        Provide source compatibility with the specified Java SE release. Supported releases: 7, 8, 9, 10, 11, 12, 13, 14
  --target <release>, -target <release>
        Generate class files suitable for the specified Java SE release. Supported releases: 7, 8, 9, 10, 11, 12, 13, 14
  -verbose                     Output messages about what the compiler is doing
  --version, -version          Version information
  ```

## 자바 실행하기

- 메인 클래스로 실행
- jar 파일 실행
- 필요한 모듈 지정
- **단일 파일 소스로 직접 실행** 

꿀팁! 단일 파일로 실행할 경우 소스로부터 실행할 수 있다.

```
Usage: java [options] <mainclass> [args...]
           (to execute a class)
   or  java [options] -jar <jarfile> [args...]
           (to execute a jar file)
   or  java [options] -m <module>[/<mainclass>] [args...]
       java [options] --module <module>[/<mainclass>] [args...]
           (to execute the main class in a module)
   or  java [options] <sourcefile> [args]
           (to execute a single source-file program)
```

### 기타 유용한 자바 관련 콘솔 명령

- javap: 디스어셈블러
- jdb: 디버거

## 바이트코드

- Bytecode는 가상머신이 실행할 수 있는 2진코드다. 
- [오라클 문서 링크](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html) 를 보면 JVM의 인스트럭션 셋을 직접 볼 수 있는데 일반적인 기계어보다 약간 추상화되어 있어서 명령이 더 직관적이고 이해하기 쉽다.

Hello.java

```
cat Hello.java
public class Hello {
	public static void main(String[] args) {
		System.out.println("Hello, CodeSquad!\n");
	}
}
```

16진수 덤프

```
xxd Hello.class
00000000: cafe babe 0000 003a 001d 0a00 0200 0307  .......:........
00000010: 0004 0c00 0500 0601 0010 6a61 7661 2f6c  ..........java/l
00000020: 616e 672f 4f62 6a65 6374 0100 063c 696e  ang/Object...<in
00000030: 6974 3e01 0003 2829 5609 0008 0009 0700  it>...()V.......
00000040: 0a0c 000b 000c 0100 106a 6176 612f 6c61  .........java/la
00000050: 6e67 2f53 7973 7465 6d01 0003 6f75 7401  ng/System...out.
00000060: 0015 4c6a 6176 612f 696f 2f50 7269 6e74  ..Ljava/io/Print
00000070: 5374 7265 616d 3b08 000e 0100 1248 656c  Stream;......Hel
00000080: 6c6f 2c20 436f 6465 5371 7561 6421 0a0a  lo, CodeSquad!..
00000090: 0010 0011 0700 120c 0013 0014 0100 136a  ...............j
000000a0: 6176 612f 696f 2f50 7269 6e74 5374 7265  ava/io/PrintStre
000000b0: 616d 0100 0770 7269 6e74 6c6e 0100 1528  am...println...(
000000c0: 4c6a 6176 612f 6c61 6e67 2f53 7472 696e  Ljava/lang/Strin
000000d0: 673b 2956 0700 1601 0005 4865 6c6c 6f01  g;)V......Hello.
000000e0: 0004 436f 6465 0100 0f4c 696e 654e 756d  ..Code...LineNum
000000f0: 6265 7254 6162 6c65 0100 046d 6169 6e01  berTable...main.
00000100: 0016 285b 4c6a 6176 612f 6c61 6e67 2f53  ..([Ljava/lang/S
00000110: 7472 696e 673b 2956 0100 0a53 6f75 7263  tring;)V...Sourc
00000120: 6546 696c 6501 000a 4865 6c6c 6f2e 6a61  eFile...Hello.ja
00000130: 7661 0021 0015 0002 0000 0000 0002 0001  va.!............
00000140: 0005 0006 0001 0017 0000 001d 0001 0001  ................
00000150: 0000 0005 2ab7 0001 b100 0000 0100 1800  ....*...........
00000160: 0000 0600 0100 0000 0100 0900 1900 1a00  ................
00000170: 0100 1700 0000 2500 0200 0100 0000 09b2  ......%.........
00000180: 0007 120d b600 0fb1 0000 0001 0018 0000  ................
00000190: 000a 0002 0000 0003 0008 0004 0001 001b  ................
000001a0: 0000 0002 001c                           ......
```

javap로 디스어셈블

```
javap -c Hello
Compiled from "Hello.java"
public class Hello {
  public Hello();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: getstatic     #7                  // Field java/lang/System.out:Ljava/io/PrintStream;
       3: ldc           #13                 // String Hello, CodeSquad!\n
       5: invokevirtual #15                 // Method java/io/PrintStream.println:(Ljava/lang/String;)V
       8: return
}
```

- [TODO] 직접 바이트코드로 1-100까지 더하는 프로그램을 작성해 보자.


## JIT 컴파일러

- [참고문서](https://docs.oracle.com/en/java/javase/14/vm/java-hotspot-virtual-machine-performance-enhancements.html#GUID-1D9B26AD-8E0A-4771-90DA-A81A2C1F5B55)
- Just In Time Compiler: 실행시간에 바이트코드를 네이티브 코드로 변환해서 성능을 높여준다. 대신 시작시간이 조금 늦어질 수도 있다.
- 오라클 JVM의 경우 HotSpot VM부터 도입된 기능인 것 같다.
- Graal VM과 Ahead-of-Time 컴파일러 키워드도 발견했는데 차후에 살펴보자. (과연)
- AoT 컴파일러: vm 시작전 바이트코드를 네이티브 코드로 컴파일해서 자바 어플리케이션 시작 성능을 개선할 수 있다.

## JVM 구성 요소

- [링크](https://www.geeksforgeeks.org/jvm-works-jvm-architecture/)

![JVM components](https://media.geeksforgeeks.org/wp-content/uploads/jvm-3.jpg)

- 클래스로더: 로딩, 링링, 초키화 담당

### JVM 메모리 구조

- 메소드 영역: 모든 클래스 정보와 static 변수가 저장됨
- 힙영역: 객체가 저장됨. gc 대상
- 스택 영역: per thread 자료구조. 메소드의 스택으로 사용됨
- PC 레지스터스: per thread 자료구조. 각 스레드의 PC를 저장함
- 네이티브 메소드 스택: per thread 자료구조. 네이티브 메소드의 스택으로 사용된다고 한다. (JNI를 쓰면 여길 사용할까 궁금함)

## JDK와 JRE의 차이

- [링크](https://stackoverflow.com/questions/1906445/what-is-the-difference-between-jdk-and-jre)
- JRE: 라이브러리, JVM, 애플릿을 돌리기 위해 필요한 컴포넌트 등으로 구성됨
- JDK: JRE + 컴파일러, 디버거 등 개발에 필요한 도구가 추가됨
